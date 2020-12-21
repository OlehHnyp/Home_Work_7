def solution(number):
    numbers_sum = 0
    if number <= 0:
        return numbers_sum
    for el in range(1, number):
        if not el % 3:
            numbers_sum += el
        elif not el % 5:
            numbers_sum += el
    return numbers_sum