# from django.shortcuts import render
# from IMDB_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.


# #function based view
# def movie_list(request):
#     movies = Movie.objects.all()#selected data in the form of QuerySet
    # data = { # list converting into Dictionary 
        # 'movies': list(movies.values()) #converting into list 
    #     }
    # return JsonResponse(data) #used json response to send this dictionary 
    

# def movie_details(request, pk):
#     movie=Movie.objects.get(pk=pk)
#     data = {
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active,
#     }
#     return JsonResponse(data)
