def calculate_price(n):
    price = float(n)

    if price >= 1000:
        final = price*0.90
    else:
        final = price
    return final

inp = input("Enter the price: ")
print(f"Final price is : {calculate_price(inp):.2f}")