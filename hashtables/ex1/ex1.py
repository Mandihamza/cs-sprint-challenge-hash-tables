def get_indices_of_item_weights(weights, length, limit):
    num_pairs_dict = {}
    for index, value in enumerate(weights):
        if value in num_pairs_dict:
            tuple_list = tuple([num_pairs_dict[value], index])
            min_value = min(tuple_list)
            max_value = max(tuple_list)
            return max_value, min_value
        num_pairs_dict[limit - value] = index
    return None
