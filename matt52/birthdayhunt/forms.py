from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q




class huntCompletionForm(forms.ModelForm):
    class Meta:
        model = complete_scavenges
        fields = ['user', 'huntId', 'proof']

        widgets = {'user': forms.HiddenInput()}
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(huntCompletionForm, self).__init__(*args, **kwargs)

        self.fields['huntId'].queryset = scavenges.objects.filter(~Q(complete_scavenges__user=self.user)).select_related()