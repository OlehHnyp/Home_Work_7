import Home_Work_7_Task_1_func as f


operations_and_functions = {
    'addition': f.addition,
    'substraction': f.substraction,
    'multiplication': f.substraction,
    'division': f.division
    }

while True:
    operation = input(
"Hi! I can execute addition, substraction, \
multiplication and division. Which operation do you want \
to execute? :"
    ).lower()
    
    if operation in operations_and_functions.keys():
        break
    else:
        print("Try again.")

while True:
    try:
        numbers = input(
            "Insert your numbers separated by space:"
            ).split()
        float_numbers = [float(el) for el in numbers]
        break
    except ValueError:
        print("Try again.")

result = operations_and_functions.get(operation)(float_numbers)
print(f"Here is the result of {operation}: {result}")
