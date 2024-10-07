Age = float(input("Enter your age: "))

if 1 >= Age:
    print("You are an infant")
elif 13 > Age > 1:
    print("You are a child")
elif 20 > Age >= 13:
    print("You are a teenager")
elif Age >= 20:
    print("You are an adult")
