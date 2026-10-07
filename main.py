import pandas as pd
import numpy as np
from functions import process_student_data, get_subject_averages, get_top_performers

def main():
    print("=" * 60)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 60)
    
    # Step 1 & 2: Load Data
    try:
        df = pd.read_csv('students.csv')
        print(f"\n[INFO] Dataset loaded successfully with {len(df)} records.\n")
    except FileNotFoundError:
        print("[ERROR] 'students.csv' file not found. Please ensure it is in the same directory.")
        return

    print("--- Raw Data Preview ---")
    print(df.head(), "\n")

    # Step 3: Process Data (Totals, Averages, Grades, Status)
    df = process_student_data(df)

    # Step 4: Perform Analysis
    print("=" * 60)
    print("                 PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    overall_class_avg = df['Average_Marks'].mean()
    print(f"-> Overall Class Average Marks: {overall_class_avg:.2f}")

    total_passed = (df['Status'] == 'Pass').sum()
    total_failed = (df['Status'] == 'Fail').sum()
    print(f"-> Total Students Passed: {total_passed}")
    print(f"-> Total Students Failed: {total_failed}")

    subject_avgs = get_subject_averages(df)
    print("\n-> Subject-wise Average Performance:")
    for sub, avg in subject_avgs.items():
        print(f"   * {sub}: {avg:.2f}")

    best_subject = subject_avgs.idxmax()
    print(f"\n-> Subject with the Best Average: {best_subject} ({subject_avgs[best_subject]:.2f})")

    top_student = df.loc[df['Average_Marks'].idxmax()]
    print(f"-> Student with Highest Average: {top_student['Name']} (ID: {top_student['Student_ID']}) with {top_student['Average_Marks']:.2f}")

    print("\n--- Top 3 Performing Students ---")
    print(get_top_performers(df, 3).to_string(index=False))

    print("\n" + "=" * 60)
    print("Execution Completed Successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()