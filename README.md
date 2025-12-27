# Student Performance Indicator

**Live Demo:** 

https://student-performance-indicator-mgt.streamlit.app/

A production-ready machine learning project that predicts student academic performance based on demographic and academic features via an interactive Streamlit web app.

---

## Problem Statement

Predicting student performance helps educators, administrators, and learners understand potential academic outcomes **before final exams**, enabling early intervention strategies to improve learning outcomes and tailor support where it’s needed most. Early prediction of performance can:

* Identify at-risk students for targeted support
* Inform parents/teachers of learning gaps
* Enable personalized learning plans based on data-driven insights

---

## Dataset Description

The project uses the **Students Performance dataset** (commonly sourced from Kaggle/UCI), containing academic, demographic, and background features such as:

| Feature                     | Description                              |
| --------------------------- | ---------------------------------------- |
| Gender                      | Student’s gender                         |
| Race/Ethnicity              | Ethnic group membership                  |
| Parental Level of Education | Highest parent education level           |
| Lunch                       | Type of lunch (standard or free/reduced) |
| Test Preparation Course     | Completed or not                         |
| Math Score                  | Final math exam score                    |
| Reading Score               | Final reading exam score                 |
| Writing Score               | Final writing exam score                 |

These features help the model learn patterns associated with student success or challenges in academic performance.

---

## Model Performance Metrics

This section summarizes your model’s evaluation results on the test set. Replace placeholders with **actual results from your notebook or evaluation script**:

| Metric        | Score |
| ------------- | ----- |
| **R2-Score**  | `88%` |


> ⚡ *These metrics were obtained using cross-validation on the test split to ensure robust performance estimation.*

---

## App Screenshots

**Homepage:**
`![Homepage Screenshot](path/to/homepage.png)`

**Prediction Form:**
`![Input Form Screenshot](path/to/inputform.png)`

**Prediction Result:**
`![Result Screenshot](path/to/result.png)`

---

## How to Run Locally

Follow these steps to get the application up and running on your machine:

### Clone the repository

```
git clone https://github.com/MadanGTiwary/mlproject.git
cd mlproject
```

### Set up a virtual environment (recommended)

```
conda activate ./mlproject/
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit app

```
streamlit run streamlit_app.py
```

### Navigate to the Interface

Open your browser and visit:

```
http://localhost:8501
```

You’ll see the interactive UI where you can input student features and get performance predictions.

---

## Live Demo

**Streamlit App Link:**

https://student-performance-indicator-mgt.streamlit.app/

---

## Tech Stack

* **Python** – Core language
* **Pandas,NumPy** – Data loading & manipulation
* **Scikit-learn, CatBoost, XGBoost** – Model training
* **Streamlit** – Web app deployment
* **GitHub** – Version control & repository

---

## 📂 Project Structure

```
mlproject/
├── artifacts/                # Trained model and preprocessing files
├── notebook/                 # EDA and model training notebooks
├── src/                      # Source code & pipeline scripts
├── templates/                # UI components (if any)
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
└── README.md
```


---

## 📜 License

This project is open-source and available under the **MIT License**.
