#100 Days of Code - Python lit code
# Day 1


#1. Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0] == 'R' or name[0] == 'r':
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"

# print(are_you_playing_banjo('Ringo'))
# print(are_you_playing_banjo('roman'))
# print(are_you_playing_banjo('Aziz'))



#2. Open or Senior?

# users = [
#     [18, 20],
#     [45, 2],
#     [61, 12],
# ]

# def open_or_senior(data):
#     result = []
#     for age, handicap in data:
#         if age >= 55 and handicap > 7:
#             result.append('Senior')
#         else:
#             result.append('Open')
#     return result

# print(open_or_senior(users))


#3. Lasagna Oven
# EXPECTED_BAKE_TIME = 40
# def bake_time_remaining(elapsed_bake_time):
#     return EXPECTED_BAKE_TIME - elapsed_bake_time

# def preparation_time_in_minutes(number_of_layers):
#     """Calculate the preparation time in minutes.

#     :param number_of_layers: int - number of layers in the lasagna.
#     :return: int - preparation time in minutes.
#     """
#     return number_of_layers * 2

# def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
#     """Calculate the elapsed time in minutes.

#     :param number_of_layers: int - number of layers in the lasagna.
#     :param elapsed_bake_time: int - elapsed time in minutes.
#     :return: int - elapsed time in minutes.
#     """
#     return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time




#4. Reverse Words

# def reverse_words(text):
#     return ' '.join(word[::-1] for word in text.split(' '))

# print(reverse_words("This is an example!"))
# print(reverse_words("double  spaces"))



#5. Sentence Smash
# def smash(words):   
#     return ' '.join(words)

# print(smash(["hello", "world", "this", "is", "test"]))
# print(smash(["hello"]))
# print(smash([]))



#6. Pac-Man Game

# def eat_ghost(power_pellet_active, touching_ghost):
#     if power_pellet_active and touching_ghost:
#         return True
#     else:
#         return False

# def score(touching_power_pellet, touching_dot):
#     if touching_power_pellet or touching_dot:
#         return True
#     else:
#         return False

# def lose(power_pellet_active, touching_ghost):     
#     if not power_pellet_active and touching_ghost:
#         return True
#     else:
#         return False

# def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
#     if has_eaten_all_dots and  touching_ghost:
#         return True
#     else:
#         return False

# print(eat_ghost(True, True))




#7. Counting Sheeps

# def count_sheeps(sheep): 
#     return sheep.count(True)

# print(count_sheeps([True, True, True, False,
#                     True, True, True, True,
#                     True, False, True, False,
#                     True, False, False, True,
#                     True, True, True, True,
#                     False, False, True, True]))


#8. XO

# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')

# print(xo("xo"))
# print(xo("xo0"))
# print(xo("xxxoo"))
# print(xo("xxo"))
# print(xo("ooxx"))
# print(xo("ooxXm"))
# print(xo("zpzpzpp"))
# print(xo("zzoo"))



#9. Basic-Operator

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
#     else:
#         return "Invalid operator"

# print(basic_op('+', 4, 7))
# print(basic_op('-', 15, 18))
# print(basic_op('*', 5, 5))
# print(basic_op('/', 49, 7))




#10 Disemvowel

# def disemvowel(string):
#     vowels = "aeiouAEIOU"
#     result = ""

#     for char in string:
#         if char not in vowels:
#             result += char

#     return result
# print(disemvowel("This website is for losers LOL!"))




#11 Even or Old

# def even_or_old(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Old"

# print(even_or_old(2))   
# print(even_or_old(7))   
# print(even_or_old(10))  
# print(even_or_old(15))  



#12. Square 

# def square_digits(num):
#     result = ""

#     for digit in str(num):
#         result += str(int(digit) ** 2)

#     return int(result)

# square_digits(9119)  
# square_digits(765)   
# square_digits(0)     




#13. Jaden Case

#def to_jaden_case(string):
#    words = string.split()
    
#    result = []

#    for word in words:
#        result.append(word.capitalize())

#    return " ".join(result)

#print(to_jaden_case("hello world"))
#print(to_jaden_case("most trees are blue"))
#print(to_jaden_case("aren't you serious"))



#14. Make Negative 

#def make_negative(num):
#    if num > 0:
#        return -num
#    return num


#print(make_negative(1))    
#print(make_negative(-5))   
#print(make_negative(0))    
#print(make_negative(42))   




