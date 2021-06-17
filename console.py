from models.recipe import Recipe

import repositories.recipe_repository as recipe_repository

recipe_1 = Recipe("Eggs", "Get eggs", "Cook the eggs", "Jon", "brekky", 5, 2)
recipe_repository.save(recipe_1)

print(recipe_repository.select_all())