from db.run_sql import run_sql

from models.recipe import Recipe

def save(recipe):
    sql = "INSERT INTO recipes (name, ingredients, instructions, author, category, cooking_time, difficulty) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [recipe.name, recipe.ingredients, recipe.instructions, recipe.author, recipe.category, recipe.cooking_time, recipe.difficulty]
    results = run_sql(sql, values)
    id = results[0]['id']
    recipe.id  = results[0]['id']
    return recipe

def select_all():
    recipes = []

    sql = "SELECT * FROM recipes"
    results = run_sql(sql)

    for row in results:
        recipe = Recipe(row['name'], row['ingredients'], row['instructions'], row['author'], row['category'], row['cooking_time'], row['difficulty'], row['id'],)
        recipes.append(recipe)
        
    return recipes