#15. Find Smallest

# def find_smallest_int(arr):
#     smallest = arr[0]

#     for num in arr:
#         if num < smallest:
#             smallest = num
    
#     return smallest


# print(find_smallest_int([34, 15, 88, 2]))
# print(find_smallest_int([34, -345, -1, 100]))


#16. Row Odd

# def row_sum_odd_numbers(n):
#     return n ** 3 

# print(row_sum_odd_numbers(1))  
# print(row_sum_odd_numbers(2))  
# print(row_sum_odd_numbers(3))  
# print(row_sum_odd_numbers(4))  
# print(row_sum_odd_numbers(5))  




#17. No space

#def no_space(x):
#    return x.replace(" ", "")




#18. String to Number

#def string_to_number(s):
#    return int(s)
#print(string_to_number("1234"))
#
#print(string_to_number("605"))
#
#print(string_to_number("-7"))



#19. Friend Name

# def friend(names):
#     result = []

#     for name in names:
#         if len(name) == 4:
#             result.append(name)

#     return result




#20.
# def find_needle(haystack):
#     index = haystack.index("needle")
#     return "found the needle at position " + str(index)

# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))




#21. Find the next perfect square

# def find_next_square(sq):
#     root = int(sq ** 0.5)

#     if root * root != sq:
#         return -1

#     return (root + 1) ** 2

# print(find_next_square(121))
# print(find_next_square(625))
# print(find_next_square(114))




#22. Population Growth

# def nb_year(p0, percent, aug, p):
#     years = 0
#     while p0 < p:
#         p0 = int(p0 + p0 * percent / 100 + aug)
#         years += 1
#     return years

# print(nb_year(1500, 5, 100, 5000))
# print(nb_year(1500000, 2.5, 10000, 2000000))
# print(nb_year(1500000, 0.25, 1000, 2000000))
# print(nb_year(1500000, 0.25, 1000, 2000000))
# print(nb_year(1500000, 0.25, 1000, 2000000))




#23. Printer Errors

# def printer_error(s):
#     errors = 0

#     for char in s:
#         if char > 'm':
#             errors += 1

#     return f"{errors}/{len(s)}"

# print(printer_error("aaabbbbhaijjjm"))
# print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))




#24. Repeat String

# def repeat_str(repeat, string):
#     return string * repeat

# print(repeat_str(4, "a"))
# print(repeat_str(3, "hello "))
# print(repeat_str(2, "abc"))




#25. Two to One

# def longest(a1, a2):
#     return ''.join(sorted(set(a1 + a2)))

# print(longest("aretheyhere", "yestheyarehere"))
# print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
# print(longest("inmanylanguages", "theresapairoffunctions"))




#26. Remove exclamation

# def remove_exclamation_marks(s):
#     return s.replace("!", "")

# print(remove_exclamation_marks("Hello World!"))
# print(remove_exclamation_marks("Hello World!!!"))
# print(remove_exclamation_marks("Hello World!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!!!!!!!!!!!!"))
# print(remove_exclamation_marks("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!"))




#30. Get Volume of Cuboid

# def get_volume_of_cuboid(length, width, height):
#     return length * width * height

# print(get_volume_of_cuboid(1, 2, 2))
# print(get_volume_of_cuboid(6.3, 2, 5))




#31. Simple Multiplication

# def simple_multiplication(number):
#     if number % 2 == 0:
#         return number * 8
#     else:
#         return number * 9

# print(simple_multiplication(2))
# print(simple_multiplication(3))




#31. Odd or Even

# def odd_or_even(arr):
#     if sum(arr) % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(odd_or_even([0, 1, 2]))
# print(odd_or_even([0, 1, 3]))




#32. String ends with

# def solution(text, ending):
#     return text.endswith(ending)

# print(solution("abc", "bc"))
# print(solution("abc", "d"))




#33. Boolean to String

# def bool_to_word(b):
#     return "Yes" if b else "No"

# print(bool_to_word(True))
# print(bool_to_word(False))




#34. Double Integer

# def double_integer(i):
#     return i * 2

# print(double_integer(2))
# print(double_integer(10))


#35. Pangram 

# def is_pangram(sentence):
#     return False if len(set(filter(str.isalpha, sentence.lower()))) < 26 else True

# print(is_pangram("The quick brown fox jumps over the lazy dog."))



#36. Add Binary 

# def add_binary(a, b):
#     return bin(a + b)[2:]

