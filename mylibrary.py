## Business Logic ---------------------------------------------------------------------
## This file stores the function(s) that implement the ticket pricing logic.
## calculate_total:
## Takes in the number of adults, the number of children and the ticket type
## Returns a breakdown of the cost (a list of dictionaries), the total price,
## and how much the visitor saved with the family package.
## ------------------------------------------------------------------------------------

## Pricing Scheme ---------------------------------------------------------------------
## Each ticket type has a price for an adult, a child, and a family package.
## A family package covers 2 adults + 2 children.
## Standard: separately 2 x $30 + 2 x $20 = $100, family package = $85
## Express : separately 2 x $50 + 2 x $35 = $170, family package = $145
## So buying a family package is always cheaper than buying the tickets separately.
## ------------------------------------------------------------------------------------

PRICES = {
    "standard": {"adult": 30, "child": 20, "family": 85},
    "express":  {"adult": 50, "child": 35, "family": 145},
}


def calculate_total(num_adults, num_children, ticket_type):
    prices = PRICES[ticket_type]

    ## Step 1: work out how many family packages we can make
    ## Each family package needs 2 adults and 2 children
    families_from_adults = num_adults // 2
    families_from_children = num_children // 2
    num_families = min(families_from_adults, families_from_children)

    ## Step 2: whoever is left over pays the normal price
    remaining_adults = num_adults - (num_families * 2)
    remaining_children = num_children - (num_families * 2)

    ## Step 3: calculate the cost of each part
    family_cost = num_families * prices["family"]
    adult_cost = remaining_adults * prices["adult"]
    child_cost = remaining_children * prices["child"]
    total = family_cost + adult_cost + child_cost

    ## Step 4: how much would it have cost without the family package?
    full_price = (num_adults * prices["adult"]) + (num_children * prices["child"])
    savings = full_price - total

    ## Step 5: build a breakdown table (a list of dictionaries, like the starter code)
    breakdown = []
    if num_families > 0:
        breakdown.append({"item": "family package (2 adults + 2 children)",
                          "quantity": num_families,
                          "unit price ($)": prices["family"],
                          "subtotal ($)": family_cost})
    if remaining_adults > 0:
        breakdown.append({"item": "adult ticket",
                          "quantity": remaining_adults,
                          "unit price ($)": prices["adult"],
                          "subtotal ($)": adult_cost})
    if remaining_children > 0:
        breakdown.append({"item": "child ticket",
                          "quantity": remaining_children,
                          "unit price ($)": prices["child"],
                          "subtotal ($)": child_cost})

    return breakdown, total, savings
