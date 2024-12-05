# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# Extract relevant columns and filter for Washington state
data = data[data['State'] == 'WA']
data['Registration_Year'] = pd.to_datetime(data['Model Year'], format='%Y').dt.year

# Aggregate registrations by year
yearly_data = data.groupby('Registration_Year').size().reset_index(name='Registrations')

# Prepare the data for time-series forecasting
for lag in range(1, 4):  # Create lagged features for the past 3 years
    yearly_data[f'Lag_{lag}'] = yearly_data['Registrations'].shift(lag)

# Drop rows with NaN (introduced by lagging)
yearly_data = yearly_data.dropna()

# Define features (lagged values) and target (registrations)
X = yearly_data[['Lag_1', 'Lag_2', 'Lag_3']]
y = yearly_data['Registrations']

# Train-test split (train on historical data, test on the last available year)
X_train, X_test = X[:-1], X[-1:]
y_train, y_test = y[:-1], y[-1:]

# Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict the last year's registrations (for evaluation)
y_pred_test = model.predict(X_test)
print(f"Mean Absolute Error for last year: {mean_absolute_error(y_test, y_pred_test)}")

# Forecast registrations for 2023–2028
future_years = [2023, 2024, 2025, 2026, 2027, 2028]
future_predictions = []
last_known_data = yearly_data.iloc[-1, 1:].values  # Last row's lags

for year in future_years:
    # Predict the next year's registrations
    prediction = model.predict([last_known_data[:3]])[0]
    future_predictions.append(prediction)

    # Update lags for the next prediction
    last_known_data = np.roll(last_known_data, 1)
    last_known_data[0] = prediction

# Combine predictions with years
future_forecast = pd.DataFrame({'Year': future_years, 'Predicted_Registrations': future_predictions})

# Save results to CSV for Tableau visualization
yearly_data = yearly_data[['Registration_Year', 'Registrations']].rename(columns={'Registration_Year': 'Year'})
final_data = pd.concat([yearly_data, future_forecast], ignore_index=True)
final_data.to_csv('EV_Registrations_Forecast.csv', index=False)

print(final_data)