# print(add_binary(1, 1))
# print(add_binary(0, 1))
# print(add_binary(1, 0))



#37. Square Every Digit

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

# print(square_sum([1, 2]))
# print(square_sum([0, 3, 4, 5]))
# print(square_sum([-3, 4]))




#38. Duplicate Encoder

# def duplicate_encode(word):
#     word = word.lower()
#     return ''.join(')' if word.count(char) > 1 else '(' for char in word)


# def dublicate_encode(word):
#     return duplicate_encode(word)


# print(duplicate_encode("din"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("Success"))
# print(duplicate_encode("(( @"))



#39. Tribonacci Sequence

#def tribonacci(signature, n):
#    if n == 0:
#        return []
#    elif n == 1:
#        return [signature[0]]
#    elif n == 2:
#        return signature[:2]
#    elif n == 3:
#        return signature
#    
#    trib = signature[:]
#    for i in range(3, n):
#        trib.append(trib[i-1] + trib[i-2] + trib[i-3])
#    
#    return trib

#print(tribonacci([1, 1, 1], 10))
#print(tribonacci([0, 0, 1], 10))
#print(tribonacci([0, 1, 1], 10))
#print(tribonacci([1, 0, 0], 10))
#print(tribonacci([0, 0, 0], 10))
#print(tribonacci([1, 2, 3], 10))
#print(tribonacci([3, 2, 1], 10))
#print(tribonacci([1, 1, 1], 1))
#print(tribonacci([1, 1, 1], 2))
#print(tribonacci([1, 1, 1], 3))
#print(tribonacci([1, 1, 1], 4))
#print(tribonacci([1, 1, 1], 5))
#print(tribonacci([1, 1, 1], 6))
#print(tribonacci([1, 1, 1], 7))
#print(tribonacci([1, 1, 1], 8))
#print(tribonacci([1, 1, 1], 9))
#print(tribonacci([1, 1, 1], 10))


#40. Rental Car

# def rental_car_cost(d):
#     return d * 40 - (d > 2) * 20 - (d > 6) * 30
    
# print(rental_car_cost(1))
# print(rental_car_cost(4))
# print(rental_car_cost(7))
# print(rental_car_cost(8))



#41. Opposite Number

# def opposite(number):
#     return -number
    
# print(opposite(1))
# print(opposite(-1))
# print(opposite(0))
# print(opposite(5))
# print(opposite(-5))



#42. Replace With Alphabet Position

# def alphabet_position(text):
#     return ' '.join(str(ord(char) - 96) for char in text.lower() if char.isalpha())

# print(alphabet_position("The sunset sets at twelve o' clock."))
# print(alphabet_position("The narwhal bacons at midnight."))



#43. Highest and Lowest

# def high_and_low(numbers):
#     nums = [int(x) for x in numbers.split()]
#     return f"{max(nums)} {min(nums)}"

# print(high_and_low("1 2 3 4 5"))
# print(high_and_low("1 2 -3 4 5"))
# print(high_and_low("1 2 3 4 -5"))



#44. Convert a Number to a String!

# def past(h, m, s):
#     return (h * 3600 + m * 60 + s) * 1000

# print(past(0, 1, 1))
# print(past(1, 1, 1))
# print(past(0, 0, 0))
# print(past(1, 0, 1))
# print(past(1, 0, 0))


#45. Number of People in the Bus

# def number(bus_stops):
#     return sum(on - off for on, off in bus_stops)

# print(number([[10,0],[3,5],[5,8]]))
# print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
# print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))



#46. Count Smileys  

# def count_smileys(arr):
#     return sum(1 for i in arr if i in [':)', ':D', ';)', ';D', ':-)', ':-D', ';-)', ';-D', ':~)', ':~D', ';~)', ';~D'])


#47. Mumbling

# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# print(likes([]))
# print(likes(["Peter"]))
# print(likes(["Jacob", "Alex"]))
# print(likes(["Max", "John", "Mark"]))
# print(likes(["Alex", "Jacob", "Mark", "Max"]))




#48. Count characters in your string

# def count_by(s):
#     result = {}
#     for char in s:
#         result[char] = result.get(char, 0) + 1
#     return result


# #49. Find Nth Digit - Day 20

# # Задача: Найти N-тый символ (цифру) в последовательности 123456789101112131415...

# def find_nth_digit(n):
#     """
#     Находит N-тый символ в последовательности 123456789101112131415...
    
