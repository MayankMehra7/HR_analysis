import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/MAYANK/Downloads/MLSA/Employee_HR.csv") # load training
print(df.columns)
print(df.isnull().sum().sum())

#1 calculate the variance, standard deviation, and interquartile range (IQR) of the salaries of employees in the HR and Marketing departments

variance = df['Salary_INR'].var()
std_deviation = df['Salary_INR'].std()

# Calculate interquartile range (IQR) for salaries
Q1, Q3=np.percentile([df["Salary_INR"]], [25 ,75])
iqr=(Q3-Q1)*100
print(f"Variance of Salaries: {variance}")
print(f"Standard Deviation of Salaries: {std_deviation}")
print(f"Interquartile Range (IQR) of Salaries: {iqr}")

#2 Calculate the range of experience in the IT department
it_department = df[df['Department'] == 'IT']
experience_range = it_department['time_spent_company'].max() - it_department['time_spent_company'].min()

print(f"The range of experience in the IT department is {experience_range} years.")
#3
plt.figure(figsize=(10,2))
sns.boxplot(x="Department", y='time_spent_company', data=df).set_title("Box Plot - Department vs Time Spent")
plt.show()

#4
std_deviations_HG = df.std()
# Find the feature with the highest standard deviation
highest_std_feature = std_deviations_HG.idxmax()

print(f"The feature with the highest standard deviation is: {highest_std_feature}")