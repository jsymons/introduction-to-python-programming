def analyze_age_in_dicts(list_of_dicts):
    temp_list = []
    for current_dict in list_of_dicts:
        if 'age' in current_dict:
            temp_list.append(current_dict["age"])

    count = len(temp_list)
    total = sum(temp_list)

    return {
        'dictionary_count': count,
        'avg_age': total / count
    }
