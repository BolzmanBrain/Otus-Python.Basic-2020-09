"""
Домашнее задание №1
Функции и структуры данных
"""
import math


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n ** 2 for n in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    """
    функция-тест на простоту числа
    """
    if number == 2:
        return True
    check_boundary = math.ceil(math.sqrt(number)) + 1
    for i in range(2,check_boundary):
        if number % i == 0:
            return False
    return True



def filter_numbers(num_list,filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1,num_list))
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0,num_list))
    if filter_type == PRIME:
        return list(filter(is_prime,num_list))
