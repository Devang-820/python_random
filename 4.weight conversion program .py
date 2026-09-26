weight =float(input("enter your waight:"))
unit = input("kilogreams or pounds? (K or L):")

if unit == "K":
    weight = weight * 2.1
    unit ="lns"
    print(f"your weight is {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight /2.1
    unit="kgs"
    print(f"your weight is {round(weight,1)} {unit}")
else:
     print(f"{unit} was not valid")
