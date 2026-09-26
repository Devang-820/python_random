num1 = float(input("enter the number "))
num2 = float(input("enter the number "))

#result = "EVEN" if num % 2 == 0 else "odd"
#print("positive" if num> 0 else "not positive")

max_num = num1 if num1 > num2 else num2
min_num = num1 if num1 < num2 else num2
print(min_num)