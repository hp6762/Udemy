print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10,12, or 15?\n")
split_people = input("How many people to split the bill?\n")
bill = float(total_bill)
int_tip = int(tip)
total_tip = (int_tip / 100) * bill
total_bill_tip = bill + total_tip
people = int(split_people)
final_bill = total_bill_tip / people
print(f"Each person should pay:{round(final_bill,2)}!")

