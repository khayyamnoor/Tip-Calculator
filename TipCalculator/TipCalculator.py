print("Welcome to the tip calculator")
bill=float(input("What is the total bill:"))
perc=int(input("What percentage tip do you wanna give:"))
people=int(input("How many people do you wanna split in:"))
new_perc= perc/100 *bill
result=((bill + new_perc)/ people)
print(round(result,2))