import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import sys

def download_dataset():
    try:
        # Initialize the Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        # Download the dataset
        print("Downloading dataset...")
        api.dataset_download_files('mahmoudelhemaly/students-grading-dataset', path='.', unzip=True)
        print("Dataset downloaded successfully!")
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        print("\nPlease make sure you have:")
        print("1. Created a Kaggle account")
        print("2. Downloaded your Kaggle API credentials (kaggle.json)")
        print("3. Placed the kaggle.json file in ~/.kaggle/ directory")
        print("4. Set the correct permissions: chmod 600 ~/.kaggle/kaggle.json")
        sys.exit(1)

def main():
    # Create visualizations directory if it doesn't exist
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')

    # Download dataset if it doesn't exist
    if not os.path.exists('Students_Grading_Dataset.csv'):
        download_dataset()

    # Read the dataset
    print("\nReading dataset...")
    df = pd.read_csv('Students_Grading_Dataset.csv')

    # Basic information about the dataset
    print("\nDataset Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())

    # 1. Grade Distribution Analysis
    print("\nCreating visualizations...")
    plt.figure(figsize=(10, 6))
    grade_counts = df['Grade'].value_counts().sort_index()
    plt.bar(grade_counts.index, grade_counts.values)
    plt.title('Distribution of Grades')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/grade_distribution.png')
    plt.close()

    # 2. Correlation Analysis (numeric columns only)
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    correlation_matrix = df[numeric_columns].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Correlation Matrix (Numeric Features)')
    plt.tight_layout()
    plt.savefig('visualizations/correlation_matrix.png')
    plt.close()

    # 3. Box Plot for Grade Distribution by Study Hours
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Study_Hours_per_Week', y='Total_Score')
    plt.title('Total Score Distribution by Study Hours')
    plt.xlabel('Study Hours per Week')
    plt.ylabel('Total Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/score_vs_study_hours.png')
    plt.close()

    # 4. Scatter Plot of Total Score vs Study Hours
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Study_Hours_per_Week', y='Total_Score', alpha=0.5)
    plt.title('Total Score vs Study Hours')
    plt.xlabel('Study Hours per Week')
    plt.ylabel('Total Score')
    plt.tight_layout()
    plt.savefig('visualizations/score_vs_hours_scatter.png')
    plt.close()

    # Statistical Analysis
    print("\nPerforming statistical analysis...")
    
    # Correlation between Study Hours and Total Score
    correlation = df['Study_Hours_per_Week'].corr(df['Total_Score'])
    print("\n1. Correlation between Study Hours and Total Score:")
    print(f"Correlation coefficient: {correlation:.3f}")

    # Perform t-test for different study hours groups
    high_study = df[df['Study_Hours_per_Week'] > df['Study_Hours_per_Week'].median()]
    low_study = df[df['Study_Hours_per_Week'] <= df['Study_Hours_per_Week'].median()]

    t_stat, p_value = stats.ttest_ind(high_study['Total_Score'], low_study['Total_Score'])
    print(f"\n2. T-test results for high vs low study hours:")
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.3f}")

    # Summary Statistics by Study Hours
    print("\n3. Summary Statistics by Study Hours:")
    study_hours_summary = df.groupby('Study_Hours_per_Week')['Total_Score'].agg(['mean', 'std', 'count'])
    print(study_hours_summary)

    # Grade Distribution
    print("\n4. Grade Distribution:")
    grade_distribution = df['Grade'].value_counts().sort_index()
    print(grade_distribution)

    # Save results to a text file
    print("\nSaving results...")
    with open('analysis_results.txt', 'w') as f:
        f.write("Student Grade Analysis Results\n")
        f.write("=============================\n\n")
        f.write("1. Correlation between Study Hours and Total Score:\n")
        f.write(f"   Correlation coefficient: {correlation:.3f}\n\n")
        f.write("2. T-test results for high vs low study hours:\n")
        f.write(f"   T-statistic: {t_stat:.3f}\n")
        f.write(f"   P-value: {p_value:.3f}\n\n")
        f.write("3. Summary Statistics by Study Hours:\n")
        f.write(study_hours_summary.to_string())
        f.write("\n\n4. Grade Distribution:\n")
        f.write(grade_distribution.to_string())

    print("\nAnalysis complete! Check the 'visualizations' directory for plots and 'analysis_results.txt' for detailed statistics.")

if __name__ == "__main__":
    main() 