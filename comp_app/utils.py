def calculate_total_price(products, quantity):
    total_price = 0
    for product in products:
        total_price += product.price * quantity
    return total_price