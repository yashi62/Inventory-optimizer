import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load sample data
data = pd.DataFrame({
    'week': [1, 2, 3, 4, 5],
    'demand': [100, 120, 150, 130, 160]
})

X = data[['week']]
y = data['demand']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.joblib')
print("Model saved as 'model.joblib'")
