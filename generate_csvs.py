import pandas as pd

# 1. Sales Data
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
df_sales = pd.DataFrame(sales_data)
df_sales.to_csv('data/sales_data.csv', index=False)

# 2. Product Master Data
product_master = {
    'product_id': ['P100', 'P101', 'P102', 'P103', 'P104'],
    'product_name': ['Apple Juice', 'Chocolate Cookies', 'Orange Soda', 'Chips', 'Energy Bar'],
    'category': ['Beverage', 'Snacks', 'Beverage', 'Snacks', 'Health'],
    'price': [None, None, 60, 30, None],    # Example nulls
    'stock': [50, 20, None, None, 40]       # Example nulls
}
df_product = pd.DataFrame(product_master)
df_product.to_csv('data/product_master.csv', index=False)

# 3. Store Info Data
store_info = {
    'store_id': ['ST01', 'ST02', 'ST03'],
    'location': ['Mumbai', 'Bangalore', 'Delhi'],
    'manager': ['Aakash', 'Neha', 'Saurav']
}
df_store = pd.DataFrame(store_info)
df_store.to_csv('data/store_info.csv', index=False)

print("CSV files created in the 'data/' directory.")
