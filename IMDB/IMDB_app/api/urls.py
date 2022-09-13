
from django.urls import path,include
# from IMDB_app.api.views import movie_list,movie_detail
from IMDB_app.api.views import StreamPlatformDetailAV, WatchListAV,WatchDetailAV,StreamPlatformAV

urlpatterns = [
    # path('list/', movie_list,name='movie-list'),
    # path('<int:pk>', movie_details,name='movie-detail'),
    
    path('list/', WatchListAV.as_view(), name='MovieList'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='Movie detail'), 
    path('stream/', StreamPlatformAV.as_view(), name='Stream Platform'), 
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='Stream details'), 
    
    
]
