from Task3_Code_Latest_Coding_File import *

# This is the code to run the graphs, it is separate from the other file to keep it cleaner and more organised


graph_dictionary = {}

### Below is the graphs to get the average delay over the hour for the shared stops
overall_average_bus_delay('Bus_Occupancy_Monday-26-December-2016---Sunday-1-January-2017-(school-holidays-and-NYE).csv',graph_dictionary)
line_graphage(graph_dictionary,"Weekly average bus delay.png")
###

### Graph to get the weekly delay
#overall_hourly_delay('Bus_Occupancy_Monday-26-December-2016---Sunday-1-January-2017-(school-holidays-and-NYE).csv',graph_dictionary)
#line_graphage(graph_dictionary,"Week 3 Delay.png")
#print(graph_dictionary)
###

### Grap to get delay at Each bus stop, each day, each hour
#hourly_bus_delay('Bus_Occupancy_Monday-26-December-2016---Sunday-1-January-2017-(school-holidays-and-NYE).csv', 'hourly_delay_tst.txt', graph_dictionary)
# Each bus stop, each day, each hour average
#average_bus_delay
#bar_graphage(graph_dictionary, "bar week 3.png")

###

# Different weeks to test, copy this into the functions to get the graph for different weeks
# Bus_Occupancy_Monday-8-August-to-Sunday-14th-August-2016-(post-MST-retirement).csv
# Bus_Occupancy_Monday-21-November-2016---Sunday-27-November-2016-(post-fare-reform).csv
# Bus_Occupancy_Monday-26-December-2016---Sunday-1-January-2017-(school-holidays-and-NYE).csv
