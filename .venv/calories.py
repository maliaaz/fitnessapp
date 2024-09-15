# Import requests module
import requests


def Calories():
    # Initialize variables
    global destination
    global command
    destination = []
    command = ""

    # Allow user to input query to search recipes
    def search():
        searching = True
        search_results = {}
        while searching == True:
            query = input("Search: ")
            response = requests.get(
                f"https://api.spoonacular.com/recipes/complexSearch?apiKey=YOUR-API-KEYnumber=10&addRecipeNutrition=True&query={query}")
            search_results = response.json()
            if search_results['totalResults'] == 0:
                print(f"No recipes found.")
            else:
                searching = False
        return search_results

    # Print search results
    def print_search(search_results):
        for recipe_index in range(len(search_results["results"])):
            print(f"[{recipe_index}] - " + search_results["results"][recipe_index]["title"])

    # Allow user to choose between commands
    def commands(search_results):
        while True:
            print(f"--- [A] Add recipe [B] Delete recipe [C] Search other recipes [D] Complete List ---")
            command = input("> ").upper()
            if command == "A":
                add_item(search_results)
            elif command == "B":
                delete_item()
            elif command == "C":
                search_results = search()
                print_search(search_results)
            elif command == "D":
                break
            else:
                print(f"Invalid input.")

    def print_list():  # Print a list of selected recipes and calculates calorie amount. This will be empty at first.
        total_calories = []
        recipe_list = "" # String variable for final return statement
        for recipe in range(len(destination)):
            print(f"[{recipe}] - {destination[recipe]["recipe"]} - {destination[recipe]["calories"]} kcal")
            total_calories.append(destination[recipe]["calories"])
            recipe_list += f"[{recipe}] - {destination[recipe]["recipe"]} - {destination[recipe]["calories"]} kcal"
        recipe_list += f"Total calories: {sum(total_calories)} kcal"
        return recipe_list

    # Allow user to add an item
    def add_item(search_results):
        new_dict = {}
        getting_response = True
        while getting_response == True:
            while True:
                try:
                    recipe_num = int(input("Add recipe number: "))
                    break
                except ValueError:
                    print("Please insert a number.")
            for recipe_index in range(len(search_results["results"])):  # Iterates through search results
                if recipe_num == recipe_index:
                    new_dict = {
                        "recipe": search_results["results"][recipe_index]["title"],
                        "calories": search_results["results"][recipe_index]["nutrition"]["nutrients"][0]["amount"],
                    }
                    destination.append(new_dict)
                    print(f"'{search_results["results"][recipe_index]["title"]}' has been added.")
                    print_list()
                    getting_response = False
            if new_dict == {}:  # Prints error if user inputs number outside index
                print(f"Invalid input.")

    # Allow user to delete an item
    def delete_item():
        getting_response = True
        while getting_response == True:
            while True:
                try:
                    recipe_num = int(input("Delete recipe number: "))
                    break
                except ValueError:
                    print("Please insert a number.")
            for recipe_index in range(len(destination)):  # Iterates through added recipes
                if recipe_num == recipe_index:
                    destination.pop(recipe_index)
                    print("'{destination[recipe_index]}' has been deleted.")
                    print_list()
                    getting_response = False

    # Populate search results dict with json
    search_results_dict = search()
    # Print relevant info
    print_search(search_results_dict)
    # While loop for editing personal list
    commands(search_results_dict)
    # When "D" is pressed in commands, the loop breaks and prints list with the line below and returns the string to
    # webapp.py.
    return print_list()