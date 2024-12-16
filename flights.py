#Ryan Haddadi
#Date: November 4th 2021
#Programmers Note: This was one of the most stress inducing labs I have ever done

import json
#Programmers Note: When using datetime in the future don't do from datetime import datetime it'll only import the datetime class and that's it 
import datetime
class Flights:
	#checks to see if a file exists or not
	def __init__(self, filename):
		self.files = filename
		self.list = []
		try:
			with open(self.files, 'r') as a:
				self.list = json.load(a)
		except FileNotFoundError:
			print ("File not found")
	#checks to make sure the format is right and then not only stores the data onto a list but dump it into a file
	def add_flight(self,origin_string, flight_number ,destination_string, departure_string, Next_day, arrival_string):
		format = "%H%M"
		try:
			datetime.datetime.strptime(departure_string, format)
		except ValueError:
			return False

		try:
			datetime.datetime.strptime(arrival_string, format)
		except ValueError:
			return False

		self.list.append([origin_string, flight_number, destination_string, departure_string,Next_day, arrival_string])
		with open(self.files, 'w') as f:
			json.dump(self.list, f)
		return True
#Does the calculations and formats required
	def get_flights(self):
		flight_schedule_list = []
		temp_list_for_append = [] #needed because when using test file it only accepts one argument same issue as I had with add_flights
		#Brings out the data stored from the list
		for list in range(len(self.list)):
				origin_point = self.list[list][0]
				destination_point = self.list[list][2]
				flight_number = self.list[list][1]
				departure_time = self.list[list][3]
				arrival_time = self.list[list][5]

				#Need to put in the : on both departure and arrival because that's the only way the duration time will work I couldn't duration_time after properly formatting departure and arrival time because then there formats wont be similar 
				departure_time = departure_time[:2] + ":" + departure_time[2:]
				arrival_time = arrival_time[:2] + ":" + arrival_time[2:]


				duration_time = str(datetime.datetime.strptime(arrival_time, "%H:%M") - datetime.datetime.strptime(departure_time, "%H:%M"))

				#needed in case the arrival_time is smaller than the departure_time which would cause a negative number
				if len(duration_time) > 8:
   					duration_time = duration_time[8:]
				#Needed to strip to 0 from the format
				duration_time = datetime.datetime.strptime(str(duration_time), '%H:%M:%S')
				duration_time = duration_time.strftime("%H:%M").lstrip("0")


				#departure_time works and used lstrip('0') on both departure and arrival to remove the leading zero in hours
				departure_time = datetime.datetime.strptime(departure_time,'%H:%M').strftime('%I:%M%P').lstrip('0')

				if self.list[list][4] == 'Y':
					arrival_time = datetime.datetime.strptime(arrival_time,'%H:%M').strftime('%I:%M%P').lstrip('0')
					arrival_time = "+" + arrival_time
				else:
					arrival_time = datetime.datetime.strptime(arrival_time, '%H:%M').strftime('%I:%M%P').lstrip('0')

				#Needed to create a temp list in order to store the list into the actual list, if I don't do that then the compiler says I'm storing to many postitional arguments and that only 1 is needed
				temp_list_for_append = [origin_point, flight_number, destination_point, departure_time, arrival_time, duration_time]
				flight_schedule_list.append(temp_list_for_append)
		return flight_schedule_list
	#used to set a different filename
	def different_filename(self, filename):
		self.files = filename
