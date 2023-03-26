def join(*lists, sep = '-'):
    if not lists:
        return None
    new_list = []
    for arr in lists:
        new_list += arr
        new_list += sep
    new_list.pop()
    print(new_list)
    return 0

