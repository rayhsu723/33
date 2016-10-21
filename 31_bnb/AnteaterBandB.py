def BandB():
    """Main program
    """
    print("Welcome to the Anteater Bed and Breakfast program!")
    our_rooms = Collection_new()
    our_rooms = handle_commands(our_rooms)
    print("\nThank you. Good-bye.")

MENU = """
Anteater Bed and Breakfast Collection Program --- Choose one:
    AB 'int' : Add a new bedroom with specified room number
    BL       : Print a list of bedrooms currently available
    PL 'text': Print stuff
    q        : Quit
"""  

def handle_commands(C: list) ->list:
    while True:
        response = input(MENU)
        response1 = response.replace(" ","")
        response1 = response1.lower()
        if 'ab' in response1:
            room_number = response1[2:]
            C = Collection_add_room(C, room_number)
        elif 'bl' in response1:
            print("Here is a list of available bedrooms")
            Collection_display(C)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")


def Collection_new() ->list:
    """ Return a new, empty collection
    """
    return []

def Collection_add_room(C:list, r:str):
    C.append(r)
    return C

def Collection_display(C:list)->str:
    print("Number of bedrooms in service: ", len(C))
    print("\n-----------------------------------\n")
    for r in C:
        print(r)
    print("\nThank you for using the Anteater BandB Reservation System!")

BandB()

    

