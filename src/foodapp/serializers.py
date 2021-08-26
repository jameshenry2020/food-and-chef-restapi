
from rest_framework import serializers
from .models import Category, Food, FoodRecipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'name']

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodRecipe
        fields=['id','procedure', 'cooking_duration']

class FoodSerializer(serializers.ModelSerializer):
    chef=serializers.StringRelatedField(read_only=True)
    recipes=FoodRecipeSerializer(many=True)
    class Meta:
        model=Food
        fields=['id', 'name','category', 'description', 'ingredience', 'nutritional_value', 'origin','picture','chef', 'recipes']

    def create(self, validated_data):
        recipe_data=validated_data.pop('recipes')
        food=Food.objects.create(**validated_data)
        for recipe in recipe_data:
            FoodRecipe.objects.create(food=food, **recipe)
        return food


    def update(self, instance, validated_data):
        recipe_data=validated_data.pop('recipes')
        pre_recipes=(instance.recipes).all()
        pre_recipes=list(pre_recipes)
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.ingredience = validated_data.get('ingredience', instance.ingredience)
        instance.nutritional_value = validated_data.get('nutritional_value', instance.nutritional_value)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()

        for recipe in recipe_data:
            recipe_obj=pre_recipes.pop(0)
            recipe_obj.procedure=recipe.get('procedure', recipe_obj.procedure)
            recipe_obj.cooking_duration=recipe.get('cooking_duration', recipe_obj.cooking_duration)
            recipe_obj.save()
        return instance



     

