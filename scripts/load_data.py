import pandas as pd
import json


def get_recipe(recipe):
    if recipe["difficulty"] is not None and recipe["course"] is not None and recipe["cooking_method"] is not None:
        if recipe["dietary_considerations"] is not None:
            is_vegetarian = "vegetarian" in recipe["dietary_considerations"]
        else:
            is_vegetarian = False

        recipe_dict = {
            "name": recipe["title"],
            "description": recipe["description"],
            "instruction": recipe["instructions"],
            "course_type": recipe["course"],
            "difficulty": recipe["difficulty"],
            "cooking_method": recipe["cooking_method"],
            "cost": recipe["cost"],
            "is_vegetarian": is_vegetarian
        }
        return recipe_dict
    else:
        pass


def run():

    with open("recipes.json", "r") as f:
        data = f.read()

    json_recipes = json.loads(data)

    recipes = pd.DataFrame()

    for recipe in json_recipes:
        recipe_dict = get_recipe(recipe)
        recipes = recipes.append(recipe_dict, ignore_index=True)

    print(recipes.head(50))
    print(recipes.shape)