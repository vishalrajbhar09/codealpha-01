
# VISHAL RAMKUMAR RAJBHAR

EMAIL ID:- vishalrajbhar.0913@gmail.com

STUDENT ID: CA/JA3/2128

DOMAIN: MACHINE LEARNING

Task Overview - Machine Learning Model Implementation Using Random Forest Classifier
This task involves building and evaluating a machine learning model using the Random Forest Classifier to predict a target variable (liked). The dataset is loaded from a CSV file, preprocessed, split into training and testing sets, and then used to train and evaluate the model.

1. Task Breakdown

1.1. Data Loading

The dataset is read from a CSV file using the pandas library.
This dataset contains multiple features (independent variables) and one target variable (liked).








The dataset structure is examined using .head() to get an initial understanding.

1.2. Data Preprocessing
Features (X) are selected by dropping the target column (liked).
The target variable (y) is extracted separately.
This step ensures the dataset is correctly structured before training.

1.3. Splitting Data into Training & Testing Sets
The dataset is split into 80% training and 20% testing using train_test_split().
The training set is used to train the machine learning model.
The testing set is used to evaluate how well the model performs on unseen data.

1.4. Model Training
A Random Forest Classifier is chosen for training.
The classifier is trained on the training dataset (X_train, y_train).
The model learns patterns and relationships from the input features.

1.5. Making Predictions
The trained model is used to make predictions on the testing dataset (X_test).
The output predictions are compared with the actual test labels.

1.6. Model Evaluation
The accuracy score is calculated to measure the model’s overall performance.
A classification report is generated, showing precision, recall, and F1-score for each class.
These metrics help understand whether the model is making accurate predictions or not.

1.7. Feature Importance Analysis
The model determines which features contribute the most to predictions.
Feature importance scores are extracted from the model and displayed.
This helps understand which input variables are most influential in the decision-making process.


2. Objective of the Task

The primary goal of this task is to:

✅ Build a machine learning model that predicts whether an instance is "liked" or not.

✅ Evaluate the model's performance using accuracy and classification metrics.

✅ Identify important features that affect predictions the most.

This task is useful for real-world applications where classification problems arise, such as:

🔹 Predicting customer preferences.

🔹 Understanding user behavior.

🔹 Improving decision-making using AI models.
