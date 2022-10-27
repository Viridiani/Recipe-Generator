# Ingredients to include in the recipe
# Add specific ingredients option
import random
from constants import ingredients
from constants import measurements
from cookers import appliances as cooking_appliance
from constants import utensils
from constants import cooking
from constants import preparing
from constants import time


class Recipe:
    def __init__(self, name, items):
        self.name = name
        self.ingredients = self.make_ingredients(items)

    @staticmethod
    def make_item():
        new_item = {
                    'Amount': random.randint(1, 20),
                    'Measurement': measurements[random.randint(0, len(measurements)-1)],
                    'Ingredient': ingredients[random.randint(0, len(ingredients)-1)]}
        return new_item

    def make_ingredients(self, times):
        blank = []
        while times > 0:
            blank.append(self.make_item())
            times -= 1
        return blank

    def describe_ingredients(self):
        for thing in self.ingredients:
            temp = []
            for key, value in thing.items():
                temp.append(value)
            if temp[0] > 1:
                print(f"*{temp[0]} {temp[1]}s of {temp[2]}")
            else:
                print(f"*{temp[0]} {temp[1]} of {temp[2]}")

    @staticmethod
    def cook(ingredient):
        adj = cooking[random.randint(0, len(cooking)-1)]
        cook_time = time[random.randint(0, len(time)-1)]
        appliance = cooking_appliance[random.randint(0, len(cooking_appliance)-1)]
        rand_time = random.randint(1, 120)
        num = range(75, 500, 25)
        temp = num[random.randint(0, len(num)-1)]

        if ingredient['Amount'] != 0:
            use = random.randint(1, ingredient['Amount'])
        else:
            return None

        if (ingredient['Amount'] - use) < 0:
            use = abs(ingredient['Amount'] - use)
            ingredient['Amount'] = 0
        elif (ingredient['Amount'] - use) == 0:
            ingredient['Amount'] = 0
        else:
            ingredient['Amount'] -= use

        line = f"{adj.title()} {use} {ingredient['Measurement']}s {ingredient['Ingredient']} with a {appliance.lower()} for {rand_time} {cook_time}s at {temp} degrees Fahrenheit."
        return line

    @staticmethod
    def prepare(ingredient1, ingredient2):
        prep = preparing[random.randint(0, len(preparing)-1)]
        utensil = utensils[random.randint(0, len(utensils)-1)]

        if (ingredient1['Amount'] != 0) and (ingredient2['Amount'] != 0):
            use = random.randint(1, ingredient1['Amount'])
            use2 = random.randint(1, ingredient2['Amount'])
        else:
            return None

        if (ingredient1['Amount'] - use) < 0:
            use = abs(ingredient1['Amount'] - use)
            ingredient1['Amount'] = 0
        elif (ingredient1['Amount'] - use) == 0:
            ingredient1['Amount'] = 0
        else:
            ingredient1['Amount'] -= use

        if (ingredient2['Amount'] - use2) < 0:
            use2 = abs(ingredient2['Amount'] - use2)
            ingredient2['Amount'] = 0
        elif (ingredient2['Amount'] - use2) == 0:
            ingredient2['Amount'] = 0
        else:
            ingredient2['Amount'] -= use2

        line = f"{prep.title()} {use} {ingredient1['Measurement']}s {ingredient1['Ingredient']} and {use2} {ingredient2['Measurement']}s {ingredient2['Ingredient']} together with a {utensil}."
        return line

    def instruct(self):
        if len(self.ingredients) > 0:
            choose = random.randint(1, 2)
            if choose == 1:
                if len(self.ingredients) >= 2:
                    num = random.randint(0, len(self.ingredients)-1)
                    ingredient1 = self.ingredients[num]
                    num2 = random.randint(0, len(self.ingredients)-1)
                    while num == num2:
                        num2 = random.randint(0, len(self.ingredients)-1)
                    ingredient2 = self.ingredients[num2]

                    return self.prepare(ingredient1, ingredient2)
                else:
                    choose = 2
            if choose == 2:
                ingredient = self.ingredients[random.randint(0, len(self.ingredients)-1)]
                return self.cook(ingredient)
        else:
            return None

    def gen_recipe(self):
        instructions = []
        while len(self.ingredients) > 0:
            for item in self.ingredients:
                if item['Amount'] <= 0:
                    self.ingredients.remove(item)
            instructions.append(self.instruct())
        return instructions

    @staticmethod
    def fix_recipe(recipe):
        while None in recipe:
            recipe.remove(None)
        return recipe

    def format_recipe(self):
        print(f"{self.name} \n")
        self.describe_ingredients()
        print("\n")
        temp = self.gen_recipe()
        recipe = self.fix_recipe(temp)
        for item in recipe:
            index = recipe.index(item)
            print(f"{index + 1}.) {item}")
        print(f"{len(recipe) + 1}.) Mix all those together.")
        print("\nAnd now you have a tasty meal!")


yes = Recipe("Questionable Resippy", 100)
yes.format_recipe()


