
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Set seaborn style for better visualization
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
def load_and_explore_data(csv_path='iris.csv'):
    try:
        # Load Iris dataset from CSV
        df = pd.read_csv(csv_path)
        
        # Ensure column names are consistent
        df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']
        df['species'] = df['species'].astype('category')
        
        # Display first few rows
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        
        # Check data types and missing values
        print("\nData Types:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        # Clean dataset (handle missing values if any)
        if df.isnull().values.any():
            print("\nHandling missing values...")
            df = df.fillna(df.mean(numeric_only=True))
            print("Missing values filled with column means")
        
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        sys.exit(1)

# Task 2: Basic Data Analysis
def analyze_data(df):
    try:
        # Basic statistics
        print("\nBasic Statistics:")
        print(df.describe())
        
        # Group by species and compute mean
        print("\nMean measurements by species:")
        group_means = df.groupby('species').mean()
        print(group_means)
        
        # Basic insights
        print("\nAnalysis Insights:")
        print("- The dataset contains measurements for three iris species")
        print("- Each species has distinct average measurements")
        print("- Setosa tends to have smaller measurements compared to versicolor and virginica")
        
        return group_means
    
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        return None

# Task 3: Data Visualization
def create_visualizations(df):
    try:
        # Create figure with subplots
        plt.figure(figsize=(15, 10))
        
        # 1. Line chart (average measurements per species)
        plt.subplot(2, 2, 1)
        group_means = df.groupby('species').mean()
        for column in group_means.columns:
            plt.plot(group_means.index, group_means[column], marker='o', label=column)
        plt.title('Average Measurements by Species')
        plt.xlabel('Species')
        plt.ylabel('Measurement (cm)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        
        # 2. Bar chart (average sepal length by species)
        plt.subplot(2, 2, 2)
        sns.barplot(x='species', y='sepal length (cm)', data=df)
        plt.title('Average Sepal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Sepal Length (cm)')
        
        # 3. Histogram (petal length distribution)
        plt.subplot(2, 2, 3)
        sns.histplot(data=df, x='petal length (cm)', bins=20, kde=True)
        plt.title('Distribution of Petal Length')
        plt.xlabel('Petal Length (cm)')
        plt.ylabel('Count')
        
        # 4. Scatter plot (sepal length vs petal length)
        plt.subplot(2, 2, 4)
        sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                       hue='species', size='species', sizes=(50, 200))
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Save the plot
        plt.tight_layout()
        plt.savefig('iris_visualizations.png')
        plt.close()
        
        print("\nVisualizations created and saved as 'iris_visualizations.png'")
        print("Visualization Insights:")
        print("- Line plot shows clear differences in measurements across species")
        print("- Bar plot indicates setosa has shortest average sepal length")
        print("- Histogram shows petal length has a multimodal distribution")
        print("- Scatter plot reveals distinct clusters for each species")
        
    except Exception as e:
        print(f"Error in visualization: {str(e)}")

# Main execution
if __name__ == "__main__":
    # Load and explore
    df = load_and_explore_data()
    
    # Analyze
    group_means = analyze_data(df)
    
    # Visualize 
    create_visualizations(df)
