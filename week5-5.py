def temp(c):
    temp = float(c)*9/5 + 32
    return temp

input = input("Enter the temperature in Celcius : ")

print(f"The temperature in Fahrenheit is : {temp(input):.1f}")