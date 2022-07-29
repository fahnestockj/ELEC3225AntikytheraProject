from datetime import datetime
from genericpath import exists
from operator import length_hint
import sqlite3
import solarSystem
import query
from datetime import datetime

conn = sqlite3.connect('Database.db')
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = conn.cursor()
def main(): 
#Main function of the code. Initializes the UI, calls functions and acts as a way to return to the "Main screen" when working in other functions.
	print("1. Search in database")
	print("2. View solar eclipse dates")
	print("3. View lunar eclipse dates")
	print("4. View solar conjuction dates")
	print("5. View solar system simulation")
	print("0. Exit")
	choice = input("Please choose an option from above: ")
	if choice == "1":
		#query()
		dateStr = input("input a date to search by in yyyy-mm-dd format: ")
		format = '%Y-%m-%d'
		try:
			datetime2 = datetime.strptime(dateStr, format)
		except:
			print("Invalid date format")
			main()
		
		print('Event types: lunarEclipse, solarEclipse, conjunction')

		eventType = input("Please enter the type of event you would like to search for: ")
		if eventType == "lunarEclipse":
			result = query.searchLunar(dateStr)
			if(result == None):
				print("No lunar eclipse found")
			else:
				print(result)
		elif eventType == "solarEclipse":
			result = query.searchSolar(dateStr)
			if(result == None):
				print("No solar eclipse found")
			else:
				print(result)

		elif eventType == "conjunction":
			result = query.searchConj(dateStr)
			if(result == None):
				print("No conjuction found")
			else:
				print(result)
		else:
			print("Invalid event type")
			main()
		main()
	elif choice == "2":
		# QUERY FOR ALL SOLAR ECLIPSES
		print("Entire table of solar eclipses:")
		cursor.execute("""SELECT SOLAR_ECLIPSES.DATE FROM SOLAR_ECLIPSES""")
		query_result = cursor.fetchall()
		sort_list = []
		for i in query_result:
		# 	query_result.sort(key = lambda date: datetime.strptime(date, "%d-%m-%y"))
		# 	print()
			print("Date: ", i[0])
			sort_list.append(i[0])
		sort_list.sort(key = lambda date: datetime.strptime(date, "%Y-%m-%d"))
		for j in sort_list:
			print(j)
		print("\n")
		main()
	elif choice == "3":
		# QUERY FOR ALL LUNAR ECLIPSES
		print("Entire table of lunar eclipses:")
		cursor.execute("""SELECT LUNAR_ECLIPSES.DATE FROM LUNAR_ECLIPSES""")
		query_result = cursor.fetchall()
		sort_list = []
		for i in query_result:
			sort_list.append(i[0])
		sort_list.sort(key = lambda date: datetime.strptime(date, "%Y-%m-%d"))
		for j in sort_list:
			print(j)
		print("\n")
		main()
	elif choice == "4":
		# # QUERY FOR ALL BODIES
		# print("Entire table of celestial bodies:")
		# cursor.execute("""SELECT * FROM BODIES""")
		# query_result = cursor.fetchall()
		# for i in query_result:
		# 	print(i)
		# print("\n")
		# # QUERY FOR ALL MOONS
		# print("Entire table of all moons:")
		# cursor.execute("""SELECT * FROM MOON""")
		# query_result = cursor.fetchall()
		# for i in query_result:
		# 	print(i)
		# print("\n")
		# QUERY FOR ALL CONJUNCTIONS
		print("Entire table of planet conjunctions:")
		print("1 = Mercury, 2 = Venus, 3 = Earth, 4 = Mars, 5 = Jupiter, 6 = Saturn, 7 = Uranus, 8 = Neptune, 9 = Pluto")
		cursor.execute("""SELECT CONJUNCTION.DATE, CONJUNCTION.FIRST_PLANET, CONJUNCTION.SECOND_PLANET FROM CONJUNCTION""")
		query_result = cursor.fetchall()
		sort_list = []
		for i in query_result:
			sort_list.append(i[0])
		sort_list.sort(key = lambda date: datetime.strptime(date, "%Y-%m-%d"))
		for j in sort_list:
			print(j)
		print("\n")		
		# # QUERY FOR ALL LUNAR ECLIPSES
		# print("Entire table of lunar eclipses:")
		# cursor.execute("""SELECT * FROM LUNAR_ECLIPSES""")
		# query_result = cursor.fetchall()
		# for i in query_result:
		# 	print(i)
		# print("\n")
		# # QUERY FOR ALL SOLAR ECLIPSES
		# print("Entire table of solar eclipses:")
		# cursor.execute("""SELECT * FROM SOLAR_ECLIPSES""")
		# query_result = cursor.fetchall()
		# for i in query_result:
		# 	print(i)
		# print("\n")
		main()
	elif choice == "5":
		#horizonstesting.py <---Is this the correct .py file for showing the solar system simulation?
		dateStr = input("input a simulation start date in yyyy-mm-dd format: ")
		format = '%Y-%m-%d'
		try:
			datetime1 = datetime.strptime(dateStr, format)
		except:
			print("Invalid date format")
			main()
		
		lengthStr = input("input a simulation length (in days): ")
		try:
			length = int(lengthStr)
			if(length < 0):
				print("Invalid length")
				main()
		except:
			print("Invalid length")
			main()

		# simulation("2002-01-01")
		solarSystem.simulation(dateStr, lengthStr)
		main()
	elif choice == "0":
		print("Goodbye.")
	else:
		print("That is not a valid choice.")
		main()