def calculate_shipping_cost(weight, delivery_type, discount_code):
    cost = 0
    if weight <= 0:
        return None

    # Cost based on weight
    if weight <= 5:
        cost = 10
    elif weight < 20:
        cost = 20
    else:
        cost = 50

    
    # Additional cost based on delivery type
    if delivery_type == "standard":
        cost += 5
    elif delivery_type == "express":
        cost += 15
    elif delivery_type == "overnight":
        cost += 25
    else:
        return None

    # Apply discount if applicable
    if discount_code != '':
        if discount_code == "LOYALTY10":
            cost *= 0.9  # 10% discount
        elif discount_code == "LOYALTY20":
            cost *= 0.8  # 20% discount
        elif discount_code == "FREESHIP":
            cost = 0  # Free shipping
        elif discount_code == "NONE":
            return cost
        else:
            return None
    else:
        return None

    return cost
