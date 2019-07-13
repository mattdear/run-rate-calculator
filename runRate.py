#!/bin/python

#Run Rate Calculator by Matthew Dear
#Version 1.6

firstInningsTotal = 0.00
inGame = "y"

print("\nWelcome to the run rate calculator... by Matthew Dear")

while True:
    try:
        isFirstInnings = str.lower((input("First innings? (y/n) ")))
    except ValueError:
        print("Invalid please try again.")

    if isFirstInnings not in ('y','n'):
        print("Invalid please try again.")
    else:
        break        

gameLength = 0

while True:
    try:
        gameLength = int(input("Game length? (20/50) "))
    except ValueError:
        print("Invalid please try again.")
    
    if gameLength == 20:
        break
    elif gameLength == 50:
        break    
    else:
        print("Invalid please try again.")

if isFirstInnings == "y":

    while inGame == "y":

        currentRuns = 0.00

        while True:
            try:
                currentRuns = float(input("\nCurrent run total? "))
            except ValueError:
                print("Invalid please try again.")

            if currentRuns <= 0:
                print("Invalid please try again.")
            else:
                break

        oversUsed = 0.00

        while True:
            try:        
                oversUsed = float(input("Overs used? "))
            except ValueError:
                print("Invalid please try again.")

            if oversUsed <= 0:
                print("Invalid please try again.")
            else:
                break

        runRate = currentRuns / oversUsed
        print("\nCurrent run rate ", "%.2f" % runRate, "\n")
        
        while True:
            try:
                inGame = str.lower(input("update? (y/n) "))
            except ValueError:
                print("Invalid please try again.")

            if inGame not in ('y','n'):
                print("Invalid please try again.")
            else:
                break        

    else:
        print("\n\nThanks for using the run rate calculator... by Matthew Dear\n")

else:

    while inGame == "y":

        if firstInningsTotal == 0.00:

            while True:
                try:
                    firstInningsTotal = float(input("\n1st innings run total? "))
                except ValueError:
                     print("Invalid please try again.")

                if firstInningsTotal <= 0:
                    print("Invalid please try again.")
                else:
                    break                

        else:

            currentRuns = 0.00

            while True:
                try:
                    currentRuns = float(input("Current run total? "))
                except ValueError:
                    print("Invalid please try again.")

                if currentRuns <= 0:
                    print("Invalid please try again.")
                else:
                    break

            oversUsed = 0.00    

            while True:
                try:        
                    oversUsed = float(input("Overs used? "))
                except ValueError:
                    print("Invalid please try again.")

                if oversUsed <= 0:
                    print("Invalid please try again.")
                else:
                    break

            runDifferance = (firstInningsTotal - currentRuns) + 1
            oversRemaining = gameLength - oversUsed
            runRate = runDifferance / oversRemaining
            print("\nRequired run rate ", "%.2f" % runRate, "\n")
            
            while True:
                try:
                    inGame = str.lower(input("update? (y/n) "))
                except ValueError:
                    print("Invalid please try again.")

                if inGame not in ('y','n'):
                    print("Invalid please try again.")
                else:
                    break        

    else:
        print("\n\nThanks for using the run rate calculator... by Matthew Dear\n")