
import pandas

# data = pandas.read_csv("weather_data(1).csv")
#
#
# data_dict = data.to_dict()
#
#
# temp = data["temp"].tolist()
#
#
# monday = data[data.day == "Monday"]
#
#
#
# dict ={
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 65, 55]
#
# }
#
# dataframe =  pandas.DataFrame(dict)
# print(dataframe)
# dataframe.to_csv("new_data.csv")

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
cinnamon = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black = len(sq_data[sq_data["Primary Fur Color"] == "Black"])
#fcolor_lst = fcolor.tolist()



# for name in fcolor_lst:
#     if name == "Gray":
#         grey += 1
#
#     elif name == "Cinnamon":
#         cinnamon += 1
#
#     elif name == "Black":
#         black += 1

fur_dict =  {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}

dataframe_sq = pandas.DataFrame(fur_dict)

print(dataframe_sq)
# dataframe_sq.to_csv("new_data.csv")