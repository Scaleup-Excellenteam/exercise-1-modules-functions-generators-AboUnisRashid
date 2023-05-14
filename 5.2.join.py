def join_lists(*lists, sep='-'):
    """
    Joins multiple lists into a single list using a separator.

    Args:
        *lists: Multiple lists to be joined.
        sep: Separator to be used between the items. Default is '-'.

    Returns:
        A list with the items from the input lists joined together.
    """
    joined_list = []

    for lst in lists:
        joined_list += lst
        if lst is not lists[-1]:
            joined_list += [sep]

    return str(joined_list)


def get_lists():
    """
    Asks the user for the number of lists to join and their contents.

    Returns:
        A list of lists entered by the user.
    """
    num_lists = int(input("Enter the number of lists to be joined: "))
    lists = []

    for i in range(num_lists):
        # Ask the user to enter a list and split the input string into a list of strings
        list_input = input(f"Enter list {i + 1}: ")
        list_items = list_input.split()

        # Convert each item in the list to an integer using a list comprehension
        list_ints = [int(item) for item in list_items]

        # Append the integer list to the list of lists
        lists.append(list_ints)

    return lists


def main():
    """
    The main function that executes the program logic.
    """
    res = get_lists()

    answer = input("Do you want a custom separator? (y/n): ")
    if answer == 'y':
        custom_sep = input("Enter a custom separator: ")
        result = join_lists(*res, sep=custom_sep)
    else:
        result = join_lists(*res)

    print(result)


if __name__ == '__main__':
    main()
