from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.http import HttpResponse,Http404
from .models import CustomUser
from games.models import Game
from django.contrib import messages
from django.conf import settings
from .forms import CustomUserCreationForm,CustomUserChangeForm,EditProfile
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required
from accounts.verification import is_player, owns_game, is_developer
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        #ifall metoden är post(svarar på formuläret)far det hit men om den är ogiltig far den till den "orginella formen"
        form = CustomUserCreationForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            if user.email != None:
                subject = 'Email verification for Miniclick'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]
                name=""
                if user.first_name:
                    name= user.first_name
                code = user.personal_secret_key
                messu = ["""Thank you for using Miniclick, """,str(name),"""! \n \n To verify your account go to profiles and press the verify link and insert your secret key\n This is your secret key: """, str(code),"""\n \n T. \n Miniclick Staff"""]
                verification_message = ''.join(messu)
                send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=verification_message, fail_silently=True)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {'form':form})

#Visar ett login formulär
def login_view(request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            try:
                return redirect(request.GET['next'])
            except:
                return redirect('/')


    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})

#Loggar ut användaren
def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/')




@login_required(login_url="/login")
def verify_account(request,link):
    user = request.user
    if request.method == 'POST':
        try:
            secretkey = int(request.POST['code'])
            if secretkey == user.personal_secret_key:
                user.verified = True
                user.save()
                return redirect('/')
            else:
                messages.error(request, 'Wrong validation-key, please check your email.')
                return render(request, 'accounts/verify_account.html')
        except ValueError:
            messages.info(request, 'Please only type your code as numbers and not as characters')
            return render(request, 'accounts/verify_account.html')
    return render(request, 'accounts/verify_account.html')

def add_email(request, link):
    if request.method=='POST':
        user = request.user
        email = request.POST['change_email']
        user.email = email
        user.save()
        subject = 'Email verification for Miniclick'
        from_email = settings.EMAIL_HOST_USER
        name = user.first_name
        to_email = [user.email]
        code = user.personal_secret_key
        messu = ["""Thank you for using Miniclick """,str(name),"""! \n \n To verify your account go to profiles and press the verify link and insert your secret key\n This is your secret key: """, str(code),"""\n \n T. \n Miniclick Staff"""]
        verification_message = ''.join(messu)
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=verification_message, fail_silently=False)
    return redirect('/profile/'+user.username+'/verify/')

def resend_email(request, link):
    if request.method == 'POST':
        user = request.user
        subject = 'Email verification for Miniclick'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        name = user.first_name
        code = user.personal_secret_key
        messu = ["""This is a reminder of your secret key, """,str(name),""" \n \n To verify your account go to profiles and press the verify link and insert your secret key\n This is your secret key: """, str(code),"""\n \n T. \n Miniclick Staff"""]
        verification_message = ''.join(messu)
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=verification_message, fail_silently=False)
    return redirect('/profile/'+user.username+'/verify/')

#Visar en användarprofil
def profile(request,link):
    try:
        profil = CustomUser.objects.get(username=link)
    except:
        raise Http404

    if request.method=="POST":
        if request.POST['delete']=="DELETE":
            try:
                game=Game.objects.get(id=request.POST['game'])
            except:
                return render(request, 'accounts/profile.html', {'profil': profil})
            try:
                if is_developer(request.user):
                    if owns_game(game,request.user):
                        game.delete()
                        return render(request, 'accounts/profile.html', {'profil': profil})
            except:
                return render(request, 'accounts/profile.html', {'profil': profil})
    try:
        profil = CustomUser.objects.get(username=link)
    except:
        raise Http404

    return render(request, 'accounts/profile.html', {'profil': profil})


@login_required(login_url='/login')
def change_profile(request,link):
    try:
        profil = CustomUser.objects.get(username=link)
    except:
        raise Http404

    if(request.user == profil):
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES,instance=request.user)
            if form.is_valid():
                try:
                    profil.profile_img = request.FILES['profile_img']
                except:
                    profil.profile_img = profil.profile_img
                profil = form.save()
                profil.save()
                render(request, 'accounts/edit_profile.html', {"form": form,'profil':profil})
        else:
            form = EditProfile(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {"form": form,'profil':profil})

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
