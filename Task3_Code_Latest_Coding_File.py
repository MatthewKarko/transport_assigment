import csv #importing library needed to read the file
import matplotlib.pyplot as plt
from numpy import diff


# Function to find the delay for STEP 2 requirements
def bus_time(file_name, file_destination_name):
    with open(file_name) as f: #opening the file
        reader = csv.reader(f) #reading the file
        is_first_line = True #this boolean is checking whether it is the header row (titles)

        avg_time = {} #creating a dictionary that is going to hold all the routes and times
        count = 0
        for row in reader:
            if is_first_line: #checking if it is header rows
                is_first_line = False #skipping the header row

            else:
                # Checking if empty
                if row[0] == 'NaN' or row[0] == '' or row[1] == 'NaN' or row[1] == '' or row[11] == 'NaN' or row[11] == '' or row[12] == 'NaN' or row[12] == '': #Checking for empty and NaN entries in the data
                    continue
                
                else:
                    date = row[0] #These variables are just assigning the information to a usable name
                    route = row[1]

                    """ This section is taking care of the predicted timetable time and converting it to a usable integer """
                    if row[11] != 'NaN' and row[11] != '': #double checking if the value is empty or NaN
                        timetable_time = row[11]
                        values = timetable_time.split(":") #Seperating the time into hours and minutes
                        
                        if int(values[0]) > 12: #Converting the 24hr Hour slot into a usable format
                            timetable_time = ((int(values[0])-12)*60 + int(values[1])) #Converting the time to a minute integer
                        
                        timetable_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer


                    
                    """ This section is taking care of the actual timetable time and converting it to a usable integer """
                    if row[12] != 'NaN' and row[12] != '': #double checking if the value is empty or NaN
                        actual_time = row[12]
                        values = actual_time.split(":")
                        actual_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer
                    
                    """Setting the hour range to a variable as well as the bus stop to a variable """
                    if row[4] != 'NaN' and row[4] != '': #double checking if the value is empty or NaN
                        hour = row[4]

                    if row[8] != 'NaN' and row[8] != '': #double checking if the value is empty or NaN
                        stop = row[8]

                    """ Setting the dictionary key to the dictionary """
                    dict_key = (date, route, hour, stop)

                    """Comparing the times to find the difference between actual and predicted """
                    diff_time = int(actual_time) - timetable_time   

                """ This section checks to see if the certain combination of the dictionary key values is in the 'avg_time' dictionary, 
                    if it is in there then it just appends the new diff_time value that to the values and if not it creates a new key & value combination
                """
                if route == '301' or route == '338' or route == '422' or route == '461':
                    if dict_key not in avg_time:
                        avg_time[dict_key] = [diff_time]

                    else:
                        avg_time[dict_key].append(diff_time)

    """ Creating a new file as write and writing all the results to that file as a print wont be enough for a file of this size"""
                
    with open(file_destination_name, 'w') as output:
        """Adding all the time values to find the overall difference in time over that certain combination , in the format (Date, Route, Hour, BUS_STOP)"""

        for key, value in avg_time.items():
            count = 0
            for i in range(len(value)):
                count += value[i]

            # Creating the output depending on if there was no delay, positive delay (bus was late) and negative delay (bus was early)
            if count > 0:
                output.write(f"{key} The hourly bus delay was {count} minutes for this route.\n")
            elif count == 0:
                output.write(f"{key} There was no hourly delay for the bus on this route.\n")

            else:
                output.write(f"{key} This bus was {abs(count)} minutes early over the hour for this route.\n")

# Running the function here by feeding it the three different files for the weeks, the output is the text files.
# bus_time('Bus_Occupancy_Monday-8-August-to-Sunday-14th-August-2016-(post-MST-retirement).csv', 'results_week1.txt')
# bus_time('Bus_Occupancy_Monday-21-November-2016---Sunday-27-November-2016-(post-fare-reform).csv','results_week2.txt')
# bus_time('Bus_Occupancy_Monday-26-December-2016---Sunday-1-January-2017-(school-holidays-and-NYE).csv', 'results_week3.txt')


"""Code for step 3: Identifying stops that share multiple routes if they exist and then the average delay (so using all points and averaging them, whats the delay probably going
to be. And total hourly delay along the route"""

