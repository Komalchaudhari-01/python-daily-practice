
t = int(input("Please tell your temperature"))

if t < 0:
    print("Freezing cold")
elif t >= 0 and t < 10:
    print("Very cold")
elif t >= 10 and t < 20:
    print("cold")
elif t >= 20 and t < 30:
    print("Pleasant")
elif t >= 30 and t < 40:
    print("Hot")
else:
    print("Temperature is very hot")
    