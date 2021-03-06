from fractions import Fraction


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


def multiplication_table(num, ran):
    """"Prints out multiples for a number up to a number."""

    for numbers in range(1, ran + 1):
        print('{0} x {1} = {2}'.format(num, numbers, num*numbers))


def get_table_numbers():
    """Gets numbers from user for table."""

    try:
        user_number = float(input("Enter a number: "))
        multiple_limit = float(input("How many multiples?: "))
        if user_number.is_integer() and multiple_limit.is_integer():
            multiplication_table(int(user_number), int(multiple_limit))
        else:
            return "Both numbers must be integers."
    except ValueError:
        print("Error: Please enter a number that is an integer.")


def fraction_calculator(first_num, second_num, operation):
    """Performs selected math operation on user input."""

    if operation == "add":
        result = first_num + second_num
        print("Adding {0} to {1} results in {2}".format(first_num, second_num, result))
    elif operation == "subtract":
        result = first_num - second_num
        print("Subtracting {0} from {1} results in {2}".format(first_num, second_num, result))
    elif operation == "multiply":
        result = first_num * second_num
        print("Multiplying {0} by {1} results in {2}".format(first_num, second_num, result))
    else:
        try:
            result = first_num / second_num
            print("Dividing {0} by {1} results in {2}".format(first_num, second_num, result))
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")


def get_calculator_vals():
    """Gets calculator numbers from user."""

    try:
        first_n = Fraction(input("Enter first fraction in this format x/y: "))
        second_n = Fraction(input("Enter second fraction in this format x/y: "))
        op = input("Enter the name of the operation i this format: add, subtract, multiply, divide: ")
        if op == "add" or op == "subtract" or op == "multiply" or op == "divide":
            fraction_calculator(first_n, second_n, op)
        else:
            return "You did not enter a valid operation."
    except ValueError:
        print("Numerator and Demonator must be whole numbers.")
