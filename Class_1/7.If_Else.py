# Greater Than
age = 40
print(age > 40)


# Less Than
age = 90
print(age < 100)

# Equal to
age = 120
print(age == 130)

# Not Equal to:
age = 118
print(age != 118)


# IF Statement:
age = 10
if age > 18:
    print("Adult, Can vote.")
else:
    print("Not an Adult, cannot Vote!")

# Multiple if:

age = 10
if age > 10 and age < 20:
    print('Teenager')
elif age >= 20 and age < 30:
    print('Young Adult')
elif age >= 30 and age < 40:
    print('Middle Aged')
elif age >=40 and age < 60:
    print('old')
elif age >= 60:
    print('Senior Citizen')
else:
    print('Child')

# NOT OPERATOR:
city  = str(input('eter your city: '))
if not (city == 'Cuttack' or city == 'Bhubaneswar'):
    print('Outside Odsiha')
else:
    print('Inside Odisha')