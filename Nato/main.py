numbers = [1, 2, 3, 4, 5]
new_numbers = [i+1 for i in numbers]
print(new_numbers)

new_arr = [i*2 for i in range(1, 6)]
print(new_arr)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_name = [name.upper() for name in names if len(name) >= 5]
print(short_name)
