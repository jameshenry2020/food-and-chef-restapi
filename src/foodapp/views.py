
from rest_framework import permissions
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from authentications.models import ChefBook
from foodapp.serializers import CategorySerializer, FoodSerializer
from django.shortcuts import render
from rest_framework.response import Response
from authentications.permissions import IsChef, IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView,ListAPIView,RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Food
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
# Create your views here.

class AddFoodCategoryApiView(CreateAPIView):
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated, IsChef]
    queryset=Category.objects.all()

class ListFoodCategoryApiView(ListAPIView):
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()

class CreateFoodApiView(GenericAPIView):
    serializer_class=FoodSerializer
    permission_classes=[IsAuthenticated, IsChef]
    parser_classes=[FormParser, JSONParser, MultiPartParser]
    def post(self, request, *args, **kwargs):
        data=request.data
        chef_obj=ChefBook.objects.get(chef=self.request.user)
        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(chef=chef_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class FoodListApiView(ListAPIView):
    serializer_class=FoodSerializer
    permission_classes=[IsAuthenticated]
    queryset=Food.objects.all()


class FoodDetailApiView(RetrieveAPIView):
    serializer_class=FoodSerializer
    queryset=Food.objects.all()
    permission_classes=[IsAuthenticated]
    lookup_field='pk'




class FoodFilterApiView(ListAPIView):
    serializer_class=FoodSerializer
    queryset=Food.objects.all()
    permission_classes=[IsAuthenticated]
    filter_backends=(SearchFilter,)
    search_fields=['name', 'category__name', 'origin']


class FoodUpdateAndDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=FoodSerializer
    queryset=Food.objects.all()
    permission_classes=[IsAuthenticated, IsChef, IsOwner]
    lookup_field='pk'
    