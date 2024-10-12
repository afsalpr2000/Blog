from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_description = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    id_proof = models .ImageField(upload_to = 'images/', blank=True, null=True)
    phone = models.CharField(max_length = 13,blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length = 40)
    content = models.TextField()
    blog_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=20,default='Published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    STATUS_CHOICES = [
    ('visible', 'Visible'),
    ('hidden', 'Hidden'),
]
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='visible')


    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']