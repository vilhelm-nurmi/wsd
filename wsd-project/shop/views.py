from django.shortcuts import render
from django.http import HttpResponse,Http404
from hashlib import md5
import uuid
from games.models import Game,Transaction
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test

@login_required(login_url='/login')
def error(request):
    #return HttpResponse('toplist')
    if request.method == 'GET':
        pid = request.GET['pid']
        ref = request.GET['ref']
        result = request.GET['result']
        checksum = request.GET['checksum']
        try:
            transaction=Transaction.objects.get(pid=pid)
            secret_key = transaction.secret_key
            if request.user != transaction.user:
                raise Http404
        except:
            raise Http404
        checksumstr="pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        if md5(checksumstr.encode('ascii')).hexdigest() == checksum and result == "error":
            transaction.status= Transaction.ERROR
            transaction.save()
        else:
            raise Http404
    return render(request,"shop/error.html",{'slug':transaction.game.slug})

@login_required(login_url='/login')
def cancel(request):
    #return HttpResponse('toplist')
    if request.method == 'GET':
        pid = request.GET['pid']
        ref = request.GET['ref']
        result = request.GET['result']
        checksum = request.GET['checksum']
        try:
            transaction=Transaction.objects.get(pid=pid)
            secret_key = transaction.secret_key
            if request.user != transaction.user:
                raise Http404
        except:
            raise Http404
        checksumstr="pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        if md5(checksumstr.encode('ascii')).hexdigest() == checksum and result == "cancel":
            transaction.status= Transaction.CANCEL
            transaction.save()
        else:
            raise Http404
    return render(request,"shop/cancel.html",{'slug':transaction.game.slug})

@login_required(login_url='/login')
def success(request,):
    if request.method == 'GET':
        pid = request.GET['pid']
        ref = request.GET['ref']
        result = request.GET['result']
        checksum = request.GET['checksum']
        try:
            transaction=Transaction.objects.get(pid=pid)
            secret_key = transaction.secret_key
            if request.user != transaction.user:
                raise Http404
        except:
            raise Http404
        checksumstr="pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        if md5(checksumstr.encode('ascii')).hexdigest() == checksum and result == "success":
            transaction.status = Transaction.SUCCESS
            transaction.save()
            transaction.user.purchased_games.add(transaction.game)
            transaction.user.save()
        else:
            raise Http404
    #return HttpResponse('toplist')
    else:
        raise Http404
    return render(request,"shop/success.html",{'slug':transaction.game.slug})
