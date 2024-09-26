def key_params(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, tuple, set, str, dict)):
            new_dict[str(value)] = key
        else:
            new_dict[value] = key

    return new_dict
