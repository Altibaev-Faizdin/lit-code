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






#17
def no_space(x):
    return x.replace("", "")

print(no_space("Hello World"))
print(no_space("a b c d"))
print(no_space("8aaaaa dddd r     "))