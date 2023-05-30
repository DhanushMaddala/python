principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period in years: "))
gender = input("Enter the gender (male/female): ")
senior_citizen = input("Are you a senior citizen? (yes/no): ")

senior_citizen = senior_citizen.lower() == 'yes'
if gender == 'female':
    if senior_citizen:
        rate = 8
    else:
        rate = 6
else:
    if senior_citizen:
        rate = 7
    else:
        rate = 5

interest = (principal * rate * time) / 100
print("Simple Interest: ", interest)
