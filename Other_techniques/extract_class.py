# by Kami Bigdely
# Extract Class
from pprint import pprint

class Food:
    def __init__(self, name, preptime, vegetarian, category, cuisine, ingredients, instructions):
        self.name = name
        self.preptime = preptime
        self.vege = vegetarian
        self.foodtype = category
        self.origin = cuisine
        self.ingredients = ingredients
        self.instructions = instructions
        

foods = []
butternut_squash_soup = Food(
    'butternut squash soup',
    45, 
    True, 
    'soup',
    'North African',
    ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk'],
    '1. Grill the butter squash, onion, carrot and garlic in the oven until'
        'they get soft and golden on top 2. Put all in blender with'
        'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
            '. Add coconut milk. Simmer for 5 mintues.')
foods.append(butternut_squash_soup)

shirazi_salad = Food(
    'shirazi salad',
    5,
    True, 
    'salad',
    'Iranian',
    ['cucumber', 'tomato', 'onion', 'lemon juice'],
    '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
        '4. Mixed them thoroughly')
foods.append(shirazi_salad)

homemade_beef_sausage = Food(
    'Home-made Beef Sausage', 
    60, 
    False, 
    'deli',
    'All',
    ['sausage casing', 'regular ground beef','garlic',\
        'corriander seeds','black pepper seeds','fennel seed','paprika'],
    '1. In a blender,'
    ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
    'the seasonings 2. In a bowl, mix ground beef with the'
    'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
    "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!")
foods.append(homemade_beef_sausage)

for food in foods:
    print("Name:", food.name)
    print("Prep time:", food.preptime, "mins")
    print("Is Veggie?", 'Yes' if food.vege else "No")
    print("Food Type:", food.foodtype)
    print("Cuisine:", food.origin)
    for item in food.ingredients:
        print(item, end=', ')
    print()
    print("recipe", food.instructions)
    print("***")
