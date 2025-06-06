import pandas as pd

# Use df_master from Q4
df_master = pd.DataFrame({
    'sale_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'product_id': ['P100', 'P101', 'P102', 'P100', 'P103'],
    'store_id': ['ST01', 'ST02', 'ST01', 'ST03', 'ST02'],
    'quantity': [5, 2, 3, 4, 1],
    'sale_date': ['2024-05-10', '2024-05-11', '2024-05-12', '2024-05-13', '2024-05-14'],
    'product_name': ['Apple Juice', 'Chocolate Cookies', 'Orange Soda', 'Apple Juice', 'Chips'],
    'category': ['Beverage', 'Snacks', 'Beverage', 'Beverage', 'Snacks'],
    'price': [100, 80, 60, 120, 30],
    'stock': [50, 20, 10, 50, 20],
    'location': ['Mumbai', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore'],
    'manager': ['Aakash', 'Neha', 'Aakash', 'Saurav', 'Neha']
})

# a) total_sale_amount column
df_master['total_sale_amount'] = df_master['price'] * df_master['quantity']

# b) Show sales where total_sale_amount > 500
big_sales = df_master[df_master['total_sale_amount'] > 500]

# c) All "Snacks" have stock > 10?
snacks_all_stock_gt_10 = (df_master[df_master['category']=='Snacks']['stock'] > 10).all()

# d) Any "Beverage" price < 50?
any_beverage_price_lt_50 = (df_master[df_master['category']=='Beverage']['price'] < 50).any()

print("Sales with total_sale_amount > 500:\n", big_sales)
print('All Snacks have stock > 10:', snacks_all_stock_gt_10)
print('Any Beverage price < 50:', any_beverage_price_lt_50)
