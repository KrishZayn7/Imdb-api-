from django.contrib import admin
from IMDB_app.models import WatchList, StreamPlatform #importing for watchlist class from model.py 

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform) 