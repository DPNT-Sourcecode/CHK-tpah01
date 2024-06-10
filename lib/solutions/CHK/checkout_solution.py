

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
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

    return total

# print(checkout("EEBBB"))







