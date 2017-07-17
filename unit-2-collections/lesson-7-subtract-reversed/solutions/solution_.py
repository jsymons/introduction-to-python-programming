def subtract_reversed(a_list):
    if len(a_list) == 0:
        return 0

    result = a_list[-1]
    index = 0
    while index < len(a_list) - 1:
        elem = a_list[index]
        result -= elem

        index += 1

    return result
