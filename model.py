import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the training and testing data
train_data = pd.read_csv("MIM-Final.csv")
test_data = pd.read_csv("Test-FINAL.csv")

# Split the training data into features and target variable
X_train = train_data.drop(columns=['Label'])
y_train = train_data['Label']

# Split the testing data into features and target variable
X_test = test_data.drop(columns=['Label'])
y_test = test_data['Label']

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Save the trained model using pickle
with open('random_forest_model2.pkl', 'wb') as file:
    pickle.dump(rf_classifier, file)

# Predictions on the testing set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Example of predicting a new data point
# new_data_point = [[value_IRTT, value_TTOC, value_MITR, value_MATR]]
# prediction = rf_classifier.predict(new_data_point)
# print("Prediction for the new data point:", prediction)
