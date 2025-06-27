# import csv
import pandas

# data = csv.reader("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])


# data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

data = pandas.read_csv("./csvdata/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color_list = data["Primary Fur Color"].to_list()
gray = 0
black = 0 
cinnamon = 0
for color in primary_fur_color_list:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1  
        
        
fur_color_dict = {
                  "Fur Color": ["gray", "black", "cinnamon"],
                  "count": [gray, black, cinnamon],}

fur_color_df = pandas.DataFrame(data=fur_color_dict)
fur_color_df.to_csv("./csvdata/squirrel_fur_color_count.csv")
