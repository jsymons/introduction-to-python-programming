def get_element_number(a_list, search_term):
    count = 0
    for item in a_list:
        if item == search_term:
            break
        count += 1
    else:
        return 'no match'
    return count
