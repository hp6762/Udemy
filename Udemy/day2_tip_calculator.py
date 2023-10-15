print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10,12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total_tip = (tip / 100) * bill
total_bill_tip = bill + total_tip
final_bill = total_bill_tip / people
print(f"Each person should pay:{round(final_bill,2)}!")