#     :param n: int - позиция символа (начиная с 1)
#     :return: int - N-тый символ (цифра)
#     """
#     digits = 1  # количество цифр в числе (1 для чисел 1-9, 2 для 10-99, и т.д.)
#     count = 9  # количество чисел с 'digits' цифрами
#     start = 1  # первое число с 'digits' цифрами
    
#     # Пропускаем все числа пока не найдём нужный диапазон
#     while n > digits * count:
#         n -= digits * count
#         digits += 1
#         count *= 10
#         start *= 10
    
#     # Находим нужное число
#     num = start + (n - 1) // digits
    
#     # Находим нужную цифру в этом числе
#     digit_index = (n - 1) % digits
    
#     return int(str(num)[digit_index])


# # Примеры использования:
# # print(find_nth_digit(3))    # 3
# # print(find_nth_digit(10))   # 1 (первая цифра числа 10)
# # print(find_nth_digit(11))   # 0 (вторая цифра числа 10)
# # print(find_nth_digit(12))   # 1 (первая цифра числа 11)
# # print(find_nth_digit(190))  # 3 (цифра в большей позиции)


# #50. Is Valid Parentheses - Day 20

# # Задача: Проверить, правильно ли расставлены скобки

# def is_valid_parentheses(s):
#     """
#     Провер��ет, правильно ли расставлены круглые скобки в строке.
    
#     :param s: str - строка со скобками
#     :return: bool - True если скобки правильно расставлены, False иначе
#     """
#     count = 0
    
#     for char in s:
#         if char == '(':
#             count += 1
#         elif char == ')':
#             count -= 1
        
#         # Если в какой-то момент больше закрывающих скобок
#         if count < 0:
#             return False
    
#     # В конце count должен быть 0
#     return count == 0


# Примеры использования:
# print(is_valid_parentheses("()"))          # True
# print(is_valid_parentheses("(())"))        # True
# print(is_valid_parentheses("()()"))        # True
# print(is_valid_parentheses("("))           # False
# print(is_valid_parentheses(")"))           # False
# print(is_valid_parentheses("(("))          # False
# print(is_valid_parentheses("())"))         # False
# print(is_valid_parentheses("(()())"))      # True

# #49. Find Nth Digit - Day 20

# # Задача: Найти N-тый символ (цифру) в последовательности 123456789101112131415...

# def find_nth_digit(n):
#     """
#     Находит N-тый символ в последовательности 123456789101112131415...
    
#     :param n: int - позиция символа (начиная с 1)
#     :return: int - N-тый символ (цифра)
#     """
#     digits = 1  # количество цифр в числе (1 для чисел 1-9, 2 для 10-99, и т.д.)
#     count = 9  # количество чисел с 'digits' цифрами
#     start = 1  # первое число с 'digits' цифрами
    
#     # Пропускаем все числа пока не найдём нужный диапазон
#     while n > digits * count:
#         n -= digits * count
#         digits += 1
#         count *= 10
#         start *= 10
    
#     # Находим нужное число
#     num = start + (n - 1) // digits
    
#     # Находим нужную цифру в этом числе
#     digit_index = (n - 1) % digits
    
#     return int(str(num)[digit_index])


# # Примеры использования:
# # print(find_nth_digit(3))    # 3
# # print(find_nth_digit(10))   # 1 (первая цифра числа 10)
# # print(find_nth_digit(11))   # 0 (вторая цифра числа 10)
# # print(find_nth_digit(12))   # 1 (первая цифра числа 11)
# # print(find_nth_digit(190))  # 3 (цифра в большей позиции)


# #50. Is Valid Parentheses - Day 20

# # Задача: Проверить, правильно ли расставлены скобки

# def is_valid_parentheses(s):
#     """
#     Проверяет, правильно ли расставлены круглые скобки в строке.
    
#     :param s: str - строка со скобками
#     :return: bool - True если скобки правильно расставлены, False иначе
#     """
#     count = 0
    
#     for char in s:
#         if char == '(':
#             count += 1
#         elif char == ')':
#             count -= 1
        
#         # Если в какой-то момент больше закрывающих скобок
#         if count < 0:
#             return False
    
#     # В конце count должен быть 0
#     return count == 0


