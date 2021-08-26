from django.urls import path, include
from .views import *


urlpatterns=[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('user/<int:pk>/profile/', UserProfileDetailUpdate.as_view(), name='user-profile'),
    path('create-book/', CreatChefBook.as_view(), name='chef-book'),
    path('chef-list/', ChefListApiView.as_view(), name='chef-list')


]

