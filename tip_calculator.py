print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n £"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_ppl = float(input("How many people to split the bill?\n"))
average = bill * (1 + percentage / 100) / num_ppl
print(f"Each person should pay: £{round(average, 2)}")