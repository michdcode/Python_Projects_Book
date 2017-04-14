# Even-Odd Vending Machine
def even_odd(num):
    """Determines if number is even or odd & prints next 9 even or odd numbers."""
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")
    for numbers in range(num, num + 20, 2):
        print(numbers)


def get_number():
    """Gets number from user and checks for correct format or returns error."""
    try:
        number = float(input("Please enter an integer: "))
        #Remember, you are using a float because it can store a number with or
        #without a decimal point and .is_integer() only works on floats and
        #will tell you if the float is an integer(no decimal) or float(decimal)if number.is_integer():
        if number.is_integer():
            even_odd(int(number))
        else:
            return "Please enter an integer."
    except ValueError:
        print("Error: Please enter a number that is an integer.")
