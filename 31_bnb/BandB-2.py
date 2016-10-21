#Anthony SuVasquez 39573991. ICS 31 Lab 3. Assignment 9 BandB

from collections import namedtuple

'''STAGE I'''

Bedroom = namedtuple("Bedroom", "number reservations") #because OOP, and because we don't actually know how to declare classes and use actual objects in python yet
#The reason why I want to use a namedTuple rather than a list of int, is because I don't know what other attributes bedrooms are going to have in later parts of the lab.
#This makes it easier for me to update the code as we proceed with the Bed and Breakfast lab, since I would only need to modify the call ot the constructor of Bedroom in addBedroom()
#and the declaration of the attributes stored within the namedtuple.
#I'm essentially treating Bedroom as a struct, sans public/private scoping for the different attributes.


bedrooms = {} #I'm using a dictionary here because these are much faster for this application than just using lists.
#I'm treating it kind of like a hash table or associative list.

def readFile(filePath: str):
    '''This reads the file at filePath and parses each line for commands.'''
    '''This is the main function of BandB part one, so to speak'''
    
    file = open(filePath, 'r')
    lines = file.readlines()

    confirmation = 1
    
    for line in lines: #For each line in the text file...
        line = line.strip()

        if(line == ""): continue
        
        #parse the command token from the current line
        command = line.split()[0]
        command = command.upper()

        #Then parse the command's parameter as the rest of the line, and remove leading/trailing whitespace.
        parameter = line[len(command) + 1 : len(line)]
        parameter = parameter.strip()

        #Now process the command with the parameter
        #A switch statement here is also appropriate
        if(command == "**"): #Comment
            continue #ignore the rest of the line

        elif(command == "AB"): #Add Bedroom
            if(not addBedroom(bedrooms, parameter)):
                print("Sorry, can't add room "+parameter+" again; it's already on the list.")

        elif(command == "BL"): #Bedroom List
            printBedrooms(bedrooms)

        elif(command == "PL"): #Echo
            print(parameter)

        elif(command == "BD"): #Delete Bedroom
            if(not deleteBedroom(bedrooms, parameter)):
                print("Sorry, can't delete room " + parameter + "; it is not in service now")
            else:
                deleteList = []
                for reservation in reservations.values():
                    if(reservation.roomNumber == parameter):
                        print("Deleting room " + parameter + " forces cancellation of this reservation:")
                        string = reservation.guestName
                        string += " arriving " + dateToString(reservation.startDate)
                        string += " and departing " + dateToString(reservation.endDate)
                        string += " (Conf. #" + reservation.number + ")"
                        print("\t" + string)

                        deleteList.append(reservation.number)

                for number in deleteList:
                    deleteReservation(reservations, number)
                        

        elif(command == "NR"): #New Reservation
            params = parameter.split()

            roomNumber = params[0]
            
            startData = params[1].split("/")
            endData = params[2].split("/")
            startDate = datetime.date(int(startData[2]), int(startData[0]), int(startData[1]))
            endDate = datetime.date(int(endData[2]), int(endData[0]), int(endData[1]))

            guestName = params[3]

            for i in range(len(params)):
                if(i <= 3): continue
                guestName += " " + params[i]

            result = addReservation(reservations, bedrooms, confirmation, roomNumber, startDate, endDate, guestName)
            
            if(int(result) == 0):
                print("Reserving room " + roomNumber + " for " + guestName + " -- Confirmation #" + str(confirmation))
                print("\t(arriving " + params[1] + ", departing " + params[2] + ")")

                confirmation += 1
                
            elif(int(result) == -1):
                print("Sorry; can't reserve room " + roomNumber + "; room not in service")
            elif(int(result) == -2):
                print("Sorry, can't reserve room " + roomNumber + " (" + params[1] + " to " + params[2] + ");")
                #The reason why this doesn't use dateToString() here is because the example output shows an unformatted date for this part.
                #Why the hell is the example so inconsistent?
                print("\tcan't leave before you arrive.")
            elif(int(result) == -3):
                print("Sorry, can't reserve room " + roomNumber + " (" + params[1] + " to " + params[2] + ");")
                #The reason why this doesn't use dateToString() here is because the example output shows an unformatted date for this part.
                #Why the hell is the example so inconsistent?
                print("\tcan't arrive and leave on the same day.")
            elif(int(result) > 0):
                print("Sorry, can't reserve room " + roomNumber + " (" + dateToString(startDate) + " to " + dateToString(endDate) + ");")
                #The example output shows formatting for this part, so dateToString() is used...
                print("\tit's already booked. (Conf. #" + result + ")")
            
        elif(command == "RL"): #Reservations List
            reservationsList(reservations, confirmation)
            
        elif(command == "RD"): #Delete Reservation
            if(not deleteReservation(reservations, parameter)):
                print("Sorry, can't cancel reservation; no confirmation number "+parameter)

        elif(command == "RB"): #Reservations by bedroom
            reservationsByBedroom(parameter)

        elif(command == "RC"): #Reservations by guest
            reservationsByGuest(parameter)

        elif(command == "LA"): #List of all arrivals on specified date
            startData = parameter.split("/")
            startDate = datetime.date(int(startData[2]), int(startData[0]), int(startData[1]))
            listOfArrivals(startDate)

        elif(command == "LD"): #List of all departures on specified date
            endData = parameter.split("/")
            endDate = datetime.date(int(endData[2]), int(endData[0]), int(endData[1]))
            listOfArrivals(endDate)

        elif(command == "LF"): #List of all free bedrooms with the given start date and end date
            params = parameter.split()
            
            startData = params[0].split("/")
            startDate = datetime.date(int(startData[2]), int(startData[0]), int(startData[1]))
            
            endData = params[1].split("/")
            endDate = datetime.date(int(endData[2]), int(endData[0]), int(endData[1]))

            listOfFreeBedrooms(startDate, endDate)


        elif(command == "LO"): #List of all occupied bedrooms with the given start date and end date
            params = parameter.split()
            
            startData = params[0].split("/")
            startDate = datetime.date(int(startData[2]), int(startData[0]), int(startData[1]))
            
            endData = params[1].split("/")
            endDate = datetime.date(int(endData[2]), int(endData[0]), int(endData[1]))

            listOfOccupiedBedrooms(startDate, endDate)

