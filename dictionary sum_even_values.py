
d = {"a": 10, "b": 15, "c": 20, "d": 7}

total = 0

for value in d.values():
    if value % 2 == 0:   # check even
        total += value

print("Sum of even values:", total)