
print("Welcome to the tip calculator")
bill = input(("How much are the bill ?"))
percent_tip = input("What percentage tip would you like to give? 10% , 12% or 15%")
total_bill = float(bill) + (float(bill)*(float(percent_tip)/100))
cont_people = input("How many people to split the bill? ")
bill_for_person = total_bill/int(cont_people)
final_amount = "{:.2f}".format(bill_for_person)
print(f"Each person should pay ${final_amount}")