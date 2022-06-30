import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator")

pw_len = int(input("How many letters would you like in your password?"))
symbols_len = int(input("How may symbols would you like?"))
numbers_len = int(input("How may numbers would you like?"))

# random.choice() : Choose a random element from list
# random.shuffle() : Shuffle list x in place, and return None.

list = []
for char in range(1, pw_len+1):
    list.append(random.choice(letters))

for char in range(1, symbols_len):
    list += random.choice(symbols)
    print(list)

for char in range(1, numbers_len):
    list += random.choice(numbers)

random.shuffle(list)

pw = ""
for char in list:
    pw += char

print(f"Your new password is : {pw}")
