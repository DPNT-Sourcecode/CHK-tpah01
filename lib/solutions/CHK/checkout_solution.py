

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
}

def checkout(skus):
    basket = {"A": 0,
              "B": 0,
              "C": 0,
              "D": 0}
    total = 0

    for char in skus:
        if char not in basket:
            return -1
        basket[char] += 1
    
    for sku in basket:
        amount = basket[sku]
        if sku in OFFERS:
            # offer calculation
        else:
            total += PRICES[sku] * amount



