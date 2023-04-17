# Step 1: Collect the data
import pandas as pd

df = pd.read_csv('LandTrading.csv')
df
print(df)

# Step 2: Preprocess the data
# TODO: Perform data preprocessing steps such as handling missing values, scaling the features, and encoding categorical variables

# Step 3: Split the data
from sklearn.model_selection import train_test_split

X = df.drop('price_per_sqm', axis=1)
y = df['price_per_sqm']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Select a model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Evaluate the model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('Mean Absolute Error:', mae)
print('R-squared:', r2)

# Step 7: Make predictions
# TODO: Input the features of a new street house and use the model to predict its price per square meter
