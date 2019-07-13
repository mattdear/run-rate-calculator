#!/bin/python

#Run Rate Calculator by Matthew Dear
#Version 1.5

firstInningsTotal = 0.00
inGame = "y"
print("\nWelcome to the run rate calculator... by Matthew Dear")
isFirstInnings = str(input("First innings? (y/n) "))
gameLength = int(input("Game length? (20/50) "))

if isFirstInnings == "y":

    while inGame == "y":
        currentRuns = float(input("\nCurrent run total? "))
        oversUsed = float(input("Overs used? "))
        runRate = currentRuns / oversUsed
        print("\nCurrent run rate ", "%.2f" % runRate, "\n")
        inGame = input("update? (y/n) ")

    else:
        print("\n\nThanks for using the run rate calculator... by Matthew Dear\n")

else:

    while inGame == "y":

        if firstInningsTotal == 0.00:
            firstInningsTotal = float(input("\n1st innings run total? "))

        else:
            currentRuns = float(input("Current run total? "))
            oversUsed = float(input("Overs used? "))
            runDifferance = (firstInningsTotal - currentRuns) + 1
            oversRemaining = gameLength - oversUsed
            runRate = runDifferance / oversRemaining
            print("\nRequired run rate ", "%.2f" % runRate, "\n")
            inGame = input("update? (y/n) ")

    else:
        print("\n\nThanks for using the run rate calculator... by Matthew Dear\n")