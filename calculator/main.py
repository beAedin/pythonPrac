from art import logo



def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

# Call functions
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))


    for symbol in operations:
        print(symbol)

    isContinue = True
    while isContinue is True:
        operation_symbol = input("Pink an operation: ")
        num2 = float(input("What's the next number?: "))

        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        next = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if next == "y":
            num1 =answer
            continue
        isContinue = False
        calculator()

calculator()