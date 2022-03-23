from db import db_session
from models import Ingredient, Cocktail


def ingredients_in_cocktail_joined(ingredient_name):
    query = db_session.query(Cocktail, Ingredient).join(
        Ingredient, Cocktail.ingredient_id == Ingredient.id
    ).filter(Ingredient.name == ingredient_name)
    cocktail_list = []
    for cocktail, ingredient in query:
            cocktail_list.append(f'{ingredient.name} - {cocktail.name}')
    return cocktail_list


if __name__ == '__main__':
    pass