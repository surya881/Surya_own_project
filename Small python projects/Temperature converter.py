def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print("Temperature Converter")
print("--------------------")

while True:
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius: {:.2f}".format(celsius))
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

print("Thank you for using the Temperature Converter!")