def printBedrooms(bedroomDict: dict):
    '''This takes a dict of bedrooms as the input and prints it out'''
    print("Number of bedrooms in service:\t", len(bedroomDict))

    #sorting keys so that we print in order...
    keys = list(bedroomDict.keys()) #This is considered a big nono in Python because it can apparently cause concurrent modification errors.
    #However, I think it's okay here because I believe this lab is single-threaded and shouldn't cause any problems
    keys.sort()
    
    for bedroom in keys:
        print(bedroom)
        

def addBedroom(bedroomDict: dict, roomNumber: str) -> bool:
    '''This creates a new Bedroom "object" and adds it to the bedroomDict'''
    if(int(roomNumber) < 0 or int(roomNumber) > 999): #check if the roomNumber is invalid...
        return #If it is then don't do anything to the bedroomList...

    if(roomNumber in bedroomDict.keys()): return False #This bedroom already exists!
    
    newRoom = Bedroom(roomNumber, [])
    bedroomDict[roomNumber] = newRoom

    return True

'''STAGE II'''

def deleteBedroom(bedroomDict: dict, roomNumber: str) -> bool:
    '''This looks for a bedroom in bedroomDict that matches roomNumber, and removes it from the dict, and returns true.
       If no bedroom was found, then the function returns false.
    '''
       
    if(roomNumber in bedroomDict.keys()):
        del bedroomDict[roomNumber]
        return True
    else:
        #I don't think that there should be any console output for adding or removing bedrooms from the bedroom list.
        #Therefore, deleteBedroom() returns a boolean on whether or not it was successful in locating and deleting a bedroom.
        #This lets the function that called deleteBedroom() then alter its behavior on whether or not the deletion was successful.
        return False

'''STAGE III AND STAGE IV'''
import datetime


Reservation = namedtuple("Reservation", "number roomNumber startDate endDate guestName")

reservations = {}#I'm using a dictionary here because these are much faster for this application than just using lists.
#I'm treating it kind of like a hash table or associative list.

