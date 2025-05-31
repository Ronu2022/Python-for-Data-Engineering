# Taking Input From the User:
name = input()
age = input()
print("Hello my name is {} and my age is {}".format(name,age))

# Input with Instructions:
name = str(input("Enter your Name: ")) # why str ? becasue if you simply printed type(name) without str
# it would have given str as the o/p, i.e by default every input is taken as a string. Thus
# conversion becomes necessay as per requirement.
age = int(input("Enter your Age: "))
print("Hello my name is {} and my age is {}".format(name,age))