import sys
import logging

logging.basicConfig(level=logging.DEBUG)


def is_number(number):
    is_number = number.isnumeric()
    if is_number == True:
        return float(number)
    else:
        logging.debug(f"Podana wrtość '{number}' nie jest liczbą")
        quit()


def addition_and_multiplication(answer):
    numbers = []
    list_len = input("Na ilu elementach chcesz przeprowadzić działanie: ")
    for i in range(int(list_len)):
        numbers.append(is_number(input(f"Podaj składnik {i+1}: ")))
    if answer == "1":
        logging.debug(f"Sumuję liczby {str(numbers)[1:-1]}")
        result = sum(numbers)
    else:
        logging.debug(f"Mnożę liczby {str(numbers)[1:-1]}")
        result = 1
        for number in numbers:
            result *= number
    print(f"Wynik to: {round(result, 2)}")


def subtraction_and_division(answer):
    first_number = is_number(input("Podaj składnik 1: "))
    second_number = is_number(input("Podaj składnik 2: "))
    if answer == "2":
        logging.debug(f"Odejmuję {first_number} od {second_number}")
        result = first_number - second_number
    else:
        if second_number == 0:
            logging.debug("Nie dziel przez 0 ty... :)")
        else:
            logging.debug(f"Dzielę {first_number} od {second_number}")
            result = first_number / second_number
    print(f"Wynik to: {round(result, 2)}")


if __name__ == "__main__":
    answer = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "
    )
    if answer == "1" or answer == "2":
        addition_and_multiplication(answer)
    elif answer == "3" or answer == "4":
        subtraction_and_division(answer)
    else:
        logging.debug("Podano niedozwoloną wartość")
