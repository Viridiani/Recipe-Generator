# Ingredients to include in the recipe
# Add specific ingredients option
import random
from constants import *
from cookers import appliances as ap


class Recipe:  # This is code that generates the actual recipe portion of the app.
    def __init__(self, name, items):
        self.name = name
        self.ingredients = self.make_ingredients(items)

    def make_item(self):
        self.new_item = {
                    'Amount': random.randint(1, 20),
                    'Measurement': measurements[random.randint(0, len(measurements)-1)],
                    'Ingredient': ingredients[random.randint(0, len(ingredients)-1)]}
        return self.new_item

    def make_ingredients(self, times):
        ing = []
        while times > 0:
            ing.append(self.make_item())
            times -= 1
        return ing

    def describe_ingredients(self):
        full_ing = []
        for ing in self.ingredients:
            temp = []
            for key, value in ing.items():
                temp.append(value)
            if temp[0] > 1:
                full_ing.append(f"*{temp[0]} {temp[1]}s of {temp[2]}\n")
            else:
                full_ing.append(f"*{temp[0]} {temp[1]} of {temp[2]}\n")
        return full_ing

    # @staticmethod ... testing
    def cook(self, ingredient):
        self.adj = cooking[random.randint(0, len(cooking)-1)]
        self.cook_time = time[random.randint(0, len(time)-1)]
        self.appliance = ap[random.randint(0, len(ap)-1)]
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

        line = f"{self.adj.title()} {use} {ingredient['Measurement']}s {ingredient['Ingredient']} with a {self.appliance.lower()} for {rand_time} {self.cook_time}s at {temp} degrees Fahrenheit."
        return line

    # @staticmethod ... testing
    def prepare(self, ing1, ing2):
        self.prep = preparing[random.randint(0, len(preparing)-1)]
        self.utensil = utensils[random.randint(0, len(utensils)-1)]

        if (ing1['Amount'] != 0) and (ing2['Amount'] != 0):
            use = random.randint(1, ing1['Amount'])
            use2 = random.randint(1, ing2['Amount'])
        else:
            return None

        if (ing1['Amount'] - use) < 0:
            use = abs(ing1['Amount'] - use)
            ing1['Amount'] = 0
        elif (ing1['Amount'] - use) == 0:
            ing1['Amount'] = 0
        else:
            ing1['Amount'] -= use

        if (ing2['Amount'] - use2) < 0:
            use2 = abs(ing2['Amount'] - use2)
            ing2['Amount'] = 0
        elif (ing2['Amount'] - use2) == 0:
            ing2['Amount'] = 0
        else:
            ing2['Amount'] -= use2

        line = f"{self.prep.title()} {use} {ing1['Measurement']}s {ing1['Ingredient']} and {use2} {ing2['Measurement']}s {ing2['Ingredient']} together with a {self.utensil}."
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

    @staticmethod
    def fix_recipe(recipe):
        while None in recipe:
            recipe.remove(None)
        return recipe

    def gen_recipe(self):
        instructions = []
        while len(self.ingredients) > 0:
            for item in self.ingredients:
                if item['Amount'] <= 0:
                    self.ingredients.remove(item)
            instructions.append(self.instruct())
        self.fix_recipe(instructions)
        return instructions

    def format_recipe(self):
        ending = ''
        title = f"{self.name} \n\n"
        li_ing = self.describe_ingredients()
        line = "\n"
        recipe = self.gen_recipe()
        final_step = f"{len(recipe) + 1}.) Mix all those together."
        final_statement = "\n\nAnd now you have a tasty meal!"
        
        ending += title
        
        for item in li_ing:
            ending += item
        
        ending += line
        
        for item in recipe:
            index = recipe.index(item)
            ending += f"{index + 1}.) {item}\n"
        
        ending += final_step
        ending += final_statement

        return ending

resippy = Recipe('test', 10)
print(resippy.format_recipe())