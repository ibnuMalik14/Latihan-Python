while True:
    number = input("Enter Number (or press Enter to exit): ")
    print("Number \t \t Square \t \t Cube")
    # Check if the user pressed Enter without entering a value
    if not number:
        break  # Exit the loop if Enter is pressed without entering a value

    # Convert the input to an integer
    number = int(number)

    square = number ** 2
    cube = number ** 3
    print(str(number) + "\t \t" + str(square) + "\t \t" + str(cube))
