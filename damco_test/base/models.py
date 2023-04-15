from django.db import models

# Create your models here.
    
class MeasuringUnit(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    unit_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Cuisine(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class MealType(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class MeatType(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class MeatClass(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class RecipeType(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Recipe(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, unique=True)
    alternate_name = models.CharField(max_length=200, null=True)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True)
    meat_type = models.ForeignKey(MeatType, on_delete=models.SET_NULL, null=True)
    meat_class = models.ForeignKey(MeatClass, on_delete=models.SET_NULL, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True)
    serving_quantity = models.CharField(max_length=200, null=True)
    serve = models.CharField(max_length=200, null=True)
    meal_type = models.ForeignKey(MealType, on_delete=models.SET_NULL, null=True)
    cookware = models.CharField(max_length=200, null=True)
    calories_per_serving = models.FloatField(default=0.0, null=True)
    cooking_steps = models.TextField(max_length=1000, null=True)
    pre_cooking_steps = models.TextField(max_length=1000, null=True)
    cook_tip = models.TextField(max_length=1000, null=True)
    serve_tip = models.TextField(max_length=1000, null=True)
    other_tip = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    alternate_name = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=200)
    measuring_unit = models.ForeignKey(MeasuringUnit, on_delete=models.SET_NULL, null=True)
    variation = models.TextField(max_length=1000, null=True)
    comments = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CookTime(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    cook_time = models.IntegerField(null=True)
    prep_time = models.IntegerField(null=True)
    soak_time = models.IntegerField(null=True)
    marinate_time = models.IntegerField(null=True)
    total_time = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Nutrients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    energy = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    kcal = models.FloatField(null=True)
    cal = models.FloatField(null=True)
    carbohydrate = models.FloatField(null=True)
    sugars = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    saturated_fat = models.FloatField(null=True)
    cholesterol = models.FloatField(null=True)
    calcium = models.FloatField(null=True)
    fibre = models.FloatField(null=True)
    sodium = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
