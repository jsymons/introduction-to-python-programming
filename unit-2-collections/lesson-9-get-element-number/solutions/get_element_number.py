def get_element_number(a_list, search_term):
    count = 0
    for item in a_list:
        if item == search_term:
            return count
        count += 1
    return 'no match'
