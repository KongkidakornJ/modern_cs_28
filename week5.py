#OOP
def SUM(a, b, c):
    sum = float(a) + float(b) + float(c)
    return sum

def minus(a, b):
    minus = float(a) - float(b)
    return minus

def multiply(a, b):
    multiply = float(a)*float(b)
    return multiply

def divide(a, b):
    divide = float(a)/float(b)
    return divide

operate = input("1 = Sum, 2 = Minus, 3 = Multiply, 4 = Divide :")

if(operate == "1"):
    inp1 = input("A :")
    inp2 = input("B :")
    inp3 = input("C :")
    print("SUM =", SUM(inp1, inp2 ,inp3))
elif(operate == "2"):
    inp1 = input("A :")
    inp2 = input("B :")
    print("Minus =", minus(inp1, inp2))
elif(operate == "3"):
    inp1 = input("A :")
    inp2 = input("B :")
    print("Multiply =", multiply(inp1, inp2))
elif(operate == "4"):
    inp1 = input("A :")
    inp2 = input("B :")
    print("Divide =", divide(inp1, inp2))
else:
    print("Not Found")

#print("SUM =", SUM(10, 11 ,12))
#print("MINUS =", minus(30, 25))
#print("Multiply =", multiply(10, 11))
#print("Divide =", divide(10, 11))