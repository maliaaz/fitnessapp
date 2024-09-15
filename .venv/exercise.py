# Import requests and random modules
import requests
import random

def Exercises():
    global level
    global equipment
    global category
    global filtered_data
    
    # Retrieve data from api
    response = requests.get("https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json")
    data = response.json()

    # Function for getting a filtered list according to parameters
    def get_exercise_list(level, equipment, category):
        filtered_data = [item for item in data if item["level"] == level and item["equipment"] == equipment and item["category"] == category]
        return filtered_data

    # Function for calling a number of random exercises
    def get_output():
        while True:
            # User inputs level, equipment, category and number of exercises
            level = input("Level: ")
            equipment = input("Equipment: ")
            category = input("Category: ")
            while True:
                try:
                    num_of_exercises = int(input("Number of Exercises: "))
                    break
                except ValueError:
                    print("Please insert a number.")
            filtered_data = get_exercise_list(level, equipment, category)  # Get exercise list according to user input 
            if len(filtered_data) == 0: # Returns an error
                print("No exercises match your parameters. Try a different search.")
            else:
                if num_of_exercises > len(filtered_data):
                    print(f"There are only {len(filtered_data)} exercises with these parameters.")
                    output = filtered_data
                    break
                else:
                    output = random.sample(filtered_data, num_of_exercises)
                    break
        return output


    return get_output()