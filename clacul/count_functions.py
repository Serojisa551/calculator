import clacul.last_processing

def sum(one_number, two_number):
    modul = one_number + two_number
    return clacul.last_processing.last_processing(modul)


def sub(one_number, two_number):
    modul = one_number - two_number
    return clacul.last_processing.last_processing(modul)


def mul(one_number, two_number):
    modul = one_number * two_number
    return clacul.last_processing.last_processing(modul)


def divide(one_number, two_number):
    if one_number == 0:
       modul = "Cannot be divided by zero"
       return clacul.last_processing.last_processing(modul)
    else:
        modul = one_number / two_number
        return clacul.last_processing.last_processing(modul)


def degree(one_number, two_number):
    if one_number == 0 and two_number == 0:
        modul= "0**0 It's impossible"
        return clacul.last_processing.last_processing(modul) 
    else:
        modul = one_number**two_number
        return clacul.last_processing.last_processing(modul) 


def percent(one_number, two_number):
    modul = (two_number / one_number) * 100
    return clacul.last_processing.last_processing(modul)


def factorial(one_number):
    modul = 1
    if one_number < 0:
        modul= "Eror"
        return clacul.last_processing.last_processing(modul)
    if one_number == 0:
        modul= 1
        return clacul.last_processing.last_processing(modul)
    for i in range(1, one_number + 1):
        modul = modul * i
    return clacul.last_processing.last_processing(modul)
    
