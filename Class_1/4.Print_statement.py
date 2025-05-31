name = 'Ronu'
age = 32
# fstring printing:
print(f'Hello my name is {name} and I am {age}')

# Input from user:
n = str(input('Enter Your Name: '))
a = int(input('Enter your Age: '))
print(f'Hello my name is {n} and I an {a} years old.')

# dot format printing:
print("Hello my name is {} and I am {} years old".format(n,a))

# loguru:
# at first install logguru 
# "C:\Users\Ronu\AppData\Local\Programs\Python\Python310\python.exe" -m pip install loguru 
# copy above in the command promt and run it!!
from loguru import logger  #importing loguru
a = 'Raju'
b = 24
logger.info("Hello my name is {} and my age is {}".format(a,b))


# Area of rectangle:
Length = float(input("Enter the length of the rectangle: "))
Width = float(input("Enter the breadth of the rectangle: "))
area = Length * Width
logger.info("The area of the rectangle is {}".format(area))
