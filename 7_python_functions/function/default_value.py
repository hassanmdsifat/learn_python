def calculate_net_price(total_price, tax_percent=5):
    net_price = total_price + total_price * (tax_percent / 100)
    print(net_price)

calculate_net_price(100)
calculate_net_price(200)
calculate_net_price(300, 10)