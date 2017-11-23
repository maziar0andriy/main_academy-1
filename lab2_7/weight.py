print('Software to calculate your weight index')

a = float(input('Your height in metres: '))
b = float(input('Your weight in kilograms: '))
c = b/(a**2)
print ("Your weight index is: {}".format(c))
if c>=18 and c<=25:
    print('Normal weight range')
elif c>=25 and c<=30:
    print('Overweight')
elif c>=30 and c<=35:
    print('1 degree of obesity')
elif c>=35 and c<=40:
    print('2 degree of obesity')
elif c>40:
    print('3 degree of obesity')
elif c<18:
    print('You need to urgently raise your weight')
else:
    print('Incorrect input data')