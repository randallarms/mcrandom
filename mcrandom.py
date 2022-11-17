from random import randint
import os

# Opening text
print("\n\n=========")
print("McRandom")
print("=========")
print("Generate a meal!")

# Input variable
g = "9.81 m/s^2"

# Name generation function
def order_gen():
    
    # Get files
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    entrees = open(os.path.join(__location__, "menu/entrees.txt"), "r")
    drinks = open(os.path.join(__location__, "menu/drinks.txt"), "r")
    desserts = open(os.path.join(__location__, "menu/desserts.txt"), "r")
    breakfasts = open(os.path.join(__location__, "menu/breakfasts.txt"), "r")
    
    # Fill list of possible names from file
    list_entrees = []
    list_drinks = []
    list_desserts = []
    list_breakfasts = []
    for line_entree in entrees:
        list_entrees.append(line_entree)
    for line_drink in drinks:
        list_drinks.append(line_drink)
    for line_dessert in desserts:
        list_desserts.append(line_dessert)
    for line_breakfast in breakfasts:
        list_breakfasts.append(line_breakfast)
        
    # Generate name
    order_str = ""
    order_str += list_entrees[randint(0, len(list_entrees)-1)].strip('\n')
    order_str += " meal, large, w/ fries and a"
    order_str += " " + list_drinks[randint(0, len(list_drinks)-1)].strip('\n')
    order_str += ". For dessert, an order of " + list_desserts[randint(0, len(list_desserts)-1)].strip('\n')
    order_str += "."
    return order_str
        
    file.close()

# Run the prompt and results
while g != "exit":

    # Get the genre
    print("\nEnter anything (or a command) to generate an order. Enter \'exit\' to quit. ")
    g = input("> ");

    # Generate the name
    order = order_gen()

    # Print the results
    if g == "exit":
        print("\nThank you for using McRandom. Goodbye! ")
        exit()
    else:
        print("\nYour McRandom order: ")
        print(order)