routes = {}
def hourly_bus_delay(file_name, file_destination_name, graph_dictionary):
    with open(file_name) as f: #opening the file
        reader = csv.reader(f) #reading the file
        is_first_line = True #this boolean is checking whether it is the header row (titles)

        avg_time = {} #creating a dictionary that is going to hold all the routes and times
        count = 0
        for row in reader:
            if is_first_line: #checking if it is header rows
                is_first_line = False #skipping the header row

            else:
                # Once again checking for empty values
                if row[0] == 'NaN' or row[0] == '' or row[1] == 'NaN' or row[1] == '' or row[11] == 'NaN' or row[11] == '' or row[12] == 'NaN' or row[12] == '': #Checking for empty and NaN entries in the data
                    continue
                
                else:
                    date = row[0] #These variables are just assigning the information to a usable name
                    route = row[1]

                    """ This section is taking care of the predicted timetable time and converting it to a usable integer """
                    if row[11] != 'NaN' and row[11] != '': #double checking if the value is empty or NaN
                        timetable_time = row[11]
                    
                        
                        values = timetable_time.split(":") #Seperating the time into hours and minutes
                        
                        if int(values[0]) > 12: #Converting the 24hr Hour slot into a usable format
                            timetable_time = ((int(values[0])-12)*60 + int(values[1])) #Converting the time to a minute integer
                        
                        timetable_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer


                    
                    """ This section is taking care of the actual timetable time and converting it to a usable integer """
                    if row[12] != 'NaN' and row[12] != '': #double checking if the value is empty or NaN
                        actual_time = row[12]
                    

                        values = actual_time.split(":")

                        actual_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer

                    

                    
                    """Setting the hour range to a variable as well as the bus stop to a variable """
                    if row[4] != 'NaN' and row[4] != '': #double checking if the value is empty or NaN
                        hour = row[4]

                    if row[8] != 'NaN' and row[8] != '': #double checking if the value is empty or NaN
                        stop = row[8]

                    """ Setting the dictionary key to the dictionary """
                    dict_key = (date, hour, stop)

                    """Comparing the times to find the difference between actual and predicted """
                    diff_time = int(actual_time) - timetable_time   

                    if diff_time <= -1400:
                        diff_time += 1440
                          

                """ This section checks to see if the certain combination of the dictionary key values is in the 'avg_time' dictionary, 
                    if it is in there then it just appends the new diff_time value that to the values and if not it creates a new key & value combination
                """
                if route == '301' or route == '338' or route == '422' or route == '461':
                    if dict_key not in avg_time:
                        avg_time[dict_key] = [diff_time]

                    else:
                        avg_time[dict_key].append(diff_time)

                    if dict_key not in routes:
                            routes[dict_key] = [route]

                    else:
                        if route not in routes[dict_key]:
                            routes[dict_key].append(route)
    
    """ Creating a new file as write and writing all the results to that file as a print wont be enough for a file of this size"""
    keys = []

    for key, value in routes.items():
        if len(routes[key]) >= 2:
            keys.append(key)
        
    with open(file_destination_name, 'w') as output:
        for key, value in avg_time.items():

            count = 0
            for i in range(len(value)):
                count += value[i]
    
            for i in range(len(keys)):
                if key == keys[i]:
                    graph_dictionary.update({key : count})
                    output.write(f" {key} : Overall delay at route {count} minutes\n")

        output.close()

# Code for the fucntion to get the average bus delay
routes1 = {}
def average_bus_delay(file_name, file_destination_name, graph_dictionary):
    with open(file_name) as f: #opening the file
        reader = csv.reader(f) #reading the file
        is_first_line = True #this boolean is checking whether it is the header row (titles)

        avg_time = {} #creating a dictionary that is going to hold all the routes and times
        count = 0
        for row in reader:
            if is_first_line: #checking if it is header rows
                is_first_line = False #skipping the header row

            else:
                if row[0] == 'NaN' or row[0] == '' or row[1] == 'NaN' or row[1] == '' or row[11] == 'NaN' or row[11] == '' or row[12] == 'NaN' or row[12] == '': #Checking for empty and NaN entries in the data
                    continue
                
                else:
                    date = row[0] #These variables are just assigning the information to a usable name
                    route = row[1]

                    """ This section is taking care of the predicted timetable time and converting it to a usable integer """
                    if row[11] != 'NaN' and row[11] != '': #double checking if the value is empty or NaN
                        timetable_time = row[11]
                    
                        
                        values = timetable_time.split(":") #Seperating the time into hours and minutes
                        
                        if int(values[0]) > 12: #Converting the 24hr Hour slot into a usable format
                            timetable_time = ((int(values[0])-12)*60 + int(values[1])) #Converting the time to a minute integer
                        
                        timetable_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer


                    
                    """ This section is taking care of the actual timetable time and converting it to a usable integer """
                    if row[12] != 'NaN' and row[12] != '': #double checking if the value is empty or NaN
                        actual_time = row[12]
                    

                        values = actual_time.split(":")

                        actual_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer

                    """Setting the hour range to a variable as well as the bus stop to a variable """
                    if row[4] != 'NaN' and row[4] != '': #double checking if the value is empty or NaN
                        hour = row[4]

                    if row[8] != 'NaN' and row[8] != '': #double checking if the value is empty or NaN
                        stop = row[8]

                    """ Setting the dictionary key to the dictionary """
                    dict_key = (hour, stop)

                    """Comparing the times to find the difference between actual and predicted """
                    diff_time = int(actual_time) - timetable_time   

                """ This section checks to see if the certain combination of the dictionary key values is in the 'avg_time' dictionary, 
                    if it is in there then it just appends the new diff_time value that to the values and if not it creates a new key & value combination
                """
                if route == '301' or route == '338' or route == '422' or route == '461':
                    if dict_key not in avg_time:
                        avg_time[dict_key] = [diff_time]
                    else:
                        avg_time[dict_key].append(diff_time)

                    if dict_key not in routes1:
                            routes1[dict_key] = [route]

                    else:
                        if route not in routes1[dict_key]:
                            routes1[dict_key].append(route)

    
    """ Creating a new file as write and writing all the results to that file as a print wont be enough for a file of this size"""
    keys = []

    for key, value in routes1.items():
        if len(routes1[key]) >= 2:
            keys.append(key)
            
        
    with open(file_destination_name, 'w') as output:
        for key, value in avg_time.items():

            for i in range(len(keys)):
                if key == keys[i]:
                    calc = round((sum(value) / len(value)), 1)
                    graph_dictionary.update({key : calc})
                    output.write(f" {key} : Average delay at route {calc} minutes\n")

        output.close()


