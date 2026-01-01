import json #For saving JSON data on each car
from basic_data_handling import print_list, input_then_cap, input_then_bool, input_then_int
from txt_csv_handler import get_saved_cars, add_to_saved_cars
from json_handler import turn_to_direct, save_car_to_json, code_inspect_car

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

#Get a car's proper name using input
def get_car_name_input(message):
    user_in = input(str(message))
    user_in_nospace = user_in.replace(" ", "")
    car_name = check_if_car(user_in_nospace)
    return car_name

data_needing_str = ["make","model","note"]
data_needing_int = ["year","rating"]
data_needing_bool = ["favorite"]
data_questions = dict(make = "What is the make of the car? ",
                      model = "What is the model of the car? ",
                      year = "What is the year of the car? ",
                      rating = "Give your rating of the car 1-5 ",
                      favorite = "Is this car one of your favorites?"
                      )

#Function to ask the correct question and question type
def get_question_type(data):
    new_data = ""
    question = data_questions[data]
    if data in data_needing_str:
        new_data = input_then_cap(question)
    elif data in data_needing_int:
        new_data = input_then_int(question)
    elif data in data_needing_bool:
        new_data = input_then_bool(question)
    return new_data

#Getting data for a new car
def new_car_input():
    car_make = get_question_type("make")
    car_model = get_question_type("model")
    car_year = get_question_type("year")
    is_car_fav = get_question_type("favorite")
    car_rating = get_question_type("rating")
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
        car_dict = code_inspect_car(car_to_inspect)
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
    car_dict = cars_dict[str(car_name)]
    car_dict[data] = new_data
    return car_dict

#User edits a piece of data for a car
def user_edit_car_data_point(car_name, data):
    new_data = get_question_type(data) #Ask the user for the new data
    if new_data:
        car = edit_car_data_point(car_name,data, new_data)
        add_to_saved_cars(car['name'])
        save_car_to_json(car, car['name'])

def get_user_data_choie():
    print(
        "\n"
        "1 - Make\n"
        "2 - Model\n"
        "3 - Year\n"
        "4 - Rating"
    )
    data_input = input_then_int("What piece of data do you want to edit? ")
    things_possible_to_edit = ['make','model','year','rating']
    chosen_data = things_possible_to_edit[data_input-1]
    return chosen_data

#Edit data for a car
def edit_car():
    print("")
    car_name = get_car_name_input("What is the name of the car you want to edit? ")
    print("")
    inspect_car(car_name)
    chosen_data = get_user_data_choie()
    user_edit_car_data_point(car_name, chosen_data)

#Bulk edit cars
def bulk_edit_cars(cars):
    print(
        "1 - Edit multiple cars fully individually\n"
        "2 - Edit the same data type but fill different new values\n"
        "3 - Same data type and same new value for all\n"
    )
    choice = input_then_int("What type of bulk edit do you want? ")
    if choice == 1:
        for car in cars:
            inspect_car(car)
            chosen_data = get_user_data_choie()
            user_edit_car_data_point(car, chosen_data)
    elif choice == 2:
        chosen_data = get_user_data_choie()
        for car in cars:
            user_edit_car_data_point(car, chosen_data)
    elif choice == 2:
        chosen_data = get_user_data_choie()
        new_data = get_question_type(chosen_data)
        for car in cars:
            edit_car_data_point(car, chosen_data, new_data)

#Get a type of data for all cars
def get_type_for_cars(cars, chosen_data):
    cars_data = dict()
    for car in cars:
        car_dict = code_inspect_car(car)
        car_data = car_dict[chosen_data]
        cars_data[car] = car_data
    return cars_data

#Allow the user to search the list of saved cars
def search_cars():
    cars_dict = make_dictionary_of_cars()
    cars = get_saved_cars()
    print_list(cars)
    print(
        "1 - Make\n"
        "2 - Model\n"
        "3 - Year\n"
        "4 - Rating"
    )
    data_input = input_then_int("What would you like to sort by? ")
    things_possible_to_sort_by = ['make','model','year','rating']
    chosen_data = things_possible_to_sort_by[data_input-1]
    question = "What " + str(chosen_data) + " would you like to search for? "
    if chosen_data in data_needing_int:
        ################### adding search by range?
        data_input = input_then_int(question)
    else:
        data_input = input_then_cap(question)
    cars_data = get_type_for_cars(cars, chosen_data)
    valid_cars = []
    for car in cars:
        data = cars_data[car]
        if str(data_input) in str(data):
            valid_cars.append(car)
    print_list(valid_cars)
    ############## Refine search
    ############## Bulk edit cars

def delete_car():
    pass

def bulk_operations():
    pass