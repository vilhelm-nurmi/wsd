from django.shortcuts import render,redirect
from .models import Game,Highscore,SavedGame,Transaction
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from accounts.verification import is_player, owns_game, is_developer
import uuid
from hashlib import md5
from .forms import GameForm,GameForm2
from django.http import JsonResponse

#loading all games on one page in alphabetic order
def game_list(request):
    games = Game.objects.all().order_by('title')
    return render(request,'games/game_list.html',{'games':games})

#Loading a single game page
def game_page(request,link):
    try:
        game = Game.objects.get(slug = link)
        amount = game.price
    except:
        raise Http404
    #Hit ska ja sätta hela payment infon!
    host = request.get_host()
    if host=="localhost:8000":
        host="http://localhost:8000"
    #Not creating an transaction if the user owns the game
    if owns_game(game,request.user):
        return render(request,'games/game_view.html',{'game':game})
    elif is_developer(request.user):
        return render(request,'games/game_view.html',{'game':game})
    #Filtering out anonymous users
    elif not request.user.is_anonymous:

        #Creating a new transaction if not
        if not Transaction.objects.filter(user=request.user,game=game):
            pid = uuid.uuid4()
            sid = "miniclick123"
            secret_key = "fc3e19550f6d7bf66301439837c77aac"
            checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
            m = md5(checksumstr.encode("ascii"))
            checksum = m.hexdigest()
            transaction= Transaction.objects.create(user=request.user,game=game,pid=pid,sid=sid,secret_key=secret_key,checksum=checksum)
            transaction.save()
            dict = {'game': game, 'checksum':checksum,'pid':pid,'sid':sid,'key':secret_key,'host':host}
            return render(request, 'games/game_view.html', dict)

        else:
            #Reopening any pending transactions
            for transaction in Transaction.objects.filter(user=request.user,game=game):
                if transaction.status == Transaction.PENDING:
                    pid = transaction.pid
                    sid = transaction.sid
                    secret_key = transaction.secret_key
                    checksum = transaction.checksum
                    dict = {'game': game, 'checksum':checksum,'pid':pid,'sid':sid,'key':secret_key,'host':host}
                    return render(request, 'games/game_view.html', dict)

        #Creating a new transaction
        pid = uuid.uuid4()
        sid = "miniclick123"
        secret_key = "fc3e19550f6d7bf66301439837c77aac"
        checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()
        transaction= Transaction.objects.create(user=request.user,game=game,pid=pid,sid=sid,secret_key=secret_key,checksum=checksum)
        transaction.save()
        dict = {'game': game, 'checksum':checksum,'pid':pid,'sid':sid,'key':secret_key,'host':host}
        return render(request, 'games/game_view.html', dict)

    return render(request,'games/game_view.html',{'game':game})

#Loads the play view for a logged in player that has purchased the game
@login_required(login_url='/login')
def play_game(request,link):
    #Parsing ajax-post requests.
    if request.method=='POST' and request.is_ajax():

        if request.POST['type'] =='highscore':
            hscore = Highscore.objects.create(player=request.user, game_h=Game.objects.get(slug=link), score=request.POST['score'])
            hscore.save()
            return JsonResponse({'status':'Success', 'msg': 'Saved score successfully'})

        elif request.POST['type']=='save':
            if SavedGame.objects.filter(game=Game.objects.get(slug=link),player=request.user):
                SavedGame.objects.filter(game=Game.objects.get(slug=link),player=request.user).delete()
            sgame = SavedGame.objects.create(game=Game.objects.get(slug=link),player=request.user,save_POST = request.POST['game_state'])
            sgame.save()
            return JsonResponse({'status':'Success', 'msg': 'Saved game state successfully'})

        elif request.POST['type']=='load':
            sgame = SavedGame.objects.get(game=Game.objects.get(slug=link),player=request.user)
            return JsonResponse({'status':'Success', 'msg': sgame.save_POST})

        else:
            return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

    #Displaying the game
    try:
        game = Game.objects.get(slug=link)
    except:
        raise Http404
    #Checking that the game has been purchased before rendering.

    if game in request.user.purchased_games.all():
        game.times_played += 1
        game.save()
        return render(request,'games/play_game.html',{'game':game})
    return HttpResponseRedirect('/games/'+link)


@login_required(login_url='/login')
@user_passes_test(is_developer,login_url='/login')
def add_game(request):
    if request.method == 'POST':
        form=GameForm(request.POST,request.FILES)
        if form.is_valid():
            game=form.save()
            game.uploader=request.user
            game.save()
            request.user.purchased_games.add(game)
            return redirect('/games/list')
    else:
        form=GameForm()
    return render(request,'games/add_game.html', {'form':form})


@login_required(login_url='/login')
@user_passes_test(is_developer,login_url='/login')
def edit_game(request,link):
    try:
        game=Game.objects.get(slug=link)
    except:
        raise Http404
    if request.user != game.uploader:
        redirect('/profile/' + request.user.username )
    if request.method == 'POST':
        form=GameForm2(request.POST,request.FILES)
        if form.data['title']:
            game.title = form.data['title']
        if form.data['slug']:
            game.slug = form.data['slug']
        if form.data['price']:
            game.price = form.data['price']
        if form.data['url']:
            game.url = form.data['url']
        if form.data['description']:
            game.description = form.data['description']
        try:
            game.game_img=request.FILES['game_img']
        except:
            pass
        game.save()
        return redirect('/games/'+game.slug+'/edit')
    else:
        form=GameForm2(initial={'title':game.title,'slug':game.slug,'price':game.price,'url':game.url,'description':game.description,})
    return render(request,'games/game_edit.html', {'form':form,'game':game})

def highscores(request,link):

    try:
        game=Game.objects.get(slug=link)
        highscores = Highscore.objects.filter(game_h = game).order_by('-score')
    except:
        raise Http404

    return render(request,'games/highscores.html',{'gameslug':game.slug,'highscores':highscores})

@login_required(login_url='/login')
@user_passes_test(is_developer,login_url='/login')
def stats_game(request,link):
    try:
        game=Game.objects.get(slug=link)
    except:
        raise Http404
    times_sold=len(Transaction.objects.filter(game=game,status=Transaction.SUCCESS))
    return render(request, "games/stats_game.html",{"game":game,"sold":times_sold})
