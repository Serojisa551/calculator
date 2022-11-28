import calcu.count_functions


def calc(one_number, operator, two_number):
    if operator == "+":
        return calcu.count_functions.sum(one_number, two_number)
    elif operator == "-":
        return  calcu.count_functions.sub(one_number, two_number)
    elif operator == "*":
        return calcu.count_functions.mul(one_number, two_number)
    elif operator == "/":
        return calcu.count_functions.divide(one_number, two_number)
    elif operator == "^":
        return calcu.count_functions.degree(one_number, two_number)
    elif operator == "%":
        return calcu.count_functions.percent(one_number, two_number)
    elif operator == "!":
        return calcu.count_functions.factorial(one_number)
