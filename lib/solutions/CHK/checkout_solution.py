

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
"A": 50,
"B": 30,
"C": 20,
"D": 15,
"E": 40,
"F": 10,
"G": 20,
"H": 10,
"I": 35,
"J": 60,
"K": 80,
"L": 90,
"M": 15,
"N": 40,
"O": 10,
"P": 50,
"Q": 30,
"R": 50,
"S": 30,
"T": 20,
"U": 40,
"V": 50,
"W": 20,
"X": 90,
"Y": 10,
"Z": 50
}

# Apply free deals first
# Bulk deals second
# smaller bulk deals 3rd
# remaining amounts 4th

FREE_DEALS = {
    #SKU: (Required amount, FREE SKU)
    "E": (2, "B"),
    ""
}


def checkout(skus):
    basket = {}
    total = 0

    for char in skus:
        if char not in PRICES:
            return -1
        basket[char] = basket.get(char, 0) + 1
    

    
    # apply E deals first
    e_count = basket.get("E", 0)
    n_free_Bs = e_count // 2

    total += e_count * PRICES["E"]
    
    if "B" in basket:
        basket["B"] -= n_free_Bs
        basket["B"] = 0 if basket["B"] < 0 else basket["B"]

        # then B deals where possible
        n_B_offers = basket["B"] // 2
        total += n_B_offers * 45
        total += (basket["B"] - 2*n_B_offers) * PRICES["B"]
    
    if "A" in basket:
        # Apply bulk A deal first
        n_5A_offers = basket["A"] // 5
        total += n_5A_offers * 200
        basket["A"] -= 5 * n_5A_offers

        # then 2ndary A deal if possible
        n_3A_offers = basket["A"] // 3
        total += n_3A_offers * 130
        basket["A"] -= 3 * n_3A_offers

        total += basket["A"] * PRICES["A"]
    
    for char in ["C", "D"]:
        if char in basket:
            total += basket[char] * PRICES[char]
    
    if "F" in basket:
        n_F_offers = basket["F"] // 3
        basket["F"] -= n_F_offers
        total += PRICES["F"] * basket["F"]

    return total



