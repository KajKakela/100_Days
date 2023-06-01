def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operator = input("Pick an operator from above: ")
num2 = int(input("What's the next number?: "))

calc_func = operations[operator]
answer = calc_func(num1, num2)

print(f"\n{num1} {operator} {num2} = {answer}\n")

want_to_continue = input(
    f"type 'y' if you want to keep calculating with number {answer}, type 'n' if you want to quit: "
)

while want_to_continue == "y":
    first_number = answer
    print(f"\nFirst number is {first_number}\n")

    for symbol in operations:
        print(symbol)

    operator = input("Pick an operator from above: ")

    second_number = int(input("\nWhat's the next number?: "))
    calc_func = operations[operator]
    answer = calc_func(first_number, second_number)

    print(f"\n{first_number} {operator} {second_number} = {answer}")

    want_to_continue = input(
        f"\ntype 'y' if you want to keep calculating with number {answer}, type 'n' if you want to quit: "
    )
