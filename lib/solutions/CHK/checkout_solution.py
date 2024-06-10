

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
        if amount == 0:
            continue

        if sku in OFFERS:
            offer_amount, offer_price = OFFERS[sku]
            times_offered = amount // offer_amount
            total += times_offered * offer_price
            print(times_offered, offer_amount)
            total += amount % (times_offered * offer_amount)
        else:
            total += PRICES[sku] * amount
    
    return total

print(checkout("AAAA"))





