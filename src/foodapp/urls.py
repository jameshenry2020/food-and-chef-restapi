from django.urls import path
from .views import *

urlpatterns=[
    path('add-category/', AddFoodCategoryApiView.as_view(), name='add-category'),
    path('food-categories/', ListFoodCategoryApiView.as_view(), name='list-category'),
    path('add-food/', CreateFoodApiView.as_view(), name='add-food'),
    path('get-food/', FoodFilterApiView.as_view(), name='search-food'),
    path('edit-food/<int:pk>/', FoodUpdateAndDeleteApiView.as_view(), name='edit-food'),
    path('food-recipes/', FoodListApiView.as_view(), name='food-list'),
    path('food-detail/<int:pk>/', FoodDetailApiView.as_view(), name='food-detail')
]