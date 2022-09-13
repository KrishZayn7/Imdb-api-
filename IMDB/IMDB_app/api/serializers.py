from multiprocessing import managers
from rest_framework import serializers
from IMDB_app.models import WatchList,StreamPlatform


#---Model Serializer----------------------------------------

class WatchListSerializer(serializers.ModelSerializer):
    
    # len_name=serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields =['id','name','description']
        # exclude =['active']
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True,read_only=True) # "watchlist" is from the models related_name from the nested 
    
    class Meta:
        model=StreamPlatform
        fields ='__all__' 






#     def get_len_name(self,object):
#         return len(object.name)
        
# #in the ModelSerializer we dont have to map the method name as it is defaul populated
#     def validate_name(self,value): # this is field level validation of "name", use class validate_<filed_name>
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         return value  
     
#     def validate(self,data): #object-level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be differnet")
#         else:
#             return data


#------------Serializer------------------------------------
#validation using validator by creating method for it and using it 
# def name_length(value): # we dont use self as it is not inside our class
#     if len(value) < 2:
#         raise serializers.ValidationError("Name too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    #if the request is POST we use create 
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    
    #now for the PUT request we use update 
    # def update(self,instance,validated_data): #instance carry old values and validated_data carry new values
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.active=validated_data.get('active')
    #     instance.save()
    #     return instance
    
    # def validate_name(self,value): # this is field level validation of "name"
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     return value  
    
    # def validate(self,data): #object-level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should be differnet")
    #     else:
    #         return data
        
         