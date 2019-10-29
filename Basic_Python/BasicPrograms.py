import random
import cmath
import calendar
def hello():
    print('hello world')

def area_of_triangle():
    length = 20
    breadth = 10
    print('area of triangle is',length * breadth)

def arithmaticOperations():
    a = 20
    b = 10
    print('addition is',a+b)
    print('multiplication is',a*b)
    print('division is',a/b)
    print('subraction is',a-b)
    print('modulas is',a%b)
    print('floor devision',a//b)

def SwapNumbers():
    a = 10
    b = 20
    print('numbers before swaping',a,b)
    temp = a
    a = b
    b = temp 
    print('swaping of two numbers with using third variable is',a,b)
    a,b = b,a
    print('swapping of two numbers without using third variable is',a,b)

def RandomGenerator():
    print('Random number between 100 and 200',random.randint(100,200))
    print('Random number between 100 and 200',random.randint(100,200))
    print('Random number between 100 and 200',random.randint(100,200))
    print('Random number between 100 and 200',random.randint(100,200))

def QuadraticEquation():
    a = float(input('enter value a: '))
    b = float(input('enter value b: '))
    c = float(input('enter value c: '))

    #calclate the discrimenent
    d = (b**2) - (4*a*c)

    #find the solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2)) 

def CalculateDistance():
    miles = int(input('enter distance in miles: '))
    kilometers = int(input('enter distance in kilometers'))
    choice =  int(input('enter 1 to convert to kilometers. 2 to convert to miles'))
    if choice == 1:
        #calculate kilometers from miles
        print(miles/0.63127)
    elif choice == 2:
        print(kilometers*0.63217)
    else:
        print('invalid option')

def CalculateTemperature():
    #Fahrenhite = (celsius * 1.8) + 32
    #celsius = (fahrenhite / 1.8) - 32
    temperature_celcius = float(input('enter your temperature in celcius'))
    temperature_fahrenhite = float(input('enter your temperature in fahrenhite'))
    choice = int(input('enter 1 to convert to fahrenhite. 2 to convert to celcius'))
    if choice == 1:
        #calculate celcius to fahrenhite
        print((temperature_celcius * 1.8)+32)
    elif choice == 2:
         print((temperature_fahrenhite / 1.8) - 32)
    else:
        print('invalid option')

def DisplayCalender():
    yy = int(input('enter year'))
    mm = int(input('enter month'))
    print(calendar.month(yy,mm))


hello()
area_of_triangle()
arithmaticOperations()
SwapNumbers()
RandomGenerator()
QuadraticEquation()
CalculateDistance()
CalculateTemperature()
DisplayCalender()