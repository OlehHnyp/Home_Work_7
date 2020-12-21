def addition(x):
    """
    This function add elements
    in sequence
    Input parameters: x
    Output: float number
    """
    return sum(x)


def substraction(x):
    """
    This function substract elements
    in sequence
    Input parameters: x
    Output: float number
    """
    result = x[0]
    for el in range(1, len(x)):
        result -= x[el]
    return result


def multiplication(x):
    """
    This function multiply elements
    in sequence
    Input parameters: x
    Output: float number
    """
    result = x[0]
    for el in range(1,len(x)):
        result *= x[el]
    return result

def division(x):
    """
    This function divide elements
    in sequence
    Input parameters: x
    Output: float number
    """
    result = x[0]
    for el in range(1,len(x)):
        result /= x[el]
    return result
    