#!/bin/python

remainingBalls = 0.00
runRate = 0.00
print " "
print("Run rate calculator...")
firstInnings = float(input("1st innings total runs? "))
currentRuns = float(input("2nd innings current run? "))
remainingOvers = float(input("Overs remaining? "))

runDifferance = (firstInnings - currentRuns)
runDifferance = runDifferance + 1
remainingBalls = remainingOvers * 6
runrate = runDifferance / remainingBalls
print " "
print "The required run rate is","%.2f" % runrate
print " "
