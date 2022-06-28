print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
bill_tip = tip / 100 * bill + bill
final = round(bill_tip/people,2)
print(f"Each person should pay : ${final}")