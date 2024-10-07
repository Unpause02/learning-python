days = int(input("Enter the number of days worked: "))
pay = 0.01

for day in range(1,days+1):
    pay *= 2.0
    print (' Day', day, "Salary", pay)

print("Your salary on day", days, "would be $", pay)