# # Примеры использования:
# # print(is_valid_parentheses("()"))          # True
# # print(is_valid_parentheses("(())"))        # True
# # print(is_valid_parentheses("()()"))        # True
# # print(is_valid_parentheses("("))           # False
# # print(is_valid_parentheses(")"))           # False
# # print(is_valid_parentheses("(("))          # False
# # print(is_valid_parentheses("())"))         # False
# # print(is_valid_parentheses("(()())"))      # True



#51. Number Lines

# def number(lines):
#     return [f"{i+1}: {line}" for i, line in enumerate(lines)]

# print(number(["a", "b", "c"]))



#52. Sum of odd numbers

# def series_sum(n):
#     total = 0
#     for i in range(n):
#         total += 1 / (1 + 3 * i)
#     return f"{total:.2f}"
# print(series_sum(0))  
# print(series_sum(1))  
# print(series_sum(2))  
# print(series_sum(3))  
# print(series_sum(5))  




#53. Get Grade

# def get_grade(s1, s2, s3):
#     avg = (s1 + s2 + s3) / 3
#     if avg >= 90:
#         return 'A'
#     elif avg >= 80:
#         return 'B'
#     elif avg >= 70:
#         return 'C'
#     elif avg >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(get_grade(95, 90, 93))  
# print(get_grade(85, 80, 87))  
# print(get_grade(75, 70, 73))  
# print(get_grade(65, 60, 63))  
# print(get_grade(55, 50, 53))  




#54. Longest Consecutive

# def longest_consec(strarr, k):
#     if k <= 0 or k > len(strarr):
#         return ""
    
#     max_str = ""
#     for i in range(len(strarr) - k + 1):
#         current_str = ''.join(strarr[i:i+k])
#         if len(current_str) > len(max_str):
#             max_str = current_str
    
#     return max_str


# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

# print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))

# print(longest_consec([], 3))

# print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15))



#55. Jump Game - LeetCode

# Задача: Определить, можно ли достичь последнего индекса массива
# Каждый элемент представляет максимальную длину прыжка с этой позиции

# def canJump(nums):
#     """
#     Определяет, можно ли достичь последнего индекса массива
    
#     :param nums: list - массив целых чисел (максимальная длина прыжка)
#     :return: bool - True если можно достичь конца, False иначе
#     """
#     max_reach = 0
#     for i, jump in enumerate(nums):
#         if i > max_reach:
#             return False
#         max_reach = max(max_reach, i + jump)
#         if max_reach >= len(nums) - 1:
#             return True
#     return True




#56. Merge Intervals - LeetCode

# Задача: Объединить перекрывающиеся интервалы
# Дан массив интервалов, вернуть массив неперекрывающихся интервалов

# def merge(intervals):
#     """
#     Объединяет все перекрывающиеся интервалы
    
#     :param intervals: list - список интервалов [[start, end], ...]
#     :return: list - список объединённых интервалов
#     """
#     if not intervals:
#         return []

#     # Сортируем интервалы по началу
#     intervals.sort(key=lambda x: x[0])
#     merged = [intervals[0]]

#     for current in intervals[1:]:
#         last = merged[-1]
#         if current[0] <= last[1]:  # Есть перекрытие
#             last[1] = max(last[1], current[1])
#         else:
#             merged.append(current)
#     return merged




#57. Best Time to Buy and Sell Stock - LeetCode

# Задача:
# Дан массив цен акций.
# Нужно купить один раз и продать один раз,
# чтобы получить максимальную прибыль.

# def maxProfit(prices):
#     """
#     Возвращает максимальную прибыль.

#     :param prices: list[int]
#     :return: int
#     """

#     min_price = float("inf")
#     profit = 0

#     for price in prices:

#         # Запоминаем минимальную цену
#         if price < min_price:
#             min_price = price

#         # Считаем максимальную прибыль
#         profit = max(profit, price - min_price)

#     return profit




#58. Valid Anagram - LeetCode

# Задача:
# Проверить, являются ли две строки анаграммами.

# def isAnagram(s, t):
#     """
#     Проверяет являются ли строки анаграммами.

#     :param s: str
#     :param t: str
#     :return: bool
#     """

#     return sorted(s) == sorted(t)








#59. Two Sum - LeetCode

# Задача:
# Найти индексы двух чисел,
# сумма которых равна target.

# def twoSum(nums, target):
#     """
#     Возвращает индексы двух чисел.

#     :param nums: list[int]
#     :param target: int
#     :return: list[int]
#     """

#     seen = {}

