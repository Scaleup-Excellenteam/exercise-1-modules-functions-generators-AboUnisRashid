def get_recipe_price(prices, optionals = None, **ingredients):
    if optionals is None:
        optionals = []
    check = False
    price = 0
    for itemX in prices:
        for itemY in optionals:
            if itemX is itemY:
                check = True
                break
        if not check:
            value = ingredients[itemX]/100
            price += prices[itemX] * value
    print(int(price))
    return 0






