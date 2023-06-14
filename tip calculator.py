#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("tip calculator")
total_bill = float(input("what is the total bill?"))
tip = input("what % tip would you like to give?")
tip = float(tip)
people = int(input("How many people are there?"))

bill_with_tip = (total_bill *(tip/100)) + total_bill
each_person = bill_with_tip/people
each_person = "{:.2f}".format(each_person)

print(f"Each person should pay {each_person}")
