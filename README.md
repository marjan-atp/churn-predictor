🏦 Bank Customer Churn Prediction using XGBoost

📌 Project Overview

Customer churn is one of the biggest challenges faced by banks. Retaining existing customers is significantly more cost-effective than acquiring new ones. This project builds a machine learning model to predict whether a customer is likely to leave the bank, enabling businesses to take proactive retention measures.

The model is trained on a dataset containing 165,000 customer records and predicts the probability of churn for each customer.

---

🎯 Project Objective

Develop a robust machine learning model that predicts whether a customer will churn and provides the probability (%) of churn to support data-driven customer retention strategies.

---

📊 Dataset

- Total Records: 165,000
- Target Variable: "Exited"
  - 1: Customer Churned
  - 0: Customer Stayed

Features Used

- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary

Removed Columns

- ID
- CustomerId
- Surname

---

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Imbalanced-learn

---

🔄 Machine Learning Workflow

- Data Cleaning & Preprocessing
- Label Encoding
- Feature Scaling
- Handling Class Imbalance using SMOTE
- Hyperparameter Tuning
- Model Training using XGBoost
- Model Evaluation
- Churn Probability Prediction

---

🤖 Model Information

Algorithm: XGBoost Classifier

Performance

- ✅ Accuracy: 91%

The model predicts:

- Whether a customer will churn.
- The probability (%) of customer churn.

---

📈 Features of the Project

- Predict customer churn accurately.
- Display churn probability (%).
- Handle imbalanced datasets using SMOTE.
- Optimized model through hyperparameter tuning.
- Clean and scalable machine learning pipeline.

---

📂 Project Structure

Bank-Customer-Churn-Prediction/
│
├── data/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
├── README.md
└── assets/

---

🚀 Installation

git clone https://github.com/yourusername/Bank-Customer-Churn-Prediction.git

cd Bank-Customer-Churn-Prediction

pip install -r requirements.txt

---

▶️ Run the Project

streamlit run app.py

---

📷 Project Demo

Application Screenshot

"Bank Customer Churn Predictor" (assets/app_screenshot.png)
churn-predictor//window.png


🌐 Live Demo

https://churn-predictor-01bank.streamlit.app/

---

📌 Future Improvements

- Deploy the model on the cloud.
- Add Explainable AI using SHAP.
- Support batch predictions.
- Automate model retraining.
- Build an interactive analytics dashboard.

---

👨‍💻 Author

Ahammed Marjan K

Data Science | Machine Learning | Python | SQL | Power BI | Tableau

If you found this project useful, consider giving it a ⭐ on GitHub.
