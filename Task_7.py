# Exercise 7: Pandas DataFrame Filtering
#
# Dataset
# DataFrame of employee data containing name, department, and salary fields
#
# Task
# Filter and return all employees with salary above the 75th percentile
#
# Skills
# Statistical analysis, DataFrame filtering, percentile calculation
import pandas as pd
data = {
    "Name":["Ali","George","Amar","Thomas","Hamza"],
    "Department":["IT","Sales","IT","Sales","HR"],
    "Salary":[50000,20000,40000,30000,70000]
}
df = pd.DataFrame(data)
print(f"{df}\n")
greater_than_75_percentile = df['Salary'].quantile(0.75)
high_earners = df['Salary'] > greater_than_75_percentile
print(df[high_earners])