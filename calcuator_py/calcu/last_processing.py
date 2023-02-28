def last_processing(number):
    if type(number) == str:
        return number
    else:
        if number % 1 == 0:
            number = int(number)
            return number
        else:
            return number
