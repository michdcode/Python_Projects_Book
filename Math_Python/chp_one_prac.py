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
