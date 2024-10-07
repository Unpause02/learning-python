number = 0
total = 0

while number >= 0:
    number = int(input("Enter a number: "))

    if number > 0:
        total += number

    if number < 0:
        break

output = "Total = " + format(total)

print(output)