def addReservation(reservationDict: dict, bedroomDict:dict, confirmation: int, roomNumber: str, startDate:datetime.date, endDate: datetime.date, guestName: str) -> int:
    ''' This will attempt to add a reservation with the given parameters.
        Returns an int depending on whether or not adding was successful.
        Return values:
        0 - Successfully added reservation. Returned value is the confirmation number
        -1 - Bedroom does not exist
        -2 - End date is not after the start date
        -3 - End date is on the start date
        any positive number - Another reservation for this room conflicts with the given start and end dates.
            Return value is the confirmation number of the other reservation
    '''

    #Check here if there are any conflicts with the given parameters for this reservation
    if(not roomNumber in bedroomDict.keys()):
        #The bedroom doesn't exist.
        return -1
    
    bedroom = bedroomDict[roomNumber]

    #Check if the end date is before the start date
    if(endDate < startDate):
        return -2
    
    #Check if the end date is the start date
    if(endDate == startDate):
        return -3

    #Check reservation conflicts...
    for key in bedroom.reservations:
        if(key in reservationDict.keys()):
            otherReservation = reservationDict[key]
            #now check the date ranges for all other reservations for this bedroom to make sure that there are no conflicts...
            
            if(otherReservation.startDate < endDate and otherReservation.endDate > endDate): return otherReservation.number
            if(otherReservation.startDate <= startDate and otherReservation.endDate >= endDate): return otherReservation.number
            
        else:
            bedroom.reservations.remove(key)
    
    #Otherwise, create the reservation and add it to the reservations list...

    confirmation = str(confirmation)

    newReservation = Reservation(confirmation, roomNumber, startDate, endDate, guestName)
    bedroom.reservations.append(confirmation)

    #Here, add the new reservation's reservationNumber to the bedroom's reservations list.
    reservationDict[confirmation] = newReservation

    return 0

def reservationsList(reservationDict:dict, confirmations:int):
    '''This prints all of the reservations that that are currently active
    '''

    numReservations = len(reservationDict.keys())
    print("Number of reservations: ", numReservations)

    #Some variables for the string formatting.
    confirmWidth = len(str(confirmations)) + 1
    if(confirmWidth < 3): confirmWidth = 3
    
    roomWidth = 3
    dateWidth = 10
    guestWidth = 5

    #First loop through everything to initialize the formatting variables
    for reservation in reservationDict.values():
        newRoomWidth = len(str(reservation.roomNumber))
        if(roomWidth < newRoomWidth): roomWidth = newRoomWidth

        newDateWidth = len(dateToString(reservation.startDate))
        if(dateWidth < newDateWidth): dateWidth = newDateWidth
        
        newDateWidth = len(dateToString(reservation.endDate))
        if(dateWidth < newDateWidth): dateWidth = newDateWidth

        newGuestWidth = len(str(reservation.guestName))
        if(guestWidth < newGuestWidth): guestWidth = newGuestWidth

    #Now print everything

    #Build and print the table header
    headerString = ""
    headerString += "{:<" + str(confirmWidth) + "} "
    headerString += "{:<" + str(roomWidth) + "} "
    headerString += "{:<" + str(dateWidth) + "} "
    headerString += "{:<" + str(dateWidth) + "} "
    headerString += "{:<" + str(guestWidth) + "} "

    headerString = headerString.format("No.","Rm.","Arrive","Depart","Guest")
    
    print(headerString)

    print("-" * (confirmWidth + roomWidth + dateWidth * 2 + guestWidth + 5))

    #sorting keys so that we print in ascending order...
    reservationList = list(reservationDict.values()) #This is considered a big nono in Python because it can apparently cause concurrent modification errors.
    #However, I think it's okay here because I believe this lab is single-threaded and shouldn't cause any problems
    reservationList.sort(key = getReservationStartDate)
    

    for reservation in reservationList:
        
        lineString = ""

        lineString += "{:>" + str(confirmWidth) + "} "
        lineString += "{:>" + str(roomWidth) + "} "
        lineString += "{:>" + str(dateWidth) + "} "
        lineString += "{:>" + str(dateWidth) + "} "
        lineString += "{:<" + str(guestWidth) + "} "

        start = dateToString(reservation.startDate)
        end = dateToString(reservation.endDate)

        lineString = lineString.format(reservation.number, reservation.roomNumber, start, end, reservation.guestName)
        print(lineString)

