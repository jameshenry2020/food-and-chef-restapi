from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import ChefBook, Profile, User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=['id','email','username','first_name','last_name']



class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model=User
        fields=['id', 'username','first_name','last_name','email']

class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Profile
        fields=['id','bio','image','phone','country', 'user']

    def update(self, instance, validated_data):
        instance.bio=validated_data.get('bio', instance.bio)
        instance.image=validated_data.get('image', instance.image)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.country=validated_data.get('country', instance.country)
        instance.save()
        return instance
        
    
   
class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChefBook
        fields=['id','name']
