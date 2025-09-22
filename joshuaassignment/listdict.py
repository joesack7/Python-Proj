products = [
    {"name": "Laptop", "price" : 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price":600}
]
#returns all products with a price less than or equal to budget
def get_affordable_products(products, budget):
    affordable = []
    for product in products:
        if product["price"] <= budget:
            affordable.append(product)
    return affordable
