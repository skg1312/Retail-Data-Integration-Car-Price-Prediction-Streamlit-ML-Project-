import pandas as pd
import numpy as np

# Product master with more nulls (for demo)
product_master = {
    'product_id': ['P100', 'P101', 'P102', 'P103', 'P104'],
    'product_name': ['Apple Juice', 'Chocolate Cookies', 'Orange Soda', 'Chips', 'Energy Bar'],
    'category': ['Beverage', 'Snacks', 'Beverage', 'Snacks', 'Health'],
    'price': [None, None, 60, np.nan, None],    # 4 nulls
    'stock': [np.nan, 20, None, None, 40]       # 3 nulls
}
df_product = pd.DataFrame(product_master)
# Add one more null
df_product.loc[4, 'price'] = np.nan

# a) Check column-wise nulls
nulls_by_col = df_product.isnull().any()

# b) Check if all values in each row are not null
rowwise_notnull = df_product.notnull().all(axis=1)

# c) Any/All for missing product data
any_missing_product = df_product.isnull().any().any()  # Any nulls anywhere?
all_missing_product = df_product.isnull().all().any()  # Any column all null?

print("Column-wise nulls:\n", nulls_by_col)
print("Each row not null:\n", rowwise_notnull)
print("Any missing product data?:", any_missing_product)
print("All missing in any column?:", all_missing_product)
