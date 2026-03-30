
name = input("Enter your name")
age = abs(int(input("Enter your age")))

if age >=18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"oops! you are not a valid voter")