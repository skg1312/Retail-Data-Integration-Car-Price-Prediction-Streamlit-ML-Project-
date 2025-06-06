import pandas as pd

# For demonstration, re-use df_master from Q1, here is a small dummy df_master:
df_master = pd.DataFrame({
    'sale_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'product_id': ['P100', 'P101', 'P102', 'P100', 'P103'],
    'store_id': ['ST01', 'ST02', 'ST01', 'ST03', 'ST02'],
    'quantity': [5, 2, 3, 4, 1],
    'sale_date': ['2024-05-10', '2024-05-11', '2024-05-12', '2024-05-13', '2024-05-14'],
    'product_name': ['Apple Juice', 'Chocolate Cookies', 'Orange Soda', 'Apple Juice', 'Chips'],
    'category': ['Beverage', 'Snacks', 'Beverage', 'Beverage', 'Snacks'],
    'price': [100, 80, 60, 100, 30],
    'stock': [50, 20, 10, 50, 20],
    'location': ['Mumbai', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore'],
    'manager': ['Aakash', 'Neha', 'Aakash', 'Saurav', 'Neha']
})

# iloc[] extraction
first5_first3 = df_master.iloc[:5, :3]
every_third_from_second = df_master.iloc[1::3, :]

# loc[] extraction (category == Beverage and price > 100)
beverage_gt_100 = df_master.loc[(df_master['category']=='Beverage') & (df_master['price'] > 100)]
# All sales in Mumbai
mumbai_sales = df_master.loc[df_master['location']=='Mumbai']

print("First 5 rows and first 3 columns:\n", first5_first3)
print("Every third row from second:\n", every_third_from_second)
print("Beverage & price>100:\n", beverage_gt_100)
print("Sales in Mumbai:\n", mumbai_sales)
