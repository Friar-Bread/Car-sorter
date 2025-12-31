from car_sorter import new_car, get_saved_cars, user_inspect_car, edit_car
from basic_data_handling import print_list, input_then_cap

#MAIN LOOP
while True:
    print(
        "\n"
        "Hello\n"
        "Enter N to add a car\n"
        "Enter V to view all cars added\n"
        "Enter I to look at a car\n"
        "Enter E to edit a car's file\n"
        "Enter S to search the saved cars\n"
    )
    plan = input_then_cap("What would you like to do? ")
    print ("\n")

    if plan == "N":
        new_car()
    elif plan == "V":
        print_list(get_saved_cars())
    elif plan == "I": 
        user_inspect_car()
    elif plan == "E":
        edit_car()
    elif plan == "S":
        pass