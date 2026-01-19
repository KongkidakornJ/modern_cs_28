def check_value(n):
    if int(n) > 0:
        return "POSITIVE"
    elif int(n) < 0:
        return "NEGATIVE"
    else:
        return "ZERO"
    
val = input("Enter the number: ")
print(check_value(val))