routes3 = {}
def overall_hourly_delay(file_name, graph_dictionary):

    with open(file_name) as f: #opening the file
        reader = csv.reader(f) #reading the file
        is_first_line = True #this boolean is checking whether it is the header row (titles)

        avg_time = {} #creating a dictionary that is going to hold all the routes and times
        count = 0
        for row in reader:
            if is_first_line: #checking if it is header rows
                is_first_line = False #skipping the header row

            else:
                if row[0] == 'NaN' or row[0] == '' or row[1] == 'NaN' or row[1] == '' or row[11] == 'NaN' or row[11] == '' or row[12] == 'NaN' or row[12] == '': #Checking for empty and NaN entries in the data
                    continue
                
                else:
                    date = row[0] #These variables are just assigning the information to a usable name
                    route = row[1]

                    """ This section is taking care of the predicted timetable time and converting it to a usable integer """
                    if row[11] != 'NaN' and row[11] != '': #double checking if the value is empty or NaN
                        timetable_time = row[11]
                    
                        
                        values = timetable_time.split(":") #Seperating the time into hours and minutes
                        
                        if int(values[0]) > 12: #Converting the 24hr Hour slot into a usable format
                            timetable_time = ((int(values[0])-12)*60 + int(values[1])) #Converting the time to a minute integer
                        
                        timetable_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer


                    
                    """ This section is taking care of the actual timetable time and converting it to a usable integer """
                    if row[12] != 'NaN' and row[12] != '': #double checking if the value is empty or NaN
                        actual_time = row[12]
                    

                        values = actual_time.split(":")

                        actual_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer
                  
                    """Setting the hour range to a variable as well as the bus stop to a variable """
                    if row[4] != 'NaN' and row[4] != '': #double checking if the value is empty or NaN
                        hour = row[4]

                    if row[8] != 'NaN' and row[8] != '': #double checking if the value is empty or NaN
                        stop = row[8]

                    """ Setting the dictionary key to the dictionary """
                    dict_key = (stop)

                    """Comparing the times to find the difference between actual and predicted """
                    diff_time = int(actual_time) - timetable_time   


                    """Accounting and fixing for when there is a midnight rollover"""
                    if diff_time <= -1400:
                        diff_time += 1440

                """ This section checks to see if the certain combination of the dictionary key values is in the 'avg_time' dictionary, 
                    if it is in there then it just appends the new diff_time value that to the values and if not it creates a new key & value combination
                """
                if route == '301' or route == '338' or route == '422' or route == '461':

                    if dict_key not in avg_time:
                        avg_time[dict_key] = [diff_time]

                    else:
                        avg_time[dict_key].append(diff_time)

                    if dict_key not in routes3:
                            routes3[dict_key] = [route]

                    else:
                        if route not in routes3[dict_key]:
                            routes3[dict_key].append(route)

    
    """ Creating a new file as write and writing all the results to that file as a print wont be enough for a file of this size"""
    keys = []

    for key, value in routes3.items():
        print
        if len(routes3[key]) >= 2:
            keys.append(key)        
    # Checking for which bus stops are shared and counting it
    for key, value in avg_time.items():       
        count = 0
        for i in range(len(value)):
            count += value[i]
    
        for i in range(len(keys)):
            if key == keys[i]:
                graph_dictionary.update({key : count})
     
