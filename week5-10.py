def bmi(w, h):
    weight = float(w)
    height = float(h)
    bmi = weight / (height*height)
    return bmi

inp1 = input("Enter weight(kg): ")
inp2 = input("Enter height(m): ")

print(f"Output: {bmi(inp1, inp2):.2f}")