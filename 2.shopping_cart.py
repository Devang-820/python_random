item = input ("what item wold you like to buy? :")
price = float(input("what is the peice?"))
quantity = int(input("how manu would you like ?"))
total = price * quantity

print(f"you have bought {quantity} x  {item} /s")
print(f"your total is = ${total} //")