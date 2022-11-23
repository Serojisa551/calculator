# 5.Write a calculator on python.
import clacul.define_operator
import clacul.count_functions


def main():
    task = input("input task...")
    if data_processing(task) != None:
        print(data_processing(task))


def data_processing(task):
    if task == "":
        return "You haven't written anything"
    for symbols in task:
        if symbols in ("1234567890.-+*/%!"):
            pass
        else:
            return "Unidentified object '{}'".format(symbols)
    return tasks(task)


def tasks(task):
    one_number = ""
    two_number = ""
    operator = ""
    for symbol in task:
        if symbol in ("0123456789."):
            one_number += symbol
            two_number += symbol
        else:
            one_number += " "
            two_number += " "
            operator += symbol
    one_number = one_number[: one_number.index(" ")]
    if operator != "!":
        two_number = two_number[two_number.index(" ") + 1:]

    one_number = float(one_number)
    two_number = float(two_number)
    if operator == "!":
        one_number = int(one_number)
    print(clacul.define_operator.calc(one_number, operator, two_number))


if __name__ == "__main__":
    main()
