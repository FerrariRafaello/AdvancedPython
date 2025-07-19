def enumerate_tuple(t):
    # Generator yielding formatted strings of index and value
    return (f"{index} {value}" for index, value in enumerate(t))

def min_max_price(products):
    min_price = min(zip(products.values(), products.keys()))
    max_price = max(zip(products.values(), products.keys()))
    return min_price, max_price

def main():
    sample_tuple = (1, 2, 3, 4)
    print("Enumerating tuple:")
    for item in enumerate_tuple(sample_tuple):
        print(item)

    product_prices = {
        "tablet": 2000,
        "notebook": 3000,
        "iphone": 5000
    }
    min_price, max_price = min_max_price(product_prices)
    print("\nMinimum price:", min_price)
    print("Maximum price:", max_price)

if __name__ == "__main__":
    main()
