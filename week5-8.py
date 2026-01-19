def find_max(a,b,c):
    num1 = int(a)
    num2 = int(b)
    num3 = int(c)

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
inp1 = input("Enter the first number: ")
inp2 = input("Enter the second number: ")
inp3 = input("Enter the third number: ")

print("The maximum is: ", find_max(inp1, inp2, inp3))