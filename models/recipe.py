class Recipe:

    def __init__(self, name, ingredients, instructions, author, category, cooking_time, difficulty, id = None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.author = author
        self.category = category
        self.cooking_time = cooking_time
        self.difficulty = difficulty
        self.id = id
     