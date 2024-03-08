spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for food in spicy_foods:
        food_names.append(food['name'])
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        spiciest_foods.append(food) if food['heat_level'] > 5 else None
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {(food['heat_level']) * '🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {(food['heat_level']) * '🌶'}") 

def get_average_heat_level(spicy_foods):
    spice_levels = []

    for food in spicy_foods:
        spice_levels.append(food['heat_level'])

    return sum(spice_levels) / len(spice_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
   
    






create_spicy_food(spicy_foods, {
    'name':'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10
})