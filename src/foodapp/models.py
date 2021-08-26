from django.db import models
from authentications.models import ChefBook

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField()
    ingredience=models.TextField()
    nutritional_value=models.CharField(max_length=255)
    origin=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='food', blank=True, null=True)
    chef=models.ForeignKey(ChefBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class FoodRecipe(models.Model):
    food=models.ForeignKey(Food, related_name='recipes', on_delete=models.CASCADE)
    procedure=models.TextField()
    cooking_duration=models.CharField(max_length=100)

    def __str__(self):
        return self.food.name
