# Solutions for LeetCode problems 57 and 58
# 57. Insert Interval
# 58. Length of Last Word

#57. Insert Interval
# Задача: дан список непересекающихся интервалов, отсортированных по началу,
# и новый интервал newInterval. Вставить новый интервал так, чтобы итоговый
# список оставался без пересечений (при необходимости объединить).

def insert_interval(intervals, newInterval):
    """
    Вставляет новый интервал в список и объединяет перекрывающиеся интервалы.

    :param intervals: list[list[int, int]] - список интервалов, отсортированный по началу
    :param newInterval: list[int, int] - новый интервал [start, end]
    :return: list[list[int, int]] - список объединённых интервалов
    """
    res = []
    i = 0
    n = len(intervals)
    new_start, new_end = newInterval

    # Добавляем все интервалы, которые находятся полностью слева от нового
    while i < n and intervals[i][1] < new_start:
        res.append(intervals[i])
        i += 1

    # Объединяем все пересекающиеся с новым
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1

    res.append([new_start, new_end])

    # Добавляем оставшиеся интервалы
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

# Примеры:
# print(insert_interval([[1,3],[6,9]], [2,5]))      # [[1,5],[6,9]]
# print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# # [[1,2],[3,10],[12,16]]


#58. Length of Last Word
# Задача: вернуть длину последнего слова в строке, слово — последовательность
# непробельных символов. Если слов нет — вернуть 0.

def length_of_last_word(s):
    """
    Возвращает длину последнего слова в строке s.

    :param s: str
    :return: int
    """
    # Убираем возможные пробелы справа, затем ищем последний фрагмент
    s = s.rstrip()
    if not s:
        return 0
    # Находим длину последнего слова, пробегая с конца
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

# Примеры:
# print(length_of_last_word("Hello World"))      # 5
# print(length_of_last_word("   fly me   to   the moon  "))  # 4
# print(length_of_last_word("luffy is still joyboy"))       # 6
