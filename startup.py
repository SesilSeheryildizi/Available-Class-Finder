# -*- coding: utf-8 -*-


import random
import csv
#from datetime import datetime
from datetime import datetime, time

DAYS = 5
SLOTS = 6

# Define the duration of a lesson and a break
LESSON_DURATION = 75
BREAK_DURATION = 15

# Define the start and end times of a school day
START_TIME = 8 * 60 + 30
END_TIME = 17 * 60 + 30

# Define the list of lesson names
lesson_names = ['Math', 'English', 'Science', 'History', 'Art', 'Music', 'Physical Education', 'Foreign Language']

# Define the weekly schedule as a 3D array: [day][time slot][classroom]
schedule = [[[None for c in range(5)] for t in range(SLOTS)] for d in range(DAYS)]

# Populate the schedule with random lessons
for day in range(DAYS):
    for slot in range(SLOTS):
        start_time = START_TIME + (slot * (LESSON_DURATION + BREAK_DURATION))
        if start_time < END_TIME:
            for classroom in range(5):
                if random.random() < 0.5:
                    lesson_name = random.choice(lesson_names)
                    schedule[day][slot][classroom] = lesson_name

file= open("startup.txt", "w")                    
                    
for day in range(DAYS):
    print(f"Day{day+1}")
   # m = ["Time",   "Classroom 1 ",  "Classroom 2 ",  "Classroom 3" ,  "Classroom 4" ,  "Classroom 5" ]
    m=("Time        Classroom1   Classroom2   Classroom3   Classroom4   Classroom5")
    print(m)
   
    file.write(f"Day{day+1}" + '\n')
    file.write(m+ '\n')
    for slot in range(SLOTS):
        start_time = START_TIME + (slot * (LESSON_DURATION + BREAK_DURATION))
        end_time = start_time + LESSON_DURATION
        if start_time < END_TIME:
            time_str = f"{start_time//60:02d}:{start_time%60:02d}-{end_time//60:02d}:{end_time%60:02d}"
            row_str = f"{time_str}"
            for classroom in range(5):
                lesson_name = schedule[day][slot][classroom]
                if lesson_name is None:
                    row_str += "  ---        "
                else:
                    row_str += f"  {lesson_name[:3]:<3}        "
            print(row_str)
            
            file.write(row_str + '\n')
              
 
file.close()             
 
 
    
# Open the input file in read mode
with open('startup.txt', 'r') as input_file:
    # Create a CSV writer object for the output file
    with open('output.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)

        # Read the input file line by line
        for line in input_file:
            # Split the line into columns using the tab separator
            columns = line.strip().split()
            # Write the columns to the output file as a row
            writer.writerow(columns)   





with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

#print(data)

#print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

day1= data[:8]
day2= data[8:16]
day3= data[16:24]
day4= data[24:32]
day5= data[32:40]
#print(day1)
#print("-----------------")
#print(day2)
#print("-----------------")
#print(day3)
#print("-----------------")
#print(day4)
#print("-----------------")
#print(day5)
#print("-----------------")



#hour=('08:30-09:45')

def carlos(day,hour):
    print(day)
    
    empty=[]
    for i in range(2,len(day)):
        
        if hour== day[i][0]: 
   
            for j in range(6):
                
                if day[i][j]== ("---"):
                    empty.append(day[1][j])
                    #print( j )
                    #print(day[1][j])
           
    return empty



def hour_converter(hour, converter):
    
    if hour=="08:30" or hour=="8:30" or hour=="08.30" or hour=="8.30":
        new_hour="08:30-09:45"
        converter=True
        return new_hour, converter
    elif hour=="10:00" or hour=="10.00" or hour=="10":
        new_hour="10:00-11:15"    
        converter=True
        return new_hour, converter
    elif hour=="11:30" or hour=="11.30" or hour=="1130":
        new_hour="11:30-12:45"
        converter=True
        return new_hour, converter
    elif hour=="13:00" or hour=="13.00" or hour=="01.00" or hour=="01:00" or hour=="1" or hour=="01" or hour=="13":
        new_hour="13:00-14:15"
        converter=True
        return new_hour, converter
    elif hour=="14:30" or hour=="14.30" or hour=="2.30" or hour=="2:30" or hour=="02:30" or hour=="02.30" :
        new_hour="14:30-15:45"
        converter=True
        return new_hour, converter
    elif hour=="16:00" or hour=="16.00" or hour=="4.00" or hour=="4:00" or hour=="04:00" or hour=="04.00":
        new_hour="16:00-17:15"
        converter=True
        return new_hour, converter
    else:
        print("Wrong Input")
        return hour, converter
        
    



def main():
    
    day= input("Which day? ")
    #hour= input("What clock?")
    
    day=day.upper()
    
    converter=False
    
    
    while converter==False :
        hour= input("When? (Enter the starting time of the lecture): ")
        hour, converter= hour_converter(hour, converter)
        
    d=False
    while d==False:
        if day=="MONDAY" or day=="MON" or day==" MONDAY" or day==" MON":
            d=True
            empty= carlos(day1,hour)
        elif day=="TUESDAY" or day=="TUE" or day==" TUESDAY" or day==" TUE":
            d=True
            empty= carlos(day2,hour)
        elif day=="WEDNESDAY" or day=="WED" or day==" WEDNESDAY" or day==" WED":
            d=True
            empty= carlos(day3,hour)
        elif day=="THURSDAY" or day=="THU" or day==" THURSDAY" or day==" THU":
            d=True
            empty= carlos(day4,hour)
            d=True
        elif day=="FRIDAY" or day=="FRI" or day==" FRIDAY" or day==" FRI":
            empty= carlos(day5,hour)
            d=True
        else: 
            day= input("Which day?")
            day=day.upper()
        
    print(empty)
    
main()
            
#yapılacaklar: kodu temizle, inputun perfect olmadan çalışması, 

    
    



