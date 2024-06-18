from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)#allows to delete the user and his post
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
     ordering=('-date_created',)#arrange post according to recent post

    def __str__(self) :
        return self.title #to show the tilte in the admin