#     for i, num in enumerate(nums):

#         diff = target - num

#         if diff in seen:
#             return [seen[diff], i]

#         seen[num] = i







#60. Contains Duplicate - LeetCode

# Задача:
# Проверить есть ли одинаковые элементы.

# def containsDuplicate(nums):
#     """
#     Проверяет наличие повторений.

#     :param nums: list[int]
#     :return: bool
#     """

#     return len(nums) != len(set(nums))








#61. Valid Palindrome - LeetCode

# Задача:
# Проверить является ли строка палиндромом.
# def isPalindrome(s):
#     """
#     Проверяет палиндром.

#     :param s: str
#     :return: bool
#     """

#     cleaned = ""

#     for char in s.lower():
#         if char.isalnum():
#             cleaned += char

#     return cleaned == cleaned[::-1]






#62. Maximum Subarray - LeetCode

# Задача:
# Найти максимальную сумму непрерывного подмассива.
# def maxSubArray(nums):
#     """
#     Алгоритм Кадане.

#     :param nums: list[int]
#     :return: int
#     """

#     current = nums[0]
#     best = nums[0]

#     for num in nums[1:]:

#         current = max(num, current + num)
#         best = max(best, current)

#     return best





#63. Binary Search - LeetCode

# Задача:
# Найти индекс элемента в отсортированном массиве.

# def search(nums, target):
#     """
#     Бинарный поиск.

#     :param nums: list[int]
#     :param target: int
#     :return: int
#     """

#     left = 0
#     right = len(nums) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid

#         elif nums[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return -1

# print(search([-1,0,3,5,9,12],9))    # 4
# print(search([-1,0,3,5,9,12],2))    # -1





#64. Two Sum

# def two_sum(numbers, target):
#     seen = {}
    
#     for i, num in enumerate(numbers):
#         diff = target - num
        
#         if diff in seen:
#             return [seen[diff], i]
        
#         seen[num] = i
    
#     return []

# print(two_sum([2,7,11,15], 9))  
# print(two_sum([3,2,4], 6))      
# print(two_sum([3,3], 6))        




#65. Find the odd int

# def find_it(seq):
#     for num in seq:
#         if seq.count(num) % 2 == 1:
#             return num
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))





#66. Find ODD

#def find_odd(numbers):
#    counts = {}

#    for number in numbers:
#        counts[number] = counts.get(number, 0) + 1

#    for number, count in counts.items():
#        if count % 2 != 0:
#            return number

#print(find_odd([1, 1, 2]))
#print(find_odd([1, 2, 2, 3, 3, 3]))




#67. Array.diff

#def array_diff(a, b):
#    return [x for x in a if x not in b]
    
#print(array_diff([1,2], [1]))  
#print(array_diff([1,2,2], [1]))  
#print(array_diff([1,2,2], [2]))  
#print(array_diff([1,2,2], []))  
#print(array_diff([], [1,2]))  



#68. Breaking chocolate problem

#def bouncing_ball(h, bounce, window):
#    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
#        return -1
#    
#    count = 1
#    h *= bounce
#
#   while h > window:
#        count += 2
#        h *= bounce
#    
#    return count
#
#print(bouncing_ball(3, 0.66, 1.5))  
#print(bouncing_ball(30, 0.66, 1.5))  
#print(bouncing_ball(30, 0.75, 1.5))  
#print(bouncing_ball(30, 0.4, 10))  
#print(bouncing_ball(40, 1, 10))  
#print(bouncing_ball(-5, 0.66, 1.5)) 





#69. Climb - Solution 

#class Solution:
#    def climbStairs(self, n: int) -> int:
#        a, b = 1, 1

#        for _ in range(n):
#            a, b = b, a + b

#        return a





#70. MySqrt

#class Solution:
#    def mySqrt(self, x: int) -> int:
#        left = 0
#        right = x
#
#        while left <= right:
#            mid = (left + right) // 2
#
#            if mid * mid == x:
#                return mid
#
#            if mid * mid < x:
#                left = mid + 1
#            else:
#                right = mid - 1
#
#        return right





#71. Your order, please

# def order(sentence):
#     if sentence == "":
#         return ""

#     words = sentence.split()
#     result = [""] * len(words)

#     for word in words:
#         for char in word:
#             if char.isdigit():
#                 number = int(char)
#                 result[number - 1] = word

#     return " ".join(result)

