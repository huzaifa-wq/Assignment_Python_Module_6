import math

def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100      # convert cm → m
    area = math.pi * radius_m ** 2           # area in square meters
    return price_eur / area                  # €/m²

# Main program
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (€): "))

d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (€): "))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

print(f"Pizza 1 unit price: {price1:.2f} €/m²")
print(f"Pizza 2 unit price: {price2:.2f} €/m²")

if price1 < price2:
    print("Pizza 1 provides better value for money.")
elif price2 < price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value for money.")
