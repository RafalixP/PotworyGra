#

#Python implementation goes here

fahreheit = float(input('Please enter the F temperature which you want to convert into Celsius: '))

celsius = (fahreheit - 32) * 5/9

print("Tempratura", fahreheit, "stopni Fahrenheita to", round(celsius, 2), "stopni Celsiusza")