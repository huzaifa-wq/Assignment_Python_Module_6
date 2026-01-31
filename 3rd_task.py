def gallons_to_liters(gallons):
    return gallons * 3.78541


# Main program
while True:
    gallons = float(input("Enter the amount of gasoline in gallons: "))

    if gallons < 0:
        break

    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters")
