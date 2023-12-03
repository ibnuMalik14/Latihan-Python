def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0b0'
    binary_result = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_result = str(remainder) + binary_result
        decimal_number = decimal_number // 2
    return '0b' + binary_result

def main():
    try:
        decimal_input = int(input("Masukkan bilangan desimal: "))
        if decimal_input < 0:
            print("Masukkan bilangan desimal non-negatif.")
        else:
            binary_result = decimal_to_binary(decimal_input)
            print(f"Bilangan biner dari {decimal_input} adalah: {binary_result}")
    except ValueError:
        print("Masukkan bilangan desimal yang valid.")

if __name__ == "__main__":
    main()
