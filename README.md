# Student Performance Analytics System

## 1. Project Title & Details
* **Project Title:** Student Performance Analytics System
* **Course:** Python with AI (EWB Courses)
* **Student Name:** Abhi Dhruve

## 2. Objective
The objective of this project is to build a Python-based data analytics application that ingests student records, computes performance statistics using NumPy and Pandas, assigns grades, assesses pass/fail criteria, and extracts valuable insights like subject-wise performance and top-performing students[cite: 1].

## 3. Technologies Used
* **Python** (Core logic, loops, modular functions)
* **Pandas** (DataFrame loading, filtering, grouping, and statistical operations)
* **NumPy** (Numerical calculations and vectorised array computations)

## 4. Dataset Description
* **File Name:** `students.csv`
* **Records:** 20 student entries
* **Key Fields:** `Student_ID`, `Name`, `Department`, `Maths`, `Science`, `English`, `Computer_Science`, and `Attendance_Percentage`.

## 5. Implementation Summary
1. **Data Ingestion:** Loaded the CSV dataset into a Pandas DataFrame and verified schema integrity.
2. **Processing & Calculations:** Calculated total and average marks across subjects utilizing Pandas/NumPy vectorization.
3. **Rule Application:** Implemented modular functions to map average scores into standard letter grades (`A` to `F`) and evaluate pass/fail criteria factoring in attendance requirements.
4. **Insight Generation:** Extracted class-wide aggregates, best-performing subjects, and top student rankings.

## 6. Key Features
* Automated total and average score calculation.
* Dynamic letter grading logic.
* Attendance-inclusive pass/fail evaluation.
* Subject-wise performance tracking and identification of top performers.

## 7. Final Outcome
Successfully built a lightweight, modular analytics pipeline that processes raw student datasets and presents clear, readable academic insights without reliance on advanced machine learning libraries.

## 8. Challenges & Learning
* **Challenge:** Ensuring cleaner modular separation between calculation utilities (`functions.py`) and execution flow (`main.py`).
* **Learning:** Gained strong practical command over handling Pandas DataFrames, axis-wise numerical reductions with NumPy, and formatting clean terminal outputs.
