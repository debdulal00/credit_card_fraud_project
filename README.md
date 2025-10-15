# Credit Card Fraud Detection

## Project Overview
This project uses machine learning to detect fraudulent credit card transactions. By analyzing transaction patterns such as amount, time, and historical behavior, the model identifies anomalies that indicate potential fraud. 

## Features
- Detects fraudulent transactions in real-time.
- Handles imbalanced datasets using oversampling techniques.
- Compares multiple ML models like Logistic Regression, Random Forest, and XGBoost for best performance.
- Visualizes transaction patterns and anomalies.

## Dataset
The dataset contains anonymized credit card transactions with features like:
- `Time`: Seconds elapsed from the first transaction
- `Amount`: Transaction amount
- `V1, V2, ... V28`: Principal components from PCA for confidentiality
- `Class`: Target variable (0 = legitimate, 1 = fraud)

Source: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Installation
1. Clone the repository:  
   ```bash
   git clone <your-repo-url>
Install dependencies:
pip install -r requirements.txt

Usage

Load the dataset and perform preprocessing.

Train and evaluate multiple ML models.

Visualize results and anomalies.

# Example
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

Results

Accuracy, Precision, Recall, F1-Score for each model.

Confusion matrix visualization for fraud detection performance.

Author

Debdulal Sahoo – Passionate about Machine Learning and AI

License
This project is licensed under the MIT License.
