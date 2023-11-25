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
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food.get('cuisine', 'Unknown') 
        heat_level = food['heat_level']
        emoji = '🌶' * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {emoji}.")

def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food['cuisine'] == target_cuisine:
            return food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food.get('cuisine', 'Unknown')  
        heat_level = food['heat_level']
        emoji = '🌶' * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {emoji}.")

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero

    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat // len(spicy_foods)

    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)