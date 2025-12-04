FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


temp = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius(C/F): ")

def convert_to_celsius(fahrenheit):
  temp = (fanhrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}°F is {temp}°C")

convert_to_celsius(100)
  
  
  



  

