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


#8

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

print(xo("xo"))
print(xo("xo0"))
print(xo("xxxoo"))
print(xo("xxo"))
print(xo("ooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))