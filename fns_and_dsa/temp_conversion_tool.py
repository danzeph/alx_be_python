FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# fucntion to convert from fahrenheit to celsius
def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}°F is {celsius}°C")
 
# function to convert from celsius to fahrenheit
def convert_to_fahrenheit(celsius):
  fahrenheit =  FAHRENHEIT_TO_CELSIUS_FACTOR * celsius + 32
  print(f"{celsius}°C is {fahrenheit}°F")
  
# Validate temperature
while True:
    try: 
        temps = input("Enter the temperature to convert: ")
        temp = float(temps)
      if temps == "Q":
        print("Exiting...")
        exit()
        break
    except ValueError:
        print(f"Invalid temperature {temps}! \n")

# Validate unit
while True:
    temp_units = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
    temp_unit = temp_units.upper()
    if temp_unit in ("C", "F"):
        break
    elif temp_unit == "Q":
        print("Exiting...")
        exit()
    else:
        print(f"Invalid unit. {temp_units}! enter q to quit")
        
if temp_unit == "C":
    convert_to_fahrenheit(temp)
else:
    convert_to_celsius(temp)

