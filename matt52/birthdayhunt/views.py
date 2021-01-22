from django.shortcuts import render
from .models import scavenges, complete_scavenges, finished_hunters
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import huntCompletionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import datetime, date
from django.utils import timezone


#supporting funtions
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)





# Create your views here.

def home(request):
    users = User.objects.all()
    userids = [id.id for id in users]
    userResults = []


    firstPhoto = complete_scavenges.objects.all().order_by('-finish_time').first()
    #firstPhoto = firstPhoto.proof.url
    for user in users:
        userprofile = Profile.objects.filter(user=user.id).select_related()
        #userobject = User.objects.filter(id=user.id)
        userstarttime = timezone.localtime(user.date_joined)
        #userstarttime = elapsedtime(userstarttime.strftime("%b %d %Y %H:%M")
        elapsedtime = ''

        userendtime = finished_hunters.objects.filter(user=user).select_related()

        if userendtime:
            userendtime = timezone.localtime(userendtime[0].finish_time)
            elapsedtime =  userendtime - userstarttime
            endtimer = strfdelta(elapsedtime,"{days} days, {hours} hours, {minutes} minutes" )
            #print(f'1 {elapsedtime}')
        else:
            endtimer = 'in progress'
            userendtime = None


        points = complete_scavenges.objects.filter(user=user.id).select_related().aggregate(points=Sum('huntId__Points'))
        
        if points['points'] != None:
            userResults.append({'id': user.id, 'name': user.username, 'points': points['points'], 'endtimer': endtimer, 'userelapsedtime': elapsedtime })   
        else:
            pass
            #userResults.append({'id': user.id, 'name': user.username, 'points': 0, 'endtimer': endtimer, 'userelapsedtime': elapsedtime })
        
        userResults = sorted(userResults, key = lambda i: (i['points'], i['userelapsedtime']))

    context = {'users': userResults, 'photo': firstPhoto}

    return render(request, 'birthdayhunt/home.html', context)

def about(request):
    return render(request, 'birthdayhunt/about.html')

@login_required
def scavenges_view(request):
    if request.method == 'POST':
        c_form = huntCompletionForm(request.user.id, request.POST, request.FILES, initial={'user': request.user})
        print(c_form)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Hunt has been updated')
            return redirect('hunt-scavenges')
    else:
        #c_form = huntCompletionForm(initial={'user': request.user})  #works without filter
        c_form = huntCompletionForm(user = request.user, initial={'user': request.user}) #not working with filter
    
    
    userprofile = Profile.objects.filter(user=request.user).select_related()
    userstarttime = timezone.localtime(userprofile[0].starttime)
    userstarttime = userstarttime.strftime("%b %d %Y %H:%M")

    context = {
        'c_form': c_form,
        'completed_hunts': complete_scavenges.objects.filter(user=request.user).select_related(),
        'hunts': scavenges.objects.filter(~Q(complete_scavenges__user=request.user)).select_related(),
        'iscomplete': finished_hunters.objects.filter(user=request.user).select_related(),
        'starttime':  {'starttime': userstarttime},

        }
   

    return render(request,'birthdayhunt/scavenges.html', context)


@login_required
def photos_view(request):
       
 
    context = {
        'photos': complete_scavenges.objects.filter(user=request.user).select_related().order_by('-finish_time'),

    }


    return render(request,'birthdayhunt/photos.html', context)


@login_required
def stop_timer_view(request):
       
    finisher = finished_hunters(user = request.user)
    finisher.save()

    return redirect('hunt-scavenges')