# print(order("is2 Thi1s T4est 3a"))
# print(order("4of Fo1r pe6ople g3ood th5e the2"))
# print(order(""))
# print(order("1"))
# print(order("2be3or not4 to1 be5"))



#71. Check for factor

# def check_for_factor(base, factor):
#     return base % factor == 0
    
# print(check_for_factor(10, 2))



#72. Sum without highest and lowest number

# def sum_array(arr):
#     if arr is None or len(arr) < 3:
#         return 0
#     return sum(arr) - min(arr) - max(arr)
    
# print(sum_array([6, 2, 1, 8, 10]))
# print(sum_array([1, 1, 11, 2, 3]))
# print(sum_array([]))
# print(sum_array([3]))
# print(sum_array([3, 5]))
# print(sum_array([6, 2, 1, 8, 10]))
# print(sum_array([-6, -20, -1, -10, -12]))
# print(sum_array([-6, 20, -1, 10, -12]))



#73.

#def filter_list(l):
#    return [x for x in l if isinstance(x, int)]
    
#print(filter_list([1, 2, 'a', 'b']))
#print(filter_list([1, 'a', 'b', 0, 15]))
#print(filter_list([1, 2, 'aasf', '1', '123', 123]))
    
    
    
    
    
    
    
    
#74. Trap

#class Solution:
#    def trap(self, height: list[int]) -> int:
#        left = 0
#        right = len(height) - 1
#
#        left_max = 0
#        right_max = 0

#        water = 0
#
#        while left < right:
#            if height[left] < height[right]:

#                if height[left] >= left_max:
#                    left_max = height[left]
#                else:
#                    water += left_max - height[left]

#                left += 1

#            else:

#                if height[right] >= right_max:
#                    right_max = height[right]
#                else:
#                    water += right_max - height[right]
#                right -= 1
#
#        return water




#75. Larger

#class Solution:
#    def largestRectangleArea(self, h):
#        stack = []
#        ans = 0
#
#        for i, x in enumerate(h + [0]):
#            while stack and h[stack[-1]] > x:
#                height = h[stack.pop()]
#                left = stack[-1] if stack else -1
#                ans = max(ans, height * (i - left - 1))
#            stack.append(i)

#        return ans









#76. MiniStack
#class MinStack:
#    def __init__(self):
#        self.s = []

#    def push(self, x):
#        self.s.append((x, min(x, self.s[-1][1]) if self.s else x))

#    def pop(self):
#        self.s.pop()

#    def top(self):
#        return self.s[-1][0]

#    def getMin(self):
#        return self.s[-1][1]


#77. Binnary

# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)

# print(binary_array_to_number([0, 0, 0, 1]))
# print(binary_array_to_number([0, 0, 1, 0]))
# print(binary_array_to_number([0, 1, 0, 1]))
# print(binary_array_to_number([1, 0, 0, 1]))
# print(binary_array_to_number([0, 0, 1, 0]))
# print(binary_array_to_number([1, 0, 1, 0]))
# print(binary_array_to_number([1, 0, 0, 1]))
# print(binary_array_to_number([0, 0, 0, 0]))
# print(binary_array_to_number([1, 1, 1, 1]))
# print(binary_array_to_number([0, 1, 1, 0]))



#78. Hero

# def hero(bullets, dragons):
#     return bullets >= dragons * 2

# print(hero(10, 5))
# print(hero(7, 4))
# print(hero(4, 5))
# print(hero(100, 40))
# print(hero(1500, 751))
# print(hero(0, 1))
# print(hero(100, 40))
# print(hero(1500, 751))
# print(hero(0, 1))
# print(hero(100, 40))
# print(hero(1500, 751))
# print(hero(0, 1))





#79. Quarter

#def quarter(month):
#    return (month - 1) // 3 + 1




#80. Descending order

#def descending_order(n):
#    return int(''.join(sorted(str(n), reverse=True)))




#81. Double Char

# def double_char(s):
#     return ''.join(c * 2 for c in s)

# print(double_char("String"))





#82. BMI

# def bmi(weight, height):
#     bmi_value = weight / height ** 2
    
#     if bmi_value <= 18.5:
#         return "Underweight"
#     elif bmi_value <= 25.0:
#         return "Normal"
#     elif bmi_value <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"




#83. Comp

# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     return sorted(x * x for x in array1) == sorted(array2)




#84. Keep up the hoop

# def hoop_count(n):
     return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"
