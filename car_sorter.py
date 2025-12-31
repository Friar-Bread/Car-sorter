import json #For saving JSON data on each car
from pathlib import Path #For saving to folders
from datetime import date #For getting current date

#function to print a list over multiple lines
def print_list(list_to_print):
    for i in list_to_print:
        print(i)

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

#Function to open a directory
def turn_to_direct(directory_name,file_name):
    folder = Path(directory_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_name = (str(file_name)+".json")
    file_path = folder/file_name
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

#Getting the saved cars list
def get_saved_cars():
    saved_cars = open_saved_cars()
    pack_up_saved_cars(saved_cars)
    return saved_cars

#Adding a car to the saved cars list and file
def add_to_saved_cars(car_to_add):
    saved_cars = open_saved_cars() #Opening list
    if str(car_to_add) not in saved_cars:
        saved_cars.append(str(car_to_add))
    pack_up_saved_cars(saved_cars) #Closing list

#Saving a car JSON file into the cars folder - using the save to JSON function
def save_car_to_json(dictionary_in, file_name):
    file_path = turn_to_direct("cars",file_name)
    file_path = save__to_json(dictionary_in, file_path)
    return file_path 

#Getting and formatting a text input
def input_then_cap(question):
    answer = input(str(question))
    answer = answer.capitalize()
    return (answer)

#Check if a car is saved and return its proper name
def check_if_car(car):
    inspect_car_lower = car.lower()
    cars = get_saved_cars()
    car_to_inspect = ""
    for car in cars:
        car_lower = car.lower()
        if inspect_car_lower == car_lower:
            car_to_inspect = car
    return car_to_inspect

def get_car_name_input(message):
    user_in = input(str(message))
    car_name = check_if_car(user_in)
    return car_name

data_needing_str = ["make","model","note"]
data_needing_int = ["year","rating"]
data_needing_bool = ["favorite"]
data_questions = dict(make = "What is the make of the car? ",
                      model = "What is the model of the car? ",
                      year = "What is the year of the car? ",
                      rating = "Give your rating of the car 1-5 "
                      )
#Getting data for a new car
def new_car_input():
    car_make = input_then_cap(data_questions["make"])
    car_model = input_then_cap(data_questions["model"])
    car_year = int(input_then_cap(data_questions["year"]))
    is_car_fav = False
    car_rating = int(input_then_cap(data_questions["rating"]))
    car_note = "No note yet..."
    car_name = str(car_year)+car_make+car_model
    car_dict = dict(name = car_name, make = car_make, model = car_model, year = car_year, favorite = is_car_fav, rating = car_rating, note = car_note)
    return car_dict

#Getting car data and storing it's files
def new_car():
    car = new_car_input()
    add_to_saved_cars(car['name'])
    save_car_to_json(car, car['name'])

#Function to inspect the data about a car
def inspect_car(car_to_inspect):
    if car_to_inspect:
        file_path = turn_to_direct("cars",car_to_inspect)
        with open(file_path, 'r') as file:
            car_dict = json.load(file)
        for i in car_dict:
            print(i,": ",car_dict[i])

#Function for user to inspect car data
def user_inspect_car():
    print("\n")
    car_to_inspect = get_car_name_input("What is the name of the car you want to look at? ")
    inspect_car(car_to_inspect)

#Function to make a dictionary of all of the car dictionaries
def make_dictionary_of_cars():
    cars_list = get_saved_cars()
    cars_dict = dict()
    for car_name in cars_list:
        file_path = turn_to_direct("cars",car_name)
        with open(file_path, 'r') as file:
            car_dict = json.load(file)
        cars_dict[car_name] = car_dict
    return cars_dict

#Edit a piece of data for a car
def edit_car_data_point(car_name, data, new_data):
    cars_dict = make_dictionary_of_cars()
    print(cars_dict)
    print(car_name)
    car_dict = cars_dict[str(car_name)]
    car_dict[data] = new_data
    return car_dict

#User edits a piece of data for a car
def user_edit_car_data_point(car_name, data):
    new_data = ""
    question = data_questions[data]
    if data in data_needing_str:
        new_data = input_then_cap(question)
    elif data in data_needing_int:
        new_data = int(input_then_cap(question))
    elif data in data_needing_bool:
        new_data = True
    if new_data:
        car = edit_car_data_point(car_name,data, new_data)
        add_to_saved_cars(car['name'])
        save_car_to_json(car, car['name'])

def edit_car():
    print("")
    car_name = get_car_name_input("What is the name of the car you want to edit? ")
    print("")
    inspect_car(car_name)
    print("")
    print(
        "1 - Make\n"
        "2 - Model\n"
        "3 - Year\n"
        "4 - Rating"
    )
    data_input = input("What piece of data do you want to edit? ")
    things_possible_to_edit = ['make','model','year','rating']
    chosen_data = things_possible_to_edit[int(data_input)-1]
    user_edit_car_data_point(car_name, chosen_data)