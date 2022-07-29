# cd america_state_quiz
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)




# Using csv

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))




# Using pandas

import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
max = data["temp"].max()

# Get Data in Columns
# print(data.condition)
# print(data["condition"])


# Get Data in Raw
# print(data[data.day == "Monday"])


# Max value in Weather data
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
mon = monday.temp
print(mon * 9/5 + 32)