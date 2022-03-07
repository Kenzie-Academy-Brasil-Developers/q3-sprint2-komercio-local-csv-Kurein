import csv

def generate_list(FILEPATH):
    product_list=[]

    with open(FILEPATH, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            product_list.append(line)

    return product_list

def get_products(FILEPATH, page, per_page):
    product_list = generate_list(FILEPATH)
    if page == 1:
        first_item = 0
    else:
        first_item = int(page)*int(per_page)-int(per_page)
    last_item = int(page)*int(per_page)
    filtered_list = product_list[first_item:last_item]
    return filtered_list

def get_product(FILEPATH, product_id):
    product_list = generate_list(FILEPATH)
    for item in product_list:
        if item["id"] == product_id:
            filtered_item = item
    return filtered_item

def create_product(FILEPATH, data):
    product_list = generate_list(FILEPATH)
    data["id"] = int(product_list[-1]['id'])+1
    fieldnames = ["id", "name", "price"]

    with open(FILEPATH, "a") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)
    
    return data

def update_product(FILEPATH, data, product_id):
    fieldnames = ["id", "name", "price"]
    product_list = generate_list(FILEPATH)
    product = get_product(FILEPATH, product_id)
    for key, value in data.items():
        product[key] = value
    product_list[int(product_id)-1] = product

    with open(FILEPATH, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({"id":"id", "name":"name", "price":"price"})

    with open(FILEPATH, "a") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for product in product_list:
            writer.writerow(product)

    return product_list[int(product_id)-1]

def delete_product(FILEPATH, product_id):
    fieldnames = ["id", "name", "price"]
    product = get_product(FILEPATH, product_id)
    product_list = generate_list(FILEPATH)
    popped_product = product_list.pop(product_list.index(product))

    with open(FILEPATH, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({"id":"id", "name":"name", "price":"price"})

    with open(FILEPATH, "a") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for product in product_list:
            writer.writerow(product)

    return popped_product