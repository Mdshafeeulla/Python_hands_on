# Exercise 8: DataFrame Plotting
#
# Data Preparation
# Start with a sales DataFrame containing product categories and sales figures
#
# Aggregation
# Calculate total sales per product category
#
# Visualisation
# Using Matplotlib or Pandas plotting, create a bar chart displaying the results

import matplotlib.pyplot as plt
import pandas as pd

data = {
        'Product': ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam', 'Laptop', 'Monitor'],
        'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Peripherals', 'Electronics', 'Electronics'],
        'Sales_Amount': [1200, 50, 350, 25, 75, 900, 450]
    }
df = pd.DataFrame(data)

total_sales = df.groupby('Category')['Product'].sum()
print(total_sales)
