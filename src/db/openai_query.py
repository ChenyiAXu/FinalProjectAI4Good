import os
import openai
from openai import OpenAI

def generate_category_and_tags(item):
    openai_api_key = "sk-proj-F5OmMn8npmC2KwavsgV7T3BlbkFJCZTxwrM6LRHgXJF4H51H"
    client = OpenAI(api_key=openai_api_key)
    
    # Define the messages for the two tasks
    category_message = {
        "role": "user",
        "content": f"""As a NLP computational expert, identify the category of {item} based on grocerycategorylist mentioned in the list below. you should give me a string of the category name from grocerycategorylist that matches the item grocerycategorylist=['Fruit', 'Vegetables', 'Bread', 'Butter_Spreads', 'Cheese', 'Egg_and_Substitutes', 'Milk_Cream', 'Milk_Substitutes', 'Yogurt', 'FrozenFruit', 'FrozenVegetables', 'FrozenMeat', 'Bacon', 'Beef_Veal', 'Chicken_Turkey', 'Fish', 'Hotdogs_Sausages', 'Lamb', 'Pork_Ham', 'Meat_Alternatives', 'Shrimp_ShellFish', 'Oils_Vinegars', 'Juice', 'Coffee', 'Tea', 'Herbs_Spices_Sesaonings', 'CannedFood', 'Rice', 'Pasta_Sauce', 'BakingEssentials', 'vegetable', 'fruit', 'sausage', 'lamb_veal','kebabs_marinatedMeat', 'beef', 'chicken_turkey', 'pork_ham', 'bacon', 'hotdogs', 'HalalMeat', 'plantBasedMeat', 'fish', 'salmon', 'shrimp', 'bread', 'coffee', 'tea_hotDrinks', 'cheese', 'yogurt', 'butter_spreads', 'egg_and_substitutes', 'milk_cream', 'bakingEssentials', 'pasta_sauce', 'rice', 'oils_vinegar', 'spices_seasoning', 'cannedFood', 'juice', 'nonDairy_milk_alternatives', 'FrozenMeat_Seafood', 'butter and spreads', 'milk and cream'] THE OUTPUT SHOULD BE ONE STRING WITHOUT ANY DESCRIPTION"""
    }

    tags_message = {
        "role": "user",
        "content": f"""As a NLP computational expert, generate some tags to describe ethnic cuisine, general descriptors, specific descriptors, packaging/type or dietary/quality of the item below. If the item has specific characteristics, like being organic, halal, dietary, vegan, vegetarian, or anything else, please include them in the tag. Also, add tags to account for user errors and other variables that could be useful when a user is searching for the item. Only generate the top 5 most relevant general tags. Item: {item} Give me a string with all the tags included. Do not include string 'user error' in the tag string! Just include the user errors as a regular tag! Example: item:'Strawberry Watermelon Cream Pop Greek Yogurt'. Output: 'diary,yogurt,greek yogurt,creamy,fruit yogurt'. The only thing you should be returning are the tags"."""
    }

    # Get the category
    chat_completion_category = client.chat.completions.create(
        messages=[category_message],
        model="gpt-4o-2024-05-13",
    )
    Category = chat_completion_category.choices[0].message.content.strip()

    # Get the tags
    chat_completion_tags = client.chat.completions.create(
        messages=[tags_message],
        model="gpt-4o-2024-05-13",
    )
    Tags = chat_completion_tags.choices[0].message.content.strip()

    print(Category)
    print(Tags)
    return Category, Tags

# Example usage:
category, tags = generate_category_and_tags("banana")
