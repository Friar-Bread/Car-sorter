#Basic functions to make data input and output easier
#function to print a list over multiple lines
def print_list(list_to_print):
    for i in list_to_print:
        print(i)

#Getting and formatting a text input
def input_then_cap(question):
    answer = input(str(question))
    answer = answer.capitalize()
    return (answer)

#Getting and formatting a text input for integer
def input_then_int(question):
    good = False
    follower = " Please pick a valid number"
    while not good:
        answer = input_then_cap(str(question)+follower)
        if answer.isdigit():    
            good = True
    answer = int(answer)
    return answer

#Getting and formatting a text input for bool
def input_then_bool(question):
    follower = " Y or yes for True, anything else False"
    answer = input(str(question)+follower)
    answer = answer.lower
    answer = answer[0]
    if answer == "y":
        return True
    else:
        return False
