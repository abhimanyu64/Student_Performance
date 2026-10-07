import numpy as np
import pandas as pd

def calculate_totals_and_averages(df):
    """Calculates total marks and average marks for each student using NumPy/Pandas."""
    subject_cols = ['Maths', 'Science', 'English', 'Computer_Science']
    
    # Using NumPy to compute row-wise sum and average across subject columns
    df['Total_Marks'] = df[subject_cols].sum(axis=1)
    df['Average_Marks'] = df[subject_cols].mean(axis=1)
    return df

def assign_grade(avg):
    """Assigns a letter grade based on the average marks."""
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 55:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

def check_pass_fail(avg, attendance):
    """Determines pass/fail status based on average marks and attendance criteria."""
    if avg >= 40 and attendance >= 65:
        return 'Pass'
    else:
        return 'Fail'

def process_student_data(df):
    """Applies grading and pass/fail rules to the dataframe."""
    df = calculate_totals_and_averages(df)
    df['Grade'] = df['Average_Marks'].apply(assign_grade)
    df['Status'] = df.apply(lambda row: check_pass_fail(row['Average_Marks'], row['Attendance_Percentage']), axis=1)
    return df

def get_subject_averages(df):
    """Calculates subject-wise average performance."""
    subject_cols = ['Maths', 'Science', 'English', 'Computer_Science']
    return df[subject_cols].mean()

def get_top_performers(df, n=3):
    """Returns top N performing students based on average marks."""
    return df.nlargest(n, 'Average_Marks')[['Student_ID', 'Name', 'Department', 'Average_Marks', 'Grade']]