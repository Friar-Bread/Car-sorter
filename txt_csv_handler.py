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