

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
"A":50,
"B":30,
"C":20,
"D":15,
"E":40,
"F":10,
"G":20,
"H":10,
"I":35,
"J":60,
"K":70,
"L":90,
"M":15,
"N":40,
"O":10,
"P":50,
"Q":30,
"R":50,
"S":20,
"T":20,
"U":40,
"V":50,
"W":20,
"X":17,
"Y":20,
"Z":21
}

# Apply free deals first
# Bulk deals second
# smaller bulk deals 3rd
# remaining amounts 4th

FREE_DEALS = {
    "E": (2, "B"),
    "F": (2, "F"),
    "N": (3, "M"),
    "R": (3, "Q"),
    "U": (3, "U")
}

BULK_DEALS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)]
}


def checkout(skus):
    basket = {}
    total = 0

    for char in skus:
        if char not in PRICES:
            return -1
        basket[char] = basket.get(char, 0) + 1
        
    # Adjust quantities based on free deals
    for deal_sku in FREE_DEALS.keys():
        if deal_sku not in basket:
            continue

        free_sku = FREE_DEALS[deal_sku][1]
        
        if free_sku not in basket:
            continue

        req_amount = FREE_DEALS[deal_sku][0]

        if free_sku == deal_sku:
            req_amount += 1
        
        n_applied = basket[deal_sku] // req_amount
        basket[free_sku] -= n_applied

        if basket[free_sku] < 0:
            basket[free_sku] = 0
    
    # Adjust quantities based on bulk deals
    for deal_sku in BULK_DEALS.keys():
        if deal_sku not in basket:
            continue

        # Go through deals in priority, add to total where possible
        for amount, cost in BULK_DEALS[deal_sku]:
            n_applied = basket[deal_sku] // amount
            total += n_applied * cost
            basket[deal_sku] -= n_applied * amount

            if basket[deal_sku] < 0:
                basket[deal_sku] = 0
    
    group = { "S", "T", "X", "Y", "Z" }
    
    while group_total(basket, group) >= 3:
        for _ in range(3):
            priority_remove(basket)
        total += 45
    
    # Calculate remaining amounts
    for sku in basket:
        total += basket[sku] * PRICES[sku]

    return total

def group_total(basket, group):
    total = 0
    for sku in group:
        total += basket.get(sku, 0)
    return total

PRIORITY = ["Z", "S", "T", "Y", "X"]

def priority_remove(basket):
    not_removed = True
    i = 0

    while not_removed:
        amount = basket.get(PRIORITY[i], 0)
        if amount <= 0:
            i += 1
        else:
            basket[PRIORITY[i]] -= 1
            not_removed = False   

print(checkout("ZSTYX"))

