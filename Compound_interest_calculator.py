# Python compound interest calculator 
# compound interest formula 
# name variables you'll need, its P, i and t

Principle = 0 
rate = 0 
time = 0 
# first start with what happens with the principle amount
while Principle <= 0:
    Principle= float(input('Enter the Princinple amount: '))
    if Principle <=0:
        print ('Principle cannot be equal or less than zero')

print (Principle)
# Do the same for the rate of interest
while rate <= 0:
    rate = float(input('Enter the rate of interest: '))
    if rate <=0:
        print ('rate of interest cannot be equal or less than zero')

print(rate)
# same thing with the time 
while time <= 0:
    time = int(input('Enter the number of years: '))
    if rate <=0:
        print ('Time cannot be equal or less than zero')

print(time)
# compound interest formula
Total = Principle * pow(1 + rate/100, time)

print(f'Your compounded amount will be: R{Total:.2f}' )




      

