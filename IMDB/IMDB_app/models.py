from django.db import models

# Create your models here.

from django.core.validators import RegexValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30) # name of the website 
    about= models.CharField(max_length=150)  # description,
    website= models.URLField(max_length=100) 

    contact = models.CharField(
        max_length=10,
        blank=True, null=True,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}-[0-9]{10}$',
            message=('Phone number must not excees 10 digits.')
        )]

    )
    
    def __str__(self):
        return self.name
        

class WatchList(models.Model):
    title =models.CharField(max_length=50)
    storyline=models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")# one movie can have one straming platform, on_delete cascade--> if platform delated all the movie from that platform will be deleted
    active=models.BooleanField(default=True) #movie is published or not
    created =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
    
     