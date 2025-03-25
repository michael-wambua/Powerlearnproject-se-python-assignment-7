import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Task 1: Data Exploration
def explore_dataset(df):
    print("1. First 5 rows of the dataset:")
    print(df.head())
    
    print("\n2. Dataset Information:")
    print(df.info())
    
    print("\n3. Check for Missing Values:")
    print(df.isnull().sum())
    
    # Clean the dataset (if needed)
    # In this case, there are no missing values
    
    return df

# Task 2: Basic Data Analysis
def perform_data_analysis(df):
    print("\n1. Basic Statistics:")
    print(df.describe())
    
    print("\n2. Grouping by Species:")
    grouped_stats = df.groupby('species')[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
    print(grouped_stats)
    
    return grouped_stats

# Task 3: Data Visualization
def create_visualizations(df):
    plt.figure(figsize=(15, 10))
    
    # Line Chart (Simulated time series using index)
    plt.subplot(2, 2, 1)
    df[['sepal_length', 'petal_length']].plot(title='Sepal and Petal Length Trends')
    plt.xlabel('Sample Index')
    plt.ylabel('Length')
    
    # Bar Chart
    plt.subplot(2, 2, 2)
    df.groupby('species')['petal_length'].mean().plot(kind='bar', title='Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.xticks(rotation=45)
    
    # Histogram
    plt.subplot(2, 2, 3)
    df['sepal_width'].hist(bins=20, title='Distribution of Sepal Width')
    plt.xlabel('Sepal Width')
    plt.ylabel('Frequency')
    
    # Scatter Plot
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
    plt.title('Sepal Length vs Petal Length')
    
    plt.tight_layout()
    plt.show()

# Execute the analysis
explored_data = explore_dataset(iris_data)
analysis_results = perform_data_analysis(explored_data)
create_visualizations(explored_data)
