from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = Message()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.mymessage = form.cleaned_data['mymessage']
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    diction = {}
    return render(request, 'home.html', context = diction)

def wrong(request):
    diction = {}
    return render(request, 'wrong.html', context = diction)