def deleteReservation(reservationDict: dict, confirmation:str) -> bool:
    '''This looks for a reservation in reservationDict that matches confirmation, and removes it from the dict, and returns true.
       If no reservation was found, then the function returns false.
    '''
    if(confirmation in reservationDict.keys()):
        del reservationDict[confirmation]
        return True
    
    else:
        return False
    
def dateToString(date: datetime.date)->str:
    '''This method is necessary because str(datetime.date) does not give the desired date format
    '''

    result = ""

    if(date.month < 10): result += " "
    result += str(date.month)
    result += "/"
    
    if(date.day < 10): result += " "
    result += str(date.day)
    result += "/"

    result += str(date.year)
    
    return result

def getReservationStartDate(reservation: Reservation) -> datetime.date:
    return reservation.startDate

'''STAGE V'''
def reservationsByBedroom(bedroomNumber: str):
    if(not bedroomNumber in bedrooms.keys()):
        #The bedroom was not found...
        print("Bedroom " + bedroomNumber + " does not exist...")
        return

    print("Reservations for room "+bedroomNumber)
    bedroom = bedrooms[bedroomNumber]
    for confirmation in bedroom.reservations:
        reservation = reservations[confirmation]
        line = "\t" + dateToString(reservation.startDate) + " to " + dateToString(reservation.endDate) + ":  " + reservation.guestName
        print(line)

def reservationsByGuest(guestName: str):
    print("Reservations for " + guestName + ":")
    for reservation in reservations.values():
        if(reservation.guestName == guestName):
            line = "\t" + dateToString(reservation.startDate) + " to " + dateToString(reservation.endDate) + ":  room " + reservation.roomNumber
            print(line)

def listOfArrivals(date: datetime.date):
    print("Guests arriving on "+dateToString(date) + ":")

    for reservation in reservations.values():
        if(reservation.startDate == date):
            print("\t" + reservation.guestName + " (room " + reservation.roomNumber + ")")
            
def listOfDepartures(date: datetime.date):
    print("Guests departing on "+dateToString(date) + ":")

    for reservation in reservations.values():
        if(reservation.endDate == date):
            print("\t" + reservation.guestName + " (room " + reservation.roomNumber + ")")
            
def listOfFreeBedrooms(startDate: datetime.date, endDate: datetime.date):
    print("Bedrooms free between " + dateToString(startDate) + " to " + dateToString(endDate) + ":")

    for bedroom in bedrooms.values():

        hasConflict = False
        
        for key in bedroom.reservations:
            reservation = reservations[key]
            
            if(reservation.startDate < endDate and reservation.endDate > startDate):
                hasConflict = True
                break
            
            if(reservation.startDate <= startDate and reservation.endDate >= endDate):
                hasConflict = True
                break

        if(hasConflict == False):
            print("\t" + bedroom.number)
            
def listOfOccupiedBedrooms(startDate: datetime.date, endDate: datetime.date):
    print("Bedrooms free between " + dateToString(startDate) + " to " + dateToString(endDate) +":")

    for bedroom in bedrooms.values():

        hasConflict = False
        
        for key in bedroom.reservations:
            reservation = reservations[key]
            
            if(reservation.startDate < endDate and reservation.endDate > startDate):
                hasConflict = True
                break
            
            if(reservation.startDate <= startDate and reservation.endDate >= endDate):
                hasConflict = True
                break

        if(hasConflict == True):
            print("\t" + bedroom.number)


'''STAGE VI'''
def writeFile(filePath: str):
    file = open(filePath, "w")

    file.write("** BEDROOMS **\n")

    for bedroom in bedrooms.values():
        file.write("AB "+bedroom.number + "\n")

    file.write("** RESERVATIONS **\n")

    for reservation in reservations.values():
        file.write("NR " + reservation.roomNumber + " " + dateToString(reservation.startDate) + " " + dateToString(reservation.endDate) + " " + reservation.guestName + "\n")

    file.write("** END OF FILE **")


readFile('bandb.txt')
writeFile(input("Input the filename to save the end-of-day data: "))


