from fractions import Fraction


def factors(num):
    """Find the factors of a given number."""

    for numbers in range(1, num+1):
        if num % numbers == 0:
            print(numbers)

    your_num = input('Please enter a number: ')
    your_num = float(your_num)

    if your_num > 0 & your_num.is_integer():
        factors(int(your_num))
    else:
        print('Please enter a positive integer.')


def multiplication_table(num):
    """"Prints out multiples for a number up to 10."""

    for numbers in range(1, 11):
        print('{0} x {1} = {2}'.format(num, numbers, num*numbers))

    user_number = input("Enter a number: ")
    multiplication_table(float(user_number))


def fahrenheit_to_celsius():
    """Converts fahrenheit to Celsius."""

    fahrenheit = float(input('Please enter the degrees in fahrenheit: '))
    celsius = (fahrenheit - 32) * Fraction(5, 9)
    print('Temperature in Celsius is: {0:.2f}'.format(celsius))


def celsius_to_fahrenheit():
    """Converts Celsius to Fahrenheit."""

    celsius = float(input('Please enter the degrees in celsius: '))
    fahrenheit = (celsius * Fraction(9, 5)) + 32
    print('Temperature in Fahrenheit is: {0:.2f}'.format(fahrenheit))


def inches_to_meters():
    """Converts inches to meters."""

    inches = float(input('Please enter the number of inches: '))
    meters = (inches * 2.54)/100
    print('Distance in meters is: {0}'.format(meters))


def miles_to_kilometers():
    """Converts miles to kilometers."""

    miles = float(input('Please enter the number of miles: '))
    KM = (miles * 1.609)
    print('Distance in kilometers is: {0}'.format(KM))


def calc_quadratic_equ_root(a, b, c):
    """Finds the roots in a quadratic equation"""

    D = (b*b - 4*a*c)**0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)
    print('x1: {0}'.format(x1))
    print('x2: {0}'.format(x2))


def gather_root_data():
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    calc_quadratic_equ_root(float(a), float(b), float(c))

