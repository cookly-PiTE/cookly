import pandas as pd
import json
from pymongo import MongoClient
from decouple import config
import uuid


def get_recipe(recipe):
    if (
        recipe["difficulty"]
        and recipe["course"]
        and recipe["cooking_method"]
        and recipe["photo_url"]
    ):
        if recipe["dietary_considerations"]:
            is_vegetarian = "vegetarian" in recipe["dietary_considerations"]
        else:
            is_vegetarian = False

        ingredients = [{"name": name} for name in recipe["ingredients"]]
        instructions = " ".join(recipe["instructions"])
        recipe_dict = {
            "id": uuid.uuid1(),
            "name": recipe["title"],
            "description": recipe["description"],
            "instructions": instructions,
            "ingredients": ingredients,
            "image_url": recipe["photo_url"],
            "course_type": recipe["course"],
            "difficulty": recipe["difficulty"],
            "cooking_method": recipe["cooking_method"],
            "cost": recipe["cost"],
            "is_vegetarian": is_vegetarian,
        }

        if recipe_dict["cost"] == "Splurge":
            recipe_dict["cost"] = "Expensive"

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

    client = MongoClient(config("DB_HOST"))

    db = client[config("DB_NAME")]
    collection = db["recipes_recipe"]

    recipes.reset_index(inplace=True)
    recipes_dict = recipes.to_dict("records")

    collection.insert_many(recipes_dict)
