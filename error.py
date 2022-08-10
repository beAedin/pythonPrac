# IndexError
fruits = ["Apple","Pear","Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit# pie")
    else:
        print(fruit+" pie")

make_pie(999)



facebook_posts = [
    {'Likes': 21, 'Comments':2},
    {'Likes': 13, 'Comments':2, 'Shares':1},
    {'Likes': 33, 'Comments':8, 'Shares':3},
    {'Comments':4, 'Shares':2},
    {'Comments':1, 'Shares':1},
    {'Likes':19, 'Comments':3},
]

def like():
    total_likes = 0
    try:
        for post in facebook_posts:
            total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0
    print(total_likes)

like()