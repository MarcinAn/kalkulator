import sys
import logging

logging.basicConfig(level=logging.DEBUG)


def check_number(input_number):
    number = input(f"Podaj składnik {input_number}: ")
    while not number.isnumeric():
        logging.debug(
            f"Wprowadzona wartość {number} nie jest liczbą. Wprowadż wartość ponownie."
        )
        number = input(f"Podaj składnik {input_number}: ")
    return float(number)


def addition_and_multiplication(answer):
    result = None
    numbers = []
    list_len = int(input("Na ilu elementach chcesz przeprowadzić działanie: "))
    for i in range(list_len):
        number = check_number(i + 1)
        numbers.append(number)
    numbers_to_show = ", ".join(map(str, numbers))
    if answer == "1":
        logging.debug(f"Sumuję liczby {numbers_to_show}")
        result = round(sum(numbers), 2)
    else:
        logging.debug(f"Mnożę liczby {numbers_to_show}")
        result = 1
        for number in numbers:
            result *= number
        result = round(result, 2)
    print(f"Wynik to: {result}")


def subtraction_and_division(answer):
    result = None
    first_number = check_number(1)
    second_number = check_number(2)
    if answer == "2":
        logging.debug(f"Odejmuję {first_number} od {second_number}")
        result = round(first_number - second_number, 2)
    else:
        if second_number == 0:
            logging.debug("Nie dziel przez 0 ty... :)")
        else:
            logging.debug(f"Dzielę {first_number} od {second_number}")
            result = round(first_number / second_number, 2)
    print(f"Wynik to: {result}")


if __name__ == "__main__":
    answer = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "
    )
    if answer == "1" or answer == "3":
        addition_and_multiplication(answer)
    elif answer == "2" or answer == "4":
        subtraction_and_division(answer)
    else:
        logging.debug("Podano niedozwoloną wartość")
