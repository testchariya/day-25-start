# # with open("weather_data.csv") as file:
# #     weather_report = file.readlines()
# #     print(weather_report)
# #     weather_report
#
# # import csv
# import pandas
# # print(pandas.__version__)
# import math
#
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     # print(data)
# #     temperatures = []
# #     for row in data:
# #         print(row)
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
# #
# data = pandas.read_csv("weather_data.csv")
# # # print(data)
# # # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(sum(temp_list)/len(temp_list))
# # print(data["temp"].median())
# # print(data["temp"].max())
# #
# # print(data["condition"])
# # print(data.condition)
#
# # print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# temp_in_f = ((monday.temp * 9/5)+32)
# print(temp_in_f)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# for x in sq_table:
# print(sq_table["Primary Fur Color"].count())
# print(sq_table["Primary Fur Color"].sample(10))
print(data["Primary Fur Color"].value_counts())

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrels["Primary Fur Color"].count())
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
print(red_squirrels["Primary Fur Color"].count())
black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(black_squirrels["Primary Fur Color"].count())
ukn_squirrels = data[data["Primary Fur Color"] == ""]
print(ukn_squirrels["Primary Fur Color"].count())

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [len(grey_squirrels), len(red_squirrels), len(black_squirrels)]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

df2 = pandas.DataFrame(data["Primary Fur Color"].value_counts())
# data["Primary Fur Color"].value_counts()
df2.to_csv("squirrel2_count.csv")

# print(sq_table["Primary Fur Color"].groupby(level=0).count())

# grey = 0
# red = 0
# black = 0
#
# for x in sq_table:
#     if sq_table["Primary Fur Color"] == "Gray":
#         grey += 1
#     if sq_table["Primary Fur Color"] == "red":
#         red += 1
#     if sq_table["Primary Fur Color"] == "black":
#         black += 1
