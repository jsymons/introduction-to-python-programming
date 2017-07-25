def common_values(list_1, list_2):
    if isinstance(list_1, list) and isinstance(list_2, list):
        return set(list_1).intersection(set(list_2))
    return "Params not of type 'list'"