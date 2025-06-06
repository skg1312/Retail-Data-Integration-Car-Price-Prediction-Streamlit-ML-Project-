import pandas as pd

# Provided and new stores
store_info = {
    'store_id': ['ST01', 'ST02', 'ST03'],
    'location': ['Mumbai', 'Bangalore', 'Delhi'],
    'manager': ['Aakash', 'Neha', 'Saurav']
}

df_store = pd.DataFrame(store_info)
new_store_info = pd.DataFrame({
    'store_id': ['ST04', 'ST05'],
    'location': ['Chennai', 'Hyderabad'],
    'manager': ['Priya', 'Rahul']
})

# Concatenate vertically
df_all_stores = pd.concat([df_store, new_store_info], axis=0)
df_all_stores.reset_index(drop=True, inplace=True)
df_all_stores['store_status'] = 'Active'

print("All Stores with Status:")
print(df_all_stores)
