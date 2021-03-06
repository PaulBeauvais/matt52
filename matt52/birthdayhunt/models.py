from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class scavenges(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Points = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title  # What you want to show
    
    class Meta:
        verbose_name_plural = "scavenges"
    

class complete_scavenges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    huntId = models.ForeignKey(scavenges, on_delete=models.CASCADE)
    proof = models.ImageField(default='Lier-vs.-Liar.jpg', upload_to='proof_pics/')
    finish_time = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        verbose_name_plural = "complete scavenges"

    def __str__(self):
        return f'{self.user} | {self.id}' # What you want to showhun

class finished_hunters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finish_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Finished Hunters"

    def __str__(self):
        return f'{self.user} ' # What you want to showhun