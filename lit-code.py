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

