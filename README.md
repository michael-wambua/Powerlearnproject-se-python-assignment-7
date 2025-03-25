Task 1: Data Exploration

    I used the Iris dataset from the seaborn library, which is a well-known dataset for machine learning and data analysis.
    The explore_dataset() function:
    
    Displays the first 5 rows of the dataset
    Provides information about data types and columns
    Checks for missing values (in this case, there are none)



Task 2: Basic Data Analysis
    
    The perform_data_analysis() function:
    
    Computes basic descriptive statistics using .describe()
    Groups the data by species and calculates mean values for each numerical column
    Helps identify differences in measurements across different iris species
    


Task 3: Data Visualization
    I created four different visualizations:
    
    Line Chart: Shows trends of sepal and petal length across samples
    Bar Chart: Displays average petal length for each iris species
    Histogram: Shows the distribution of sepal width
    Scatter Plot: Illustrates the relationship between sepal length and petal length, colored by species

Key Observations

    The dataset contains measurements for three iris species: setosa, versicolor, and virginica
    Each species has distinct characteristics in terms of sepal and petal measurements
    The scatter plot reveals clear separation between species based on sepal and petal measurements

Note: To run this code, you'll need to:

    Install required libraries: pandas, matplotlib, seaborn
    Have an active internet connection to load the dataset from GitHub


Expected outcome

    PS D:\PLP> & C:/Users/slymi/AppData/Local/Programs/Python/Python313/python.exe d:/PLP/analyze.py
    1. First 5 rows of the dataset:
       sepal_length  sepal_width  petal_length  petal_width species
    0           5.1          3.5           1.4          0.2  setosa
    1           4.9          3.0           1.4          0.2  setosa
    2           4.7          3.2           1.3          0.2  setosa
    3           4.6          3.1           1.5          0.2  setosa
    4           5.0          3.6           1.4          0.2  setosa
    
    2. Dataset Information:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal_length  150 non-null    float64
     1   sepal_width   150 non-null    float64
     2   petal_length  150 non-null    float64
     3   petal_width   150 non-null    float64
     4   species       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    None
    
    3. Check for Missing Values:
    sepal_length    0
    sepal_width     0
    petal_length    0
    petal_width     0
    species         0
    dtype: int64
    
    1. Basic Statistics:
           sepal_length  sepal_width  petal_length  petal_width
    count    150.000000   150.000000    150.000000   150.000000
    mean       5.843333     3.057333      3.758000     1.199333
    std        0.828066     0.435866      1.765298     0.762238
    min        4.300000     2.000000      1.000000     0.100000
    25%        5.100000     2.800000      1.600000     0.300000
    50%        5.800000     3.000000      4.350000     1.300000
    75%        6.400000     3.300000      5.100000     1.800000
    max        7.900000     4.400000      6.900000     2.500000
    
    2. Grouping by Species:
                sepal_length  sepal_width  petal_length  petal_width
    species
    setosa             5.006        3.428         1.462        0.246
    versicolor         5.936        2.770         4.260        1.326
    virginica          6.588        2.974         5.552        2.026


An graph output
A visualization output is included

