def avg(a, b, c):
    avg = (float(a) + float(b) + float(c))/3
    return avg

inp1 = input("First Number : ")
inp2 = input("Second Number : ")
inp3 = input("Third Number : ")

print(f"The average number is : {avg(inp1, inp2, inp3):.2f}")