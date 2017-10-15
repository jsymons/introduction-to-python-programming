def subtract_reversed(a_list):
    if len(a_list) == 0:
        return 0

    result = a_list[-1]
    index = 0
    new_list = a_list[:-1]
    new_list.reverse()
    while index < len(new_list):
        elem = new_list[index]
        result -= elem

        index += 1

    return result
