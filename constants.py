ingredients = []
measurements = ['drop', 'ounce', 'teaspoon', 'tablespoon', 'cup', 'pint', 'quart', 'gallon']
utensils = []
cooking = []
preparing = []
time = ['millisecond', 'second', 'minute', 'hour', 'day']

file = open('ingredients.txt').readlines()
for ingredient in file:
    ingredients.append(ingredient.rstrip())

file = open('utensils.txt').readlines()
for utensil in file:
    utensils.append(utensil.rstrip())

file = open('cooking.txt').readlines()
for item in file:
    cooking.append(item.rstrip())

file = open('preparing.txt').readlines()
for item in file:
    preparing.append(item.rstrip())
