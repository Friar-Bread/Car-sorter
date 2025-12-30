import json
from pathlib import Path

def save_to_json(dictionary_in, file_name):
    folder = Path("cars")
    file_name = (str(file_name)+".json")
    file_path = folder/file_name
    folder.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as json_file:
        json.dump(dictionary_in, json_file, indent=4) # 'indent=4' makes the file human-readable
    return file_path

def input_then_cap(question):
    answer = input(str(question))
    answer = answer.capitalize()
    return (answer)

def new_car_input():
    car_make = input_then_cap("What is the make of the car? ")
    car_model = input_then_cap("What is the model of the car? ")
    car_year = int(input_then_cap("What is the year of the car? "))
    is_car_fav = True
    car_rating = int(input_then_cap("Give your rating of the car 1-5 "))
    car_note = "my car"
    car_dict = dict(make = car_make, model = car_model, year = car_year, favorite = is_car_fav, rating = car_rating, notes = car_note)
    return car_dict
# car format [model, make, year, rating, favorite, notes]
car = new_car_input()
save_to_json(car, str(car['year'])+car['make']+car['model'])