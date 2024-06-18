print("Write a program that reads data from a CSV file and prints it to the console. ")

import csv 
	
header = ['Student Name ', 'Subject', 'marks'] 
	
rows = [ ["Saransh","maths",90], 
		["ankit","science",80], 
		["neetu","sst",85], 
		["sapna","hindi",88]] 
	
filename = "college.csv"
with open(filename, 'w') as csvfile: 
	csvwriter = csv.writer(csvfile) 

	csvwriter.writerow(header) 
		
	csvwriter.writerows(rows) 
with open('college.csv', mode ='r') as file: 
	csvFile = csv.DictReader(file)
	for lines in csvFile:
			print(lines)
