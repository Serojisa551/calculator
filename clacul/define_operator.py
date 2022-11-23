import clacul.count_functions


def calc(one_number, operator, two_number):
    if operator == "+":
        return clacul.count_functions.sum(one_number, two_number)
    elif operator == "-":
        return clacul.count_functions.sub(one_number, two_number)
    elif operator == "*":
        return clacul.count_functions.mul(one_number, two_number)
    elif operator == "/":
        return clacul.count_functions.divide(one_number, two_number)
    elif operator == "**":
        return clacul.count_functions.degree(one_number, two_number)
    elif operator == "%":
        return clacul.count_functions.percent(one_number, two_number)
    elif operator == "!":
        return clacul.count_functions.factorial(one_number)
    