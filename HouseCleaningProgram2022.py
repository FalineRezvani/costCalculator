# This program will compute the cost of a house cleaning service and display the results
# Developer: Faline Rezvani
# Date: Oct 10, 2022

def main ():
    print("Week 3 Assignment")
    print("Faline Rezvani CMIS 102/6980")
    print("10 Oct 2022")
    
    # Greet user
    print("Welcome to Student Cleaners!")

    # Prompt user for number of rooms to define room number category
    x = int(input("Please enter the number of rooms to be cleaned.  Our limit is 12 rooms: \t"))


    # Define invalid entry
    if ((x < 1) or (x > 12)):
        print("Invalid entry.")
        x = int(input("Please enter the number of rooms to be cleaned.  Our limit is 12 rooms: \t"))
        # Define room number category price
        # Small room number
        if (0 < x < 4):
            roomPrice = 60
        # Medium room number
        elif (3 < x < 8):
            roomPrice = 100
        # Large room number
        elif (7 < x < 13):
            roomPrice = 200

    # Define room number category price
    # Small room number
    elif (0 < x < 4):
        roomPrice = 60
    # Medium room number
    elif (3 < x < 8):
        roomPrice = 100
    # Large room number
    elif (7 < x < 13):
        roomPrice = 200

    # Display line item options
    print("We do thorough floor and window cleaning.")

    # Prompt user for choice of floors or windows
    y = int(input("Please enter “1” if we are cleaning floors, or “2” for windows. You may add a second service later: \t"))

    # Define invalid entry
    if ((y == 0) or (y > 2)):
        print("Invalid entry.")
        y = int(input("Please enter “1” if we are cleaning floors, or “2” for windows. You may add a second service later: \t"))
        

    # Set floor price based on services
    if y == 1:
        floors = int(input("Please enter “1” for vacuum and “2” for polishing.  You may add a second service later: \t"))
        if floors == 1:
            floorXtra = int(input("Please enter “2” if you would like polishing as well, or enter “1” to continue: \t"))
            # Vacuum and polish floors with window option
            if floorXtra == 2:
                floorPrice = 40
                windows = int(input("Please enter “2” if you are adding windows to your quote, or enter “1” to continue: \t"))
                # Vacuum and polish floors only
                if windows == 1:
                    totalCost = (roomPrice + floorPrice)
                    print("Your total cost is: \t $", totalCost)
            # Vacuum only floors with window option
            elif floorXtra == 1:
                floorPrice = 20
                windows = int(input("Please enter “2” if you are adding windows to your quote, or enter “1” to continue: \t"))
                # Vacuum floors only
                if windows == 1:
                    totalCost = (roomPrice + floorPrice)
                    print("Your total cost is: \t $", totalCost)
        elif floors == 2:
            floorXtra = int(input("Please enter “2” if you would like vacuuming as well, or enter “1” to continue: \t"))
            # Polish and vacuum floors with window option
            if floorXtra == 2:
                floorPrice = 40
                windows = int(input("Please enter “2” if you are adding windows to your quote, or enter “1” to continue: \t"))
                # Polish and vacuum floors only
                if windows == 1:
                    totalCost = (roomPrice + floorPrice)
                    print("Your total cost is: \t $", totalCost)
            # Polish only floors with window option
            elif floorXtra == 1:
                floorPrice = 20
                windows = int(input("Please enter “2” if you are adding windows to your quote, or enter “1” to continue: \t"))
                # Polish floors only
                if windows == 1:
                    totalCost = (roomPrice + floorPrice)
                    print("Your total cost is: \t $", totalCost)
                    
    # Set window price based on services
    if ((y == 2) or (windows == 2)):
        windows = int(input("Please enter “1” for interior and “2” for exterior.  You may add a second service later: \t"))
        if windows == 1:
            windowXtra = int(input("Please enter “2” if you would like exterior as well, or enter “1” to continue: \t"))
            if windowXtra == 2:
                windowPrice = 50
                floorsSecond = int(input("Please enter “2” if you are adding floors to your quote, or enter “1” to continue: \t"))
                # Calculate using floor entries before windows
                if ((floorsSecond == 1) and (y == 1)):
                    totalCost = (roomPrice + floorPrice + windowPrice)
                    print("Your total cost is: \t $", totalCost)
            elif windowXtra == 1:
                windowPrice = 20
                floorsSecond = int(input("Please enter “2” if you are adding floors to your quote, or enter “1” to continue: \t"))
                # Calculate using floor entries before windows
                if ((floorsSecond == 1) and (y == 1)):
                    totalCost = (roomPrice + floorPrice + windowPrice)
                    print("Your total cost is: \t $", totalCost)
                # Allow for user to add floors after windows
                elif floorsSecond == 2:
                    floors = int(input("Please enter “1” for vacuum and “2” for polishing.  You may add a second service later: \t"))
                    if floors == 1:
                        floorXtra = int(input("Please enter “2” if you would like polishing as well, or enter “1” to continue: \t"))
                        # Windows with vacuum and polish floors
                        if floorXtra == 2:
                            floorPrice = 40
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                        # Windows with only vacuum floors
                        elif floorXtra == 1:
                            floorPrice = 20
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                    elif floors == 2:
                        floorXtra = int(input("Please enter “2” if you would like vacuuming as well, or enter “1” to continue: \t"))
                        # Windows with vacuum and polish floors
                        if floorXtra == 2:
                            floorPrice = 40
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                        # Windows with only polish floors
                        elif floorXtra == 1:
                            floorPrice = 20
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                # Interior windows only
                elif floorsSecond == 1:
                    totalCost = (roomPrice + windowPrice)
                    print("Your total cost is: \t $", totalCost)
                    
        elif windows == 2:
            windowXtra = int(input("Please enter “2” if you would like interior as well, or enter “1” to continue: \t"))
            if windowXtra == 2:
                windowPrice = 50
                floorsSecond = int(input("Please enter “2” if you are adding floors to your quote, or enter “1” to continue: \t"))
            elif windowXtra == 1:
                windowPrice = 30
                floorsSecond = int(input("Please enter “2” if you are adding floors to your quote, or enter “1” to continue: \t"))
                # Exterior windows only
                if floorsSecond == 1:
                    totalCost = (roomPrice + windowPrice)
                    print("Your total cost is: \t $", totalCost)
                # Allow for user to add floors after windows
                elif floorsSecond == 2:
                    floors = int(input("Please enter “1” for vacuum and “2” for polishing.  You may add a second service later: \t"))
                    if floors == 1:
                        floorXtra = int(input("Please enter “2” if you would like polishing as well, or enter “1” to continue: \t"))
                        # Windows with vacuum and polish floors
                        if floorXtra == 2:
                            floorPrice = 40
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                        # Windows with only vacuum floors
                        elif floorXtra == 1:
                            floorPrice = 20
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                    elif floors == 2:
                        floorXtra = int(input("Please enter “2” if you would like vacuuming as well, or enter “1” to continue: \t"))
                        # Windows with vacuum and polish floors
                        if floorXtra == 2:
                            floorPrice = 40
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)
                        # Windows with only polish floors
                        elif floorXtra == 1:
                            floorPrice = 20
                            totalCost = (roomPrice + windowPrice + floorPrice)
                            print("Your total cost is: \t $", totalCost)

    
# Execute------------------------------------------------------------------------------------------------------------------------
main()
