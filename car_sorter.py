import json #For saving JSON data on each car
from pathlib import Path #For saving to folders
from datetime import date #For getting current date

#Comparing current year with model year to get age
def years_since (year_in):
    now = date.today()
    now_year = now.year
    age = int(now_year)-int(year_in)
    return age

#Function to save dictionary to JSON
def save__to_json(dictionary_in, file_path):
    with open(file_path, "w") as json_file:
        json.dump(dictionary_in, json_file, indent=4)
    return file_path

#Opening the file that shows all saved cars - makes it into a list
def open_saved_cars():
    file_path = "SavedCars.txt"
    with open(file_path, 'r') as file:
        saved_cars = [line.rstrip('\n') for line in file]
        return saved_cars

#Taking the saved cars list and putting it back into the text file
def pack_up_saved_cars(saved_cars):
    file_path = "SavedCars.txt"
    with open(file_path, 'w') as file:
        for item in saved_cars:
            file.write(str(item) + '\n')

#Adding a car to the saved cars list and file
def add_to_saved_cars(car_to_add):
    saved_cars = open_saved_cars() #Opening list
    if str(car_to_add) not in saved_cars:
        saved_cars.append(str(car_to_add))
    pack_up_saved_cars(saved_cars) #Closing list

#Saving a car JSON file into the cars folder - using the save to JSON function
def save_car_to_json(dictionary_in, file_name):
    folder = Path("cars")
    file_name = (str(file_name)+".json")
    file_path = folder/file_name
    folder.mkdir(parents=True, exist_ok=True)
    file_path = save__to_json(dictionary_in, file_path)
    return file_path 

#Getting and formatting a text input
def input_then_cap(question):
    answer = input(str(question))
    answer = answer.capitalize()
    return (answer)

#Getting data for a new car
def new_car_input():
    car_make = input_then_cap("What is the make of the car? ")
    car_model = input_then_cap("What is the model of the car? ")
    car_year = int(input_then_cap("What is the year of the car? "))
    is_car_fav = True
    car_rating = int(input_then_cap("Give your rating of the car 1-5 "))
    car_note = "my car"
    car_name = str(car_year)+car_make+car_model
    car_dict = dict(name = car_name, make = car_make, model = car_model, year = car_year, favorite = is_car_fav, rating = car_rating, notes = car_note)
    return car_dict

#Getting car data and storing it's files
def new_car():
    car = new_car_input()
    add_to_saved_cars(car['name'])
    save_car_to_json(car, car['name'])

#MAIN
new_car()