"""
На вход подается список чисел и целевое число на отдельной строке. Верните индексы двух чисел, которые в сумме дают целевое число.
Любые входные данные имеют только 1 решение и один и тот же элемент списка не нужно использовать дважды.
Индексы можно вернуть в любом порядке.

Sample Input:
2,7,11,15
9

Sample Output:
[0, 1]
"""

"""def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        result = target - num
        if result in num_to_index:
            return [num_to_index[result], index]
        num_to_index[num] = index
x = input()
y = int(input())
nums = list(map(int, x.split(',')))
res = two_sum(nums, y)
print(res)"""
"""
Напишите программу, которая находит самый длинный общий префикс для строк находящихся в списке строк

Sample Input:

flower,flow,flight
Sample Output:

fl
"""
import os
# s = input().split(',')
# print(os.path.commonprefix(s))
def larger_pref(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words:
        while words[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        if not prefix:
            break
    return prefix

def is_palindrome(number):
    # Преобразуем число в строку
    num_str = str(number)
    # Сравниваем строку с её обратной версией
    return num_str == num_str[::-1]
# res = is_palindrome(121)
# if is_palindrome(x):
#     print(True)
# else:
#     print(False)
