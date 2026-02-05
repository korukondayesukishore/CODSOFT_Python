print("Calculator Application")
print("Created by Ramana")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = input("Choose operation (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if option == "1":
    answer = num1 + num2
    print("Answer:", answer)

elif option == "2":
    answer = num1 - num2
    print("Answer:", answer)

elif option == "3":
    answer = num1 * num2
    print("Answer:", answer)

elif option == "4":
    if num2 == 0:
        print("Division not possible")
    else:
        answer = num1 / num2
        print("Answer:", answer)

else:
    print("Wrong choice")

print("Program finished")
