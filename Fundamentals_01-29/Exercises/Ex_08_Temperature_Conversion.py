# Temperature Conversion Program

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F/K): ").strip().lower()

if unit == "c":
    temperature_f = (temperature * 9/5) + 32
    temperature_k = temperature + 273.15
    print(f"The temperature in Fahrenheit is: {temperature_f:.2f}°F")
    print(f"The temperature in Kelvin is: {temperature_k:.2f}K")
elif unit == "f":
    temperature_c = (temperature - 32) * 5/9
    temperature_k = temperature_c + 273.15
    print(f"The temperature in Celsius is: {temperature_c:.2f}°C")
    print(f"The temperature in Kelvin is: {temperature_k:.2f}K")
elif unit == "k":
    temperature_c = temperature - 273.15
    temperature_f = (temperature_c * 9/5) + 32
    print(f"The temperature in Celsius is: {temperature_c:.2f}°C")
    print(f"The temperature in Fahrenheit is: {temperature_f:.2f}°F")   
else:
    print("Invalid unit. Please enter 'C', 'F', or 'K'.")
    exit()
