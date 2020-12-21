def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    else:
        positive_numbers = []
        negative_numbers = []
        for num in arr:
            if num < 0:
                negative_numbers.append(num)
            elif num > 0:
                positive_numbers.append(num)
    return [len(positive_numbers), sum(negative_numbers)]