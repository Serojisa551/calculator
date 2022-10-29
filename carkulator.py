# 5.Write a calculator on python.
def sum(one_number, two_number):
    modul = one_number + two_number
    return modul


def sub(one_number, two_number):
    modul = one_number - two_number
    return modul


def mul(one_number, two_number):
    modul = one_number * two_number
    return modul 


def divide(one_number, two_number):
    if one_number == 0:
        "Cannot be divided by zero"
    else:
        modul = one_number / two_number
        return modul


def degree(one_number, two_number):
    if one_number == 0 and two_number == 0:
        print("0**0 It's impossible")
    else:
        modul = one_number**two_number
        return modul


def percent(one_number, two_number):
    modul = (two_number / 100) * one_number
    return modul


def factorial(one_number):
    amount = 1
    if one_number < 0:
        return "Eror"
    if one_number == 0:
        return 1
    for i in range(1, one_number + 1):
        amount = amount * i
    return amount


def calc(one_number, operator, two_number):
    if operator == "+":
        return sum(one_number, two_number)
    elif operator == "-":
        return sub(one_number, two_number)
    elif operator == "*":
        return mul(one_number, two_number)
    elif operator == "/":
        return divide(one_number, two_number)
    elif operator == "**":
        return degree(one_number, two_number)
    elif operator == "%":
        return percent(one_number, two_number)
    elif operator == "!":
        return factorial(one_number)


def mian():
    one_number = ""
    two_number = ""
    operator = ""
    task = input("input task...")
    for symbols in task:
        if 48 <= ord(symbols) <= 57:
            pass
        elif 43 == ord(symbols) or 45 == ord(symbols):
            pass
        elif 47 == ord(symbols) or 42 == ord(symbols):
            pass
        elif 33 == ord(symbols) or 37 == ord(symbols):
            pass
        else:
            return print("Unidentified object '{}'".format(symbols))
    for symbol in task:
        if 48 <= ord(symbol) <= 57:
            one_number += symbol
            two_number += symbol
        else:
            one_number += " "
            two_number += " "
            operator += symbol
    one_number = one_number[: one_number.index(" ")]
    if operator != "!":
        two_number = two_number[two_number.index(" ") + 1 :]
    one_number = float(one_number)
    two_number = float(two_number)
    if operator == "!":
        one_number = int(one_number)
    print(calc(one_number, operator, two_number))


if __name__ == "__main__":
    mian()
