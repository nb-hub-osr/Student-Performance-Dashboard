import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error

from sklearn.metrics import mean_absolute_error,r2_score

# Load data
data = pd.read_csv("students.csv")

# Create Average
data["Average"] = data[["Python", "ML", "OS"]].mean(axis=1)

# Input and target
X = data[["Study_Hours", "Attendance"]]
y = data["Average"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:")
print(X_train)

print("\nX_test:")
print(X_test)

print("\ny_train:")
print(y_train)

print("\ny_test:")
print(y_test)


# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

mae= mean_absolute_error(y_test,predictions)
print("MAE:",mae)

r2=r2_score(y_test,predictions)
print("R^2 Score:",r2)

print("Actual Average:")
print(y_test.values)
print("predicted values:")
print(predictions)


new_student = [[5, 90]]

new_prediction = model.predict(new_student)

print("Predicted Average for new student:")
print(new_prediction)