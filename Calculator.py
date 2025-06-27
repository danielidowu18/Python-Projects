def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operands = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
userAnswer = "n"
while userAnswer == "n":
    num1 = float(input("What is the first number?: "))
    for operation in operands:
        print(operation)
    operands_symbol = input("Pick an operation from above: ")
    num2 = float(input("What is the second number?: "))
    answer_function = operands[operands_symbol]
    answer = answer_function(n1=num1, n2=num2)
    print(f"{num1} {operands_symbol} {num2} = {answer}")
    userAnswer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'end' to exit: ").lower()
    while userAnswer == "y": 
            operands_symbol = input("Pick an operation: ")
            num3 = float(input("What is the next number?: "))
            answer_function = operands[operands_symbol]
            new_answer = answer_function(n1=answer, n2=num3)
            print(f"{answer} {operands_symbol} {num3} = {new_answer}")
            userAnswer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'end' to exit: ").lower()
