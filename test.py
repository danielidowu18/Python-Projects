def add(x1, x2):
    x  = x1 + x2
    return x

def subtract(x1, x2):
    x  = x1 - x2
    return x

def multiply(x1, x2):
    x  = x1 * x2
    return x

def divide(x1, x2):
    x  = x1 / x2
    return x

first_num = int(input("What's the first number?: "))
operand = input("Which symbol + or - or * or /?: ")
second_num = int(input("What's the second number?: "))
answer = 0
if operand == "+":
    answer = add(first_num, second_num)
elif operand == "-":
    answer = subtract(first_num, second_num)
elif operand == "*":
    answer = multiply(first_num, second_num)
elif operand == "/":
    answer = divide(first_num, second_num)
else:
    print("You entered an invalid symbol")
print(answer)


# num = add(5, 6)
# print(num)