from django.shortcuts import render
from .models import scavenges, complete_scavenges
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import huntCompletionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import datetime


# Create your views here.

def home(request):
    users = User.objects.all()
    userids = [id.id for id in users]
    userResults = []

    for user in users:
        points = complete_scavenges.objects.filter(user=1).select_related().aggregate(points=Sum('huntId__Points'))
        userResults.append({'id': user.id, 'name': user.username, 'points': points['points']})   


    context = {'users': userResults}

    return render(request, 'birthdayhunt/home.html', context)

def about(request):
    return render(request, 'birthdayhunt/about.html')

@login_required
def scavenges_view(request):
    if request.method == 'POST':
        c_form = huntCompletionForm(request.POST, request.FILES)
        print(c_form)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Hunt has been updated')
            return redirect('hunt-scavenges')

    else:
        c_form = huntCompletionForm(initial={'user': request.user})
       
    context = {
        'c_form': c_form,
        'completed_hunts': complete_scavenges.objects.filter(user=request.user).select_related(),
        'hunts': scavenges.objects.filter(~Q(complete_scavenges__user=request.user)).select_related(),
         }


    return render(request,'birthdayhunt/scavenges.html', context)


@login_required
def photos_view(request):
       
 
    context = {
        'photos': complete_scavenges.objects.filter(user=request.user).select_related(),

    }


    return render(request,'birthdayhunt/photos.html', context)