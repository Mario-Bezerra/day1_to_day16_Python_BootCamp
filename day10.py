from replit import clear
def calculator(first_number,operation,second_number):
    result = 0
    if operation=="+":
        result = first_number + second_number
    elif operation=="-":
        result = first_number - second_number
    elif operation=="*":
        result = first_number * second_number
    elif operation=="/":
        result = first_number / second_number
    print(f"The result is {result}")
    return result


def calculator_memory(operation,second_number):
    result2 = 0
    if operation=="+":
        result2 = (memory + second_number)
    elif operation=="-":
        result2 = (memory - second_number)
    elif operation=="*":
        result2 = (memory * second_number)
    elif operation=="/":
        result2 = (memory / second_number)
    print(f"The result is {result2}")
    return result2

use_memory = ""
repeat = 1
while repeat == 1:
    first_number = float(input("Type the first number "))
    operation = str(input("Select the operation \n + \n - \n * \n / \n"))
    second_number = float(input("Type the second number "))
    memory = calculator(first_number , operation , second_number)
    use_memory = str(input("Do you wanna use the result 'y' or 'n' ? "))
    clear()
    while use_memory == "y":
        operation = str(input("Select the operation \n + \n - \n * \n / \n"))
        second_number = float(input("Type the other number "))
        memory = calculator_memory(operation , second_number)
        use_memory = str(input("Do you wanna use the result 'y' or 'n' ? "))
        clear()


