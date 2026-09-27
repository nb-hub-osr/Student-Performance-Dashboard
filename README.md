# 🎓 Student Performance Dashboard

A Python-based student performance dashboard built using Pandas, Streamlit, Matplotlib, and Scikit-learn.

## 📌 About the Project

This project analyzes student performance using attendance, study hours, and subject marks.

It also uses a Linear Regression model to predict a student's average marks based on their study hours and attendance.

## ✨ Features

- View student performance data
- Calculate average marks
- Filter students by attendance
- View individual student performance
- Compare subject performance
- Rank students based on average marks
- Identify students needing attention
- Analyze attendance
- Predict average marks using Machine Learning
- Interactive Streamlit dashboard

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib
- Scikit-learn
- Linear Regression

## 🤖 Machine Learning

The project uses **Linear Regression**.

### Input Features

- Study Hours
- Attendance

### Target

- Average Marks

The model is trained using existing student data and can predict the average marks of a new student.

## 📊 Dataset

The dataset contains:

- Student Name
- Attendance
- Study Hours
- Python Marks
- ML Marks
- OS Marks

The Average Marks column is calculated from Python, ML, and OS marks.

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt


Run the Streamlit dashboard:
python -m streamlit run dashboard.py

```

