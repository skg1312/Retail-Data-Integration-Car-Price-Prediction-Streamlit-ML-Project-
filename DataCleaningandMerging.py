import pandas as pd

# Provided Data
sales_data = {
    'sale_id': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010'],
    'product_id': ['P100', 'P101', 'P102', 'P100', 'P103', 'P104', 'P101', 'P102', 'P103', 'P104'],
    'store_id': ['ST01', 'ST02', 'ST01', 'ST03', 'ST02', 'ST03', 'ST01', 'ST01', 'ST02', 'ST03'],
    'quantity': [5, 2, 3, 4, 1, 6, 2, 3, 7, 1],
    'sale_date': [
        '2024-05-10', '2024-05-11', '2024-05-12', '2024-05-13', '2024-05-14',
        '2024-05-15', '2024-05-16', '2024-05-17', '2024-05-18', '2024-05-19'
    ]
}

product_master = {
    'product_id': ['P100', 'P101', 'P102', 'P103', 'P104'],
    'product_name': ['Apple Juice', 'Chocolate Cookies', 'Orange Soda', 'Chips', 'Energy Bar'],
    'category': ['Beverage', 'Snacks', 'Beverage', 'Snacks', 'Health'],
    'price': [None, None, 60, 30, None],    # Intentionally added None (null)
    'stock': [50, 20, None, None, 40]       # Intentionally added None (null)
}

store_info = {
    'store_id': ['ST01', 'ST02', 'ST03'],
    'location': ['Mumbai', 'Bangalore', 'Delhi'],
    'manager': ['Aakash', 'Neha', 'Saurav']
}

# Convert to DataFrames
df_sales = pd.DataFrame(sales_data)
df_product = pd.DataFrame(product_master)
df_store = pd.DataFrame(store_info)

# Merge: sales + product, then result + store (inner join, only matching records)
df_master = pd.merge(df_sales, df_product, on='product_id', how='inner')
df_master = pd.merge(df_master, df_store, on='store_id', how='inner')

# Append one additional record
new_record = {
    'sale_id': 'S011',
    'product_id': 'P104',
    'store_id': 'ST01',
    'quantity': 4,
    'sale_date': '2024-05-20',
    'product_name': 'Energy Bar',
    'category': 'Health',
    'price': None,
    'stock': 40,
    'location': 'Mumbai',
    'manager': 'Aakash'
}
new_row_df = pd.DataFrame([new_record])
df_master = pd.concat([df_master, new_row_df], ignore_index=True)

print("Master DataFrame after merging and appending:")
print(df_master)
