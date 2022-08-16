from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name='members_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def get_absolute_url(self):
        return reverse('members:post_detail',args=[self.slug,self.id])
    def __str__(self):
       return self.title

class Account(models.Model):
    phone = models.CharField(max_length=11)