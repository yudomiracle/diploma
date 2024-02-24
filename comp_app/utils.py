def calculate_total_price(products, quantities):
    total_price = 0
    for product, quantity in zip(products, quantities):
        total_price += product.price * quantity
    return total_price