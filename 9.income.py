unit = float(input("Enter the units: "))

if unit <= 200:
    pay = 0

elif unit <= 400:
    pay = (unit - 200) * 0.05
elif unit <= 800:
    pay = (unit - 200) * 0.10


print(f" your bill is :{pay}")