routes2 = {}
def overall_average_bus_delay(file_name, graph_dictionary):
    with open(file_name) as f: #opening the file
        reader = csv.reader(f) #reading the file
        is_first_line = True #this boolean is checking whether it is the header row (titles)

        avg_time = {} #creating a dictionary that is going to hold all the routes and times
        count = 0
        for row in reader:
            if is_first_line: #checking if it is header rows
                is_first_line = False #skipping the header row

            else:
                if row[0] == 'NaN' or row[0] == '' or row[1] == 'NaN' or row[1] == '' or row[11] == 'NaN' or row[11] == '' or row[12] == 'NaN' or row[12] == '': #Checking for empty and NaN entries in the data
                    continue
                
                else:
                    date = row[0] #These variables are just assigning the information to a usable name
                    route = row[1]

                    """ This section is taking care of the predicted timetable time and converting it to a usable integer """
                    if row[11] != 'NaN' and row[11] != '': #double checking if the value is empty or NaN
                        timetable_time = row[11]

                        values = timetable_time.split(":") #Seperating the time into hours and minutes
                        
                        if int(values[0]) > 12: #Converting the 24hr Hour slot into a usable format
                            timetable_time = ((int(values[0])-12)*60 + int(values[1])) #Converting the time to a minute integer
                        
                        timetable_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer
                    
                    """ This section is taking care of the actual timetable time and converting it to a usable integer """
                    if row[12] != 'NaN' and row[12] != '': #double checking if the value is empty or NaN
                        actual_time = row[12]
                    

                        values = actual_time.split(":")

                        actual_time = (int(values[0])*60 + int(values[1])) #Converting the time to a minute integer                  
                    
                    """Setting the hour range to a variable as well as the bus stop to a variable """
                    if row[4] != 'NaN' and row[4] != '': #double checking if the value is empty or NaN
                        hour = row[4]

                    if row[8] != 'NaN' and row[8] != '': #double checking if the value is empty or NaN
                        stop = row[8]

                    """ Setting the dictionary key to the dictionary """
                    dict_key = (stop)

                    """Comparing the times to find the difference between actual and predicted """
                    diff_time = int(actual_time) - timetable_time   

                """ This section checks to see if the certain combination of the dictionary key values is in the 'avg_time' dictionary, 
                    if it is in there then it just appends the new diff_time value that to the values and if not it creates a new key & value combination
                """
                if route == '301' or route == '338' or route == '422' or route == '461':
                    if dict_key not in avg_time:
                        avg_time[dict_key] = [diff_time]
                    else:
                        avg_time[dict_key].append(diff_time)

                    if dict_key not in routes2:
                            routes2[dict_key] = [route]

                    else:
                        if route not in routes2[dict_key]:
                            routes2[dict_key].append(route)

    
    """ Creating a new file as write and writing all the results to that file as a print wont be enough for a file of this size"""
                
    # with open(file_destination_name, 'w') as output:
    #     for key, value in avg_time.items():
    
    #         output.write(f" {key} : {value}\n")

    keys = []

    for key, value in routes2.items():
        if len(routes2[key]) >= 2:
            keys.append(key)       
   # Calculating the average delay
    for key, value in avg_time.items():
        for i in range(len(keys)):
            if key == keys[i]:
                calc = round((sum(value) / len(value)), 1)
                graph_dictionary.update({key : calc})              

# Creating the bar graph              
def bar_graphage(graph_dictionary,bar_graph_name):
    names = list(graph_dictionary.keys())
    values = list(graph_dictionary.values())
    plt.figure()
    plt.bar(range(len(graph_dictionary)), values)
    plt.ylabel("Average Hourly Delay(minutes)")
    plt.xlabel("Number of trips")
    # plt.xticks
    plt.savefig(bar_graph_name) 


    graph_dictionary.clear()
# Creating the line graph
def line_graphage(graph_dictionary,line_graph_name):
    names = list(graph_dictionary.keys())
    values = list(graph_dictionary.values())
    plt.figure()
    plt.ylabel("Delay(minutes)")
    plt.xlabel("Route")
    plt.xticks(fontsize= 6)
    # print(graph_dictionary)
    plt.plot(names, values)
    
    # plt.xlabel()
    # plt.ylabel()
    # plt.title()
    plt.savefig(line_graph_name) 

    graph_dictionary.clear()
