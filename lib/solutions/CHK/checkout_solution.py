

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
}

def checkout(skus):
    basket = {}
    total = 0

    for char in skus:
        if char not in PRICES:
            return -1
        basket[char] = basket.get(char, 0) + 1
    
    # apply E deals first
    # then B deals where possible

    # Apply bulk A deal first
    # then 2ndary A deal if possible
    
    return total

print(checkout("ABCD"))


