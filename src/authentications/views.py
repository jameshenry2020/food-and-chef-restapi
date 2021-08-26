from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Profile, ChefBook, User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser,JSONParser, MultiPartParser
from rest_framework import status
from .serializers import ProfileSerializer,ChefSerializer, UserSerializer
# Create your views here.


class UserProfileDetailUpdate(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    parser_classes=[FormParser, JSONParser, MultiPartParser]

    def get(self, request,*args, **kwargs):
        profile=Profile.objects.get(user=self.request.user)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        profile=Profile.objects.get(user=self.request.user)
        serializer=ProfileSerializer(profile, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class CreatChefBook(CreateAPIView):
    serializer_class=ChefSerializer
    queryset=ChefBook.objects.all()
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)
        user_obj=self.request.user
        user_obj.is_chef=True
        user_obj.save()



   
class ChefListApiView(ListAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_chef=True)




