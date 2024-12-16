#Ryan Haddadi
#Date: November 4th 2021

#need to import flights file
from flights import *

#stores the flight schedule into a file for use later
flight = Flights("txt.dat")

#creates an empty list to hold our flight schedule
flight_list = []
#used for inside the loop when user needs to make a loop
choice = 0

#While loop will continue until the user chooses choice 4 which will break out of the loop
while(True):
	print ("***Tuffy Titan Flight Schedule Main Menu***")
	print ("1.)Add Flight")
	print ("2.)Print Flight Schedule")
	print ("3.)Set Flight Schedule Filename")
	print ("4.)Exit The Program")
	choice = int(input("Enter menu choice:"))
	#This asks the user to input there own flight schedule and then sends it to add_flight to make sure the format is right and then send it to the txt.dat file
	if choice == 1:
		Origin = input("Enter origin:")
		Destination = input("Enter destination:")
		Flight_Number = input("Enter flight number:")
		Departure_Time = input("Enter departure time (HHMM):")
		Arrival_Time = input("Enter arrival time (HHMM):")
		Next_Day = input("Is arrival time next day (Y/N):")
		flight.add_flight(Origin, Flight_Number,Destination,Departure_Time,Arrival_Time,Next_Day)
	#prints out the schedule based on whats in the txt.dat file
	elif choice == 2:
		print ("================= Flight Schedule =================")
		print ("Origin              Number       Destination  Departure   Arrival     Duration")
		flight_list = flight.get_flights()
		for schedule in range(len(flight_list)):
			print(f"{flight_list[schedule][0]:20}{flight_list[schedule][1]:14}{flight_list[schedule][2]:10}{flight_list[schedule][3]:15}{flight_list[schedule][4]:10}{flight_list[schedule][5]}")
	#Helps store the schedule data to another file
	elif choice == 3:
		filename = input("Enter the filename that you want to store the schedule in")
		flight.different_filename(filename)
	elif choice == 4:
		break
