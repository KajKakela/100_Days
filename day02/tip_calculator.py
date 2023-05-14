bill = int(input("How much is the bill? "))
people = int(input("How many people are splitting the bill? "))
tip_percentage = int(input("How many % is the tip? "))

sum_per_person = (bill/people) * ((tip_percentage/100) + 1) 

print(f"Each person should pay {sum_per_person:.2f}")