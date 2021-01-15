from django.shortcuts import render
from .models import scavenges
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import huntCompletionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
dummyHunts = [
    {
        'title': 'Your bathroom',
        'input': 'picture of your nice clean bathroom for everyone to see',
        'input_type': 'picture'
    },
    {
        'title': 'Your bedroom',
        'input': 'Picture of your boring sex life',
        'input_type': 'picture'
    },

]
def home(request):
    context = {'hunts': dummyHunts}
    return render(request, 'birthdayhunt/home.html', context)

def about(request):
    return render(request, 'birthdayhunt/about.html')

@login_required
def scavenges_view(request):
    if request.method == 'POST':
        c_form = huntCompletionForm(request.POST, instance=request.user)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Hunt has been updated')
            return redirect('hunt-scavenges')

    else:
        c_form = huntCompletionForm(instance=request.user)
       

    context = {
        'c_form': c_form,
        'hunts': scavenges.objects.all()
    }

    return render(request,'birthdayhunt/scavenges.html', context)