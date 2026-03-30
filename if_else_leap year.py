
year = int(input("Enter a year"))

if year % 100 == 0 and year % 400 == 0:
    print(f"It/'s a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print(f"It's a leap year")
else:
    print(f"It/'s not a leap year")