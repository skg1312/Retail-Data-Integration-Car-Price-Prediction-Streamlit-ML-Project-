import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Example data
data = pd.DataFrame({
    'year': [2010, 2012, 2015, 2017, 2018],
    'km_driven': [50000, 40000, 30000, 25000, 12000],
    'fuel': [0, 1, 0, 1, 0],  # Encoded: 0=Petrol, 1=Diesel
    'transmission': [0, 1, 0, 1, 0],  # 0=Manual, 1=Automatic
    'price': [300000, 350000, 480000, 550000, 700000]
})
X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
with open('car_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
