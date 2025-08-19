# Logical operators evaluate multiple conditions (or, and, not)
#    or  - At least one condition must be true
#    and - All conditions must be true
#    not - Inverts the truth value of a condition

temp = 25
is_raining = False

if temp > 35 or is_raining:
    print("It's too hot or it's raining, stay indoors!")
elif temp < 15 and not is_raining:
    print("It's too cold and not raining, wear a jacket!")
else:
    print("The weather is fine, enjoy your day!")
    
temp = 7
is_sunny = True
if temp >= 28 and is_sunny:
    print("It's hot outside today 🥵")
elif temp < 28 and temp >= 5 and is_sunny:
    print("It's warm outside today ☀️")
elif temp < 5 or not is_sunny:
    print("It's cold and cloudy outside today 🥶 ☁️")
else:
    print("It's not that hot outside today 😌")