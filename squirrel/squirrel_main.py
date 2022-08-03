import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]
gray_cnt = len(data[color == "Gray"])
cinnamon_cnt = len(data[color == "Cinnamon"])
black_cnt = len(data[color == "Black"])
# print(gray_cnt)
# print(cinnamon_cnt)
# print(black_cnt)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_cnt, cinnamon_cnt, black_cnt]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")