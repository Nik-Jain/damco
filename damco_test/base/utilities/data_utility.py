import time
import traceback
import pandas as pd
import numpy as np
from ..models import MeasuringUnit, Ingredient, Cuisine, MealType, MeatType, MeatClass, RecipeType, Recipe, RecipeIngredient, CookTime, Nutrients

def save_excel_data(path:str):
    success_count = 0
    failure_count = 0
    try:
        df = pd.read_excel(path, sheet_name=['Recipe', 'Ingredients', 'CookTime', 'Nutrients'])

        for _, row in df['Recipe'].iterrows():
            try:
                recipe = Recipe(
                        name = row.Recipe_Name,
                        alternate_name = row.Alternate_Name,
                        recipe_type= RecipeType.objects.get_or_create(type=row.Recipe_Type)[0],
                        description = row.Description,
                        meat_type = MeatType.objects.get_or_create(type=row.Meat_Type)[0],
                        meat_class = MeatClass.objects.get_or_create(type=row.Meat_Classification)[0],
                        cuisine = Cuisine.objects.get_or_create(type=row.Cuisine)[0],
                        serving_quantity = row.Serving_Quantity,
                        serve = row.Serve,
                        meal_type = MealType.objects.get_or_create(type=row.meal_type)[0],
                        cookware = row.Cookware,
                        calories_per_serving = row.Calories_per_Serving,
                        cooking_steps = row.cooking_steps,
                        pre_cooking_steps = row.pre_cooking_steps,
                        cook_tip = row.cook_tip,
                        serve_tip = row.serve_tip,
                        other_tip = row.other_tip)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                failure_count += 1
                continue
            recipe.save()
            try:
                recipe_ingredients = df['Ingredients'].loc[df['Ingredients']['Recipe_Name'] == recipe.name]
                recipe_ingredient_created = []
                for _, each_ingredient in recipe_ingredients.iterrows():
                    ingredient = Ingredient.objects.get_or_create(name=each_ingredient.Ingredient_Name)[0]
                    measuring_unit = MeasuringUnit.objects.get_or_create(unit_name=each_ingredient.Measuring_Unit)[0]
                    recipe_ingredient = RecipeIngredient(recipe=recipe,
                                                                        ingredient=ingredient,
                                                                        alternate_name=each_ingredient.Alternate_Name,
                                                                        quantity=each_ingredient.Quantity,
                                                                        measuring_unit=measuring_unit,
                                                                        variation= each_ingredient.Variation,
                                                                        comments= each_ingredient.Comments
                                                                        )
                    recipe_ingredient_created.append(recipe_ingredient)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                failure_count += 1
                continue
            [rec_ing.save() for rec_ing in recipe_ingredient_created]
            try:        
                cook_times_data = df['CookTime'].loc[df['CookTime']['Recipe_Name'] == recipe.name]
                for _, cook_time in cook_times_data.iterrows():
                    ct = CookTime(
                        recipe=recipe,
                        cook_time=0 if np.nan else cook_time.Cook_Time,
                        prep_time=0 if np.nan else cook_time.Prep_Time,
                        soak_time=0 if np.nan else cook_time.Soak_Time,
                        marinate_time=0 if np.nan else cook_time.Marinate_Time,
                        total_time=0 if np.nan else cook_time.Total_Time,
                    )
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                failure_count += 1
                continue
            ct.save()
            try:
                nutrients_data = df['Nutrients'].loc[df['Nutrients']['Recipe_Name'] == recipe.name]
                for _, nutrient_row in nutrients_data.iterrows():
                    nutrient = Nutrients(recipe=recipe,
                                                        energy=nutrient_row.Energy,
                                                        protein=nutrient_row.Protein,
                                                        kcal=nutrient_row.Kcal,
                                                        cal=nutrient_row.Cal,
                                                        carbohydrate=nutrient_row.Carbohydrate,
                                                        sugars=nutrient_row.Sugars,
                                                        fat=nutrient_row.Fat,
                                                        saturated_fat=nutrient_row.Saturated_Fat,
                                                        cholesterol=nutrient_row.Cholesterol,
                                                        calcium=nutrient_row.Calcium,
                                                        fibre=nutrient_row.Fibre,
                                                        sodium=nutrient_row.Sodium
                                                        )
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                failure_count += 1
                continue
            nutrient.save()
            success_count +=1

        return success_count, failure_count
    except Exception as e:
        failure_count += 1
        print(e)
        print(traceback.format_exc())
        return success_count, failure_count
