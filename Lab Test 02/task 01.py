def add_stock(stock, sold):
    for item in sold:
        if item in stock:
            stock[item] = stock[item] + sold[item]
        else:
            stock[item] = sold[item]
    return stock

stock = {"Shoes": 10, "Socks": 20}
sold = {"Shoes": 2, "Socks": 5}
print(add_stock(stock, sold))
