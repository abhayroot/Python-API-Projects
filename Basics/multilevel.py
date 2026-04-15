print("""There are 366
days in a leap year""")

#fstring use f with curly braces to user numbers
print(f"The temperature 75F in degrees celsius is {(75 - 32) * 5 / 9}C")

#combining both
print(f"""
    Most countries use the metric system for recipe measurement, 
    but American bakers use a different system. For example, they use 
    fluid ounces to measure liquids instead of milliliters (ml).
    
    So you need to convert recipe units to your local measuring system!
    
    For example, 8 fluid ounces of milk is {8 * 29.5735} ml.
    And 100ml of water is {100 / 29.5735} fluid ounces.
""")

#:.0f strings (.<number of decimal places>f)
# Modify the code to display one decimal place
print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903 :.1f} meters squared!")

#-----------------------------------------------------------------------------------------------------------
#vairables 
name = "Abhay"
age = 23
hight = 5.6

print(f"my age is {age}")
print(f"my hight is {hight}")

print(f"""my name is {name} 
my age is {age} and 
my hight is {hight}""")