class BurgerData:
    BUN_NAME = 'black bun'
    BUN_PRICE = 100

    SAUCE_NAME = 'hot sauce'
    SAUCE_PRICE = 50

    FILLING_NAME = 'cutlet'
    FILLING_PRICE = 80

    RECEIPT_WITH_INGREDIENTS = (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '(==== black bun ====)\n'
        '\n'
        'Price: 330'
    )

    RECEIPT_WITHOUT_INGREDIENTS = (
        '(==== black bun ====)\n'
        '(==== black bun ====)\n'
        '\n'
        'Price: 200'
    )