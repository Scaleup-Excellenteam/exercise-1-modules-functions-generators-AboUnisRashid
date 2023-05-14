def get_recipe_price(prices, optionals=None, **ingredients):
    optionals = optionals or []
    price = 0

    for ingredient, amount in ingredients.items():
        if ingredient in optionals:
            continue
        value = amount / 100
        price += prices[ingredient] * value

    return int(price)


def main():
    """
    The main function that executes the program logic.
    """
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    # Expected output: 44

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    # Expected output: 54

    print(get_recipe_price({}))
    # Expected output: 0
    return 0


if __name__ == '__main__':
    main()




