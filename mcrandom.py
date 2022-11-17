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
def order_gen(params):
    
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
        
    # Consider parameters
    size = "large"
    if "small" in params:
        size = "small" 
    elif "medium" in params:
        size = "medium" 
        
    # Generate name
    order_str = ""
    
    if "breakfast" in params: # Check and roll for breakfast
        order_str += list_breakfasts[randint(0, len(list_breakfasts)-1)].strip('\n') + " meal, " + size + ", w/ a coffee. "
    else:
        if randint(1, 101) == 100: # Roll for Happy Meal entree, 1% chance
            order_str += "Happy Meal w/ a "
        elif (randint(0, 100) < 10) and ("mcrib" in params): # Check and roll for McRib, 10% chance
            order_str += "McRib meal, " + size + ", w/ fries and a "
        else: # Roll for entree
            order_str += list_entrees[randint(0, len(list_entrees)-1)].strip('\n') + " meal, " + size + ", w/ fries and a "
        # Roll for drink
        order_str += list_drinks[randint(0, len(list_drinks)-1)].strip('\n') + ". "
    
    if "dessert" in params: # Check and roll for dessert
        order_str += "For dessert, an order of " + list_desserts[randint(0, len(list_desserts)-1)].strip('\n') + ". "
    
    return order_str
        
    file.close()

# Run the prompt and results
while g.lower() != "exit":

    # Get the genre
    print("\nEnter anything (or a command) to generate an order. Enter \'exit\' to quit. ")
    g = input("> ")
    
    # Get commands for passing as parameters
    params = []
    if "breakfast" in g.lower(): params.append("breakfast")
    if "dessert" in g.lower(): params.append("dessert")
    if "small" in g.lower(): params.append("small")
    if "medium" in g.lower(): params.append("medium")
    if "large" in g.lower(): params.append("large")
    if "mcrib" in g.lower(): params.append("mcrib")

    # Generate the name
    order = order_gen(params)

    # Print the results
    if g.lower() == "exit":
        print("\nThank you for using McRandom. Goodbye! ")
        exit()
    else:
        print("\nYour McRandom order: ")
        print(order)