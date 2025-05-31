# Division
print(10//3) # floor division


# Modulus - Gives Reminder.
print(121%11)
print(13%2)

# Exponential:
a = 4
b = 4**2
print(b)

# Calculation of BMI:
import math
weight = 65
height = 1.75
bmi_type_a = weight / (height**2)
print(bmi_type_a)
bmi_type_b = weight / math.pow(height,2)
print(bmi_type_b)

# Concatenation of String
a = "Ronu"
place = "Cuttack"
print(a+" " + place)

# quotes within quotes:
a = "Ronu's"
print(a)

# DOuble quotes printing
a = '"Ronu"'
print(a)

# Exlplicit Conversion:
import math
weight = 78
height = "1.75"
bmi_type_a = weight / (float(height)**2)
print(bmi_type_a)
bmi_type_b = weight / math.pow(float(height),2)
print(bmi_type_b)

# implicit conversion:
a = 20
b = 10.5
print(a + b) # Python automatically converts int to float for addition


