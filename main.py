# 5.Write a calculator on python.
import clacul.define_operator
import clacul.count_functions


def main():
    task = input("input task...")
    if tasks(task) != None:
        print(tasks(task))


def tasks(task):
    one_number = ""
    two_number = ""
    operator = ""

    for symbols in task:
        if 48 <= ord(symbols) <= 57:
            pass
        elif 43 == ord(symbols) or 45 == ord(symbols) or 46 == ord(symbols):
            pass
        elif 47 == ord(symbols) or 42 == ord(symbols):
            pass
        elif 33 == ord(symbols) or 37 == ord(symbols):
            pass
        else:
            return "Unidentified object '{}'".format(symbols)
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
