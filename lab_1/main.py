# 6. Напишите функцию, принимающую от 1 до 3 параметров целых
# чисел (как стандартная функция range). Единственный обязательный аргумент -
# последнее число. Если поданы 2 аргумента, то первый интерпретируется как
# начальное число, второй, как конечное (не включительно). Если поданы 3
# аргумента, то третий аргумент интерпретируется как шаг. Функция должна
# выдавать один из следующих списков: квадратов чисел; кубов чисел; квадратных
# корней чисел; логарифмов чисел.
import math


def generate_list(*args) -> list:
    functions = {
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3,
        'square_root': lambda x: math.sqrt(x),
        'logarithm': lambda x: math.log(x),
    }

    if len(args) == 3:
        start, end, step = args

    elif len(args) == 2:
        start, end = args
        step = 1
    elif len(args) == 1:
        end = args[0]
        start = 0
        step = 1

    else:
        raise ValueError("Функция должна принимать от 1 до 3 аргументов")

    result = []
    choice = input('введите одно из названий функций: square, cube, square_root, logarithm: ')
    if choice not in functions:
        raise KeyError("некорректно введено название функции")

    for num in range(start, end, step):
        # print(num)
        result.append(functions[choice](num))

    return result


print(generate_list(1, 5, 1))
