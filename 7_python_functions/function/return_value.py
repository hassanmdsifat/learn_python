def calculate_net_price(total_price, tax_percent=5):
    net_price = total_price + total_price * (tax_percent / 100)
    return net_price


dream_cafe_net_price = calculate_net_price(100)
print(dream_cafe_net_price)