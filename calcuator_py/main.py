# 5.Write a calculator on python.
import calcu.define_operator
import calcu.count_functions


def main():
    task = input("input task...")
    return data_processing(task)


def data_processing(task):
    number_operators = 0
    if task == "":
        return "You haven't written anything"
    elif task[0] in ("^+*/%!"):
        return "Аre you sure you haven't forgotten anything '{}'".format(task)
    for symbols in task:
        if symbols in ("1234567890.^-+*/%!"):
            pass
        else:
            return "Unidentified object '{}'".format(symbols)
    for symbol in range(len(task)):
        if task[symbol] in ("^-+*/%!"):
            break
    if task[0] == "-":
        number_operators -= 1
    for index in range(len(task)):
        if task[index] in ("^-+*/%!"):
            number_operators += 1
    if number_operators != 1:
        return "You wrote the wrong number of operators '{}'".format(task)
    elif symbol == len(task) - 1 and task[symbol] != "!":
        return "You haven't written enough '{}'".format(task)
    # elif task[0] == "-" and  symbol == len(task) -2 and task[symbol] != "!":
    #     return "You haven't written enough '{}'".format(task)
    return separation_elements(task)


def separation_elements(task):
    one_number = ""
    two_number = ""
    number = ""
    operator = ""
    if task[0] == "-":
        one_number = "-"
        task = task[1:]
    for symbol in task:
        if symbol in ("0123456789."):
            number += symbol
        else:
            number += " "
            operator += symbol
    one_number = number[: number.index(" ")]
    if operator != "!":
        two_number = number[number.index(" ") + 1 :]
    if operator == "%":
        if one_number == "0":
            return "This is important, I do not divide it by zero"
    one_number = float(one_number)
    two_number = float(two_number)
    if operator == "!":
        one_number = int(one_number)
    return calcu.define_operator.calc(one_number, operator, two_number)


if __name__ == "__main__":
    print(main())
