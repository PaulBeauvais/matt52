from django.shortcuts import render
from .models import scavenges
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import huntCompletionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'birthdayhunt/home.html')

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
        'hunts': scavenges.objects.all()
    }

    return render(request,'birthdayhunt/scavenges.html', context)