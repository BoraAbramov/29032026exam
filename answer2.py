


def find_median(numbers: list) -> float:
    """

    :param numbers: list of numbers
    :return: return the median
    """
    srt_n = sorted(numbers)
    if len(srt_n) % 2 == 0:
        st1 = srt_n[len(srt_n) // 2] + srt_n[len(srt_n) // 2 + 1]
        median = st1 / 2
        return median
    else:
        median = srt_n[len(srt_n) // 2]
        return median


print(find_median([7, 3, 6, 5, 9 ,3]))