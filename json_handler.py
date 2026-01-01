import json #For saving JSON data on each car
from pathlib import Path #For saving to folders

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

#Saving a car JSON file into the cars folder - using the save to JSON function
def save_car_to_json(dictionary_in, file_name):
    file_path = turn_to_direct("cars",file_name)
    file_path = save__to_json(dictionary_in, file_path)
    return file_path 

#Code function to inspect car data
def code_inspect_car(car_to_inspect):
    file_path = turn_to_direct("cars",car_to_inspect)
    with open(file_path, 'r') as file:
        car_dict = json.load(file)
    return car_dict