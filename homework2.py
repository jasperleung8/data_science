import numpy as np

Arr1 = np.full((5,5),10)
Arr2 = np.full((5,5),20)

operation = input("Enter +, -, * or /   ")

if operation == "+":
    print(Arr1+Arr2)
elif operation == "-":
    print(Arr1-Arr2)
elif operation == "*":
    print(Arr1*Arr2)
elif operation == "/":
    print(Arr1/Arr2)
else :
    print("Invalid response")

