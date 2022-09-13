from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from IMDB_app.models import WatchList,StreamPlatform
from IMDB_app.api.serializers import StreamPlatformSerializer, WatchListSerializer
from rest_framework import status 


class WatchListAV(APIView): 
    def get(self,request):
        movies =WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    

class StreamPlatformAV(APIView):
    
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':' not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer =WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

#create a detail about the streaming platform 

class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            streams=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializers=StreamPlatformSerializer(streams)
        return Response (serializers.data)
    
    def put(self,request,pk):
        streams=StreamPlatform.objects.get(pk=pk)
        serializers=StreamPlatformSerializer(streams,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        streams=StreamPlatform.objects.get(pk=pk)
        streams.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







#function based view 

    
# @api_view(['GET', 'POST']) # function based view 
# def movie_list(request):
    
#     if request.method =='GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many =True) #we defined may-true becaues as the serializer access multiple objects we have to write it 
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if  request.method=='GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
     