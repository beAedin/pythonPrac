import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value, "ㅎ")


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a Dataframe
for (index, row) in student_data_frame.iterrows():
    print(row.score)
    if row.student == "Angela":
        print(row.score)
