#!/usr/bin/env python
# coding: utf-8

# # VISHAL RAMKUMAR RAJBHAR
# EMAIL ID:- vishalrajbhar.0913@gmail.com
# STUDENT ID: CA/JA3/2128
# DOMAIN: MACHINE LEARNING

# In[1]:


pip install pandas scikit-learn numpy


# In[8]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = 'C:/Users/vishal rajbhar/Downloads/data (1).csv'
df = pd.read_csv(file_path)



# In[11]:


# Display basic dataset information
print("Dataset Overview:")
print(df.head(10))


# In[14]:


# Define features (X) and target (y)
X = df.drop(columns=['liked'])  # Features
y = df['liked']                # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# In[17]:


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature Importance
importances = model.feature_importances_
feature_names = X.columns

print("\nFeature Importance:")
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

