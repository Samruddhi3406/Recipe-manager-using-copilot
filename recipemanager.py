#create a recipe manager application using python add features like add recipe with ingredients,view saved recipes,favourite recipes list,serving size calculator,meal planner for the week,serch recipes by ingredient or name
class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.favorites = []

    def add_recipe(self, name, ingredients):
        self.recipes.append({'name': name, 'ingredients': ingredients})

    def view_recipes(self):
        for recipe in self.recipes:
            print(f"{recipe['name']} - Ingredients: {', '.join(recipe['ingredients'])}")

    def add_to_favorites(self, name):
        for recipe in self.recipes:
            if recipe['name'] == name:
                self.favorites.append(recipe)

    def view_favorites(self):
        for recipe in self.favorites:
            print(f"{recipe['name']} - Ingredients: {', '.join(recipe['ingredients'])}")

    def serving_size_calculator(self, name, servings):
        for recipe in self.recipes:
            if recipe['name'] == name:
                print(f"{name} for {servings} servings: {', '.join(recipe['ingredients'])}")

    def meal_planner(self):
        # This is a placeholder for the meal planner functionality
        print("Meal Planner: Plan your meals for the week!")

    def search_recipes(self, query):
        results = [r for r in self.recipes if query in r['name'] or query in ', '.join(r['ingredients'])]
        for recipe in results:
            print(f"{recipe['name']} - Ingredients: {', '.join(recipe['ingredients'])}")
# Example usage
manager = RecipeManager()
manager.add_recipe("Pasta", ["Noodles", "Tomato Sauce", "Cheese"])
manager.add_recipe("Salad", ["Lettuce", "Tomatoes", "Cucumbers"])
manager.add_recipe("Sandwich", ["Bread", "Ham", "Cheese"])
manager.add_recipe("Soup", ["Broth", "Vegetables", "Chicken"])
manager.add_recipe("Pizza", ["Dough", "Tomato Sauce", "Cheese"])
manager.view_recipes()
manager.add_to_favorites("Pasta")
manager.view_favorites()
manager.serving_size_calculator("Pasta", 4)
manager.meal_planner()
manager.search_recipes("Cheese")
