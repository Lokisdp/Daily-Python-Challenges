import art
# first_number = int(input("Enter first number: "))
# for symbol in operations
# operand = input("Choose mathematical operand '*', '+', '-','/',: ")
# second_number = int(input("Enter second number: "))
# ask_user = input(f"Do you want to continue with previous result {result}. Then type 'Y' or No for 'N'.").lower()

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {"+":add,
              "-":sub,
              "*":multi,
              "/":div,
}

def cal_function():
    print(art.logo)
    calculator = True
    first_number = float(input("Enter first number: "))

    while calculator:
        for symbol in operations:
            print(symbol)
        operand = input("Choose mathematical operand: ")
        second_number = float(input("Enter next number: "))

        result = operations[operand](first_number, second_number)
        print(f"{first_number} {operand} {second_number} = {result}")

        ask_user = input(f"Do you want to continue with previous result {result}. Then type 'Y' or No for 'N' to start a new calculation"
                         f".").lower()

        if ask_user == "y":
            first_number = result

        else:
            calculator = False
            print(f"Final Answer: {result}")
            print("\n" * 25)
            cal_function()

cal_function()


# for operand in operations:
#     if operand == "*":
#         output = multi(4,8)
#         print(output)

# first_number = int(input("Enter first: "))
# operand = input("Choose mathematical operand '*', '+', '-','/',: ")
# second_number = int(input("Enter second number: "))