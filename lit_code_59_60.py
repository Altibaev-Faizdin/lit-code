# Tasks 59-60 solutions for lit-code
# Author: added by Copilot helper

#59. Two Sum - LeetCode
# Задача: Найти индексы двух чисел в массиве, которые в сумме дают заданное значение target.
# Решение: Используем хэш-таблицу (словарь) для хранения уже просмотренных чисел и их индексов.

def two_sum(nums, target):
    """
    :param nums: list[int]
    :param target: int
    :return: tuple(int, int) - индексы двух чисел, которые дают target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

# Примеры:
# print(two_sum([2,7,11,15], 9))  # (0, 1)
# print(two_sum([3,2,4], 6))      # (1, 2)
# print(two_sum([3,3], 6))        # (0, 1)


#60. Plus One
# Задача: Увеличит�� число, представленного массивом цифр, на единицу.
# Решение: Проходим справа налево, увеличиваем цифру, обрабатываем перенос (carry).

def plus_one(digits):
    """
    :param digits: list[int] - каждая цифра от 0 до 9, старшие цифры слева
    :return: list[int] - новый список цифр после прибавления 1
    """
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        new_val = digits[i] + carry
        digits[i] = new_val % 10
        carry = new_val // 10
        if carry == 0:
            break
    if carry:
        return [carry] + digits
    return digits

# Примеры:
# print(plus_one([1,2,3]))  # [1,2,4]
# print(plus_one([4,3,2,1])) # [4,3,2,2]
# print(plus_one([9]))       # [1,0]
# print(plus_one([9,9,9]))   # [1,0,0,0]
