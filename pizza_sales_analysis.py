# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:18:36 2024

@author: Alex Alkhatib
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


# =============================================================================
# Read the Excel files
# =============================================================================

pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_size_df = pd.read_csv('pizza_size.csv')
pizza_category_df = pd.read_csv('pizza_category.csv')



# =============================================================================
# Viewing top and bottom rows in a DataFrame
# =============================================================================

pizza_sales_df.head()
pizza_sales_df.tail()

# Describing the data
pizza_description = pizza_sales_df.describe()

# Have a look at non-null counts per column
pizza_sales_df.info()

# Count the number of null values in each column
null_count = pizza_sales_df.isnull().sum()

# Check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()

# =============================================================================
# Dealing with Rows and Columns in Pandas
# =============================================================================

# To select a column
quantity_column = pizza_sales_df['quantity']

# Extract quantity, unit price and order ID
selected_columns = pizza_sales_df[[ 'order_id', 'quantity', 'unit_price']]

# Get the row with index label 3
row = pizza_sales_df.loc[3]

# Get two rows indexlabel 3 and 5
rows = pizza_sales_df.loc[[3,5]]

# Get rows between index labels 3 and 5
subset = pizza_sales_df.loc[3:5]

# Get rows between index labels 3 and 5 and specific columns
subset2 = pizza_sales_df.loc[3:5, ['order_id', 'quantity', 'unit_price']]

# =============================================================================
# Understanding Indexing in DataFrames
# =============================================================================
 
# Set an index as a column in a DataFrame
pizza_sales_df.set_index('order_details_id', inplace=True)

# Reseting an index
pizza_sales_df.reset_index(inplace=True)


# =============================================================================
# Truncating DataFrames and Series
# =============================================================================

# Truncate DataFrame before index 3
truncated_before = pizza_sales_df.truncate(before=3)

# Truncate DataFrame after index 5
truncated_after = pizza_sales_df.truncate(after=5)

# Truncating columns
quantity_series = pizza_sales_df['quantity']

# Truncate quantity series before index 3
truncated_series_before = quantity_series.truncate(before=3)

# Truncate series after index 5
truncate_series_after = quantity_series.truncate(after=5)

# =============================================================================
# Filtering DataFrame
# =============================================================================

# Basic filtering
# I want to filter rows to see pizzas where unit price is greater than 20
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filter on a date
# Change the order date from datetime to date
pizza_sales_df['order_date'] = pizza_sales_df['order_date'].dt.date

# Filter pizza where the date > 2015-12-15
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[ pizza_sales_df['order_date'] > date_target]

# Combine conditions
# See rows where unit price > 15 and the pizza name needs to be 'The Barbecue Chicken Pizza'
bbq_chicken_rows = pizza_sales_df[
    (pizza_sales_df['unit_price'] > 15) & 
    (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')
    ]

# Using the or condition
bbq_chicken_rows_or = pizza_sales_df[
    (pizza_sales_df['unit_price'] > 15) |
    (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')
    ]

# Filter a specific range
high_sales = pizza_sales_df[
    (pizza_sales_df['unit_price'] > 15) &
    (pizza_sales_df['unit_price'] <= 20)
    ]

# =============================================================================
# Working with Missing Data
# =============================================================================

# Dropping null values
pizza_sales_null_values_dropped = pizza_sales_df.dropna()
null_count = pizza_sales_null_values_dropped.isnull().sum()

# Replacing null with a specific value
datena_fill = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(datena_fill)

# =============================================================================
#  Drop specific row
# =============================================================================

# Deleting specific rows and columns in a DataFrame (Drop row n°2)
filtered_rows_2 = pizza_sales_df.drop(2, axis=0)

# Deleting rows 5,7,9
filtered_rows_5_7_9 = pizza_sales_df.drop([5,7,9], axis=0)

# Drop specific columns by name
filtered_unit_price = pizza_sales_df.drop('unit_price', axis=1)

# Drop multiple columns
filtered_unit_price_and_order_id = pizza_sales_df.drop(['unit_price', 'order_id'], axis=1)


# =============================================================================
# Sorting DataFrame
# =============================================================================

# Sorting in a descending order
sorted_df = pizza_sales_df.sort_values('total_price', ascending=False)

# Sorting in an ascending order
sorted_df = pizza_sales_df.sort_values('total_price')

# Sort by multiple columns
sorted_multiple_df = pizza_sales_df.sort_values(['pizza_category_id', 'total_price'],
                                                ascending=[True, False])


# =============================================================================
# Grouping By
# =============================================================================

# Group by pizza size id and get the count of sales (row count)
grouped_df_pizza_size = pizza_sales_df.groupby(['pizza_size_id']).count()
grouped_df_pizza_size = grouped_df_pizza_size.sort_values(['pizza_size_id'], ascending=False)

# Group by pizza size id and get the sum
grouped_by_pizza_size_sum = pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()
grouped_by_pizza_size_sum = grouped_by_pizza_size_sum.sort_values(ascending=False)

# Group by pizza size id and sum_total_price and quantity
grouped_df_pizza_size_sales_quantity = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

# Looking at different aggregation functions
# Count(), Sum(), mean(), std(), var(), min(), max(), prod(), first(), size(), numerique()

# Using agg to perform different aggregations on different columns
aggregated_data = pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity' : 'sum', 'total_price' : 'mean'})


# =============================================================================
# Merging and Concatenating
# =============================================================================

# Merging pizza sales df and pizza size df
merged_df = pd.merge(pizza_sales_df, pizza_size_df, on='pizza_size_id')

# Add category information
merged_df = pd.merge(merged_df, pizza_category_df, on='pizza_category_id')

# Concatenate two dataframes - appending rows to a data frame - vertically
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx') 
concatenate_vertically = pd.concat([pizza_sales_df, another_pizza_sales_df])
concatenate_vertically = concatenate_vertically.reset_index() 

# Concatenate two data frames - horizontally
pizza_sales_voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')
concatenate_horizontally = pd.concat([pizza_sales_df, pizza_sales_voucher_df], axis=1)


# =============================================================================
# Changing case in Python
# =============================================================================

# Converting to lower case
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.lower()

# Converting to upper case
upper_text = pizza_sales_df['pizza_ingredients'].str.upper()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.upper()

# Converting to title case
title_text = pizza_sales_df['pizza_ingredients'].str.title()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.title()


# =============================================================================
# Replacing text values
# =============================================================================

replaced_text = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')

# Removing extra white spaces
pizza_sales_df['pizza_name'] = pizza_sales_df['pizza_name'].str.strip()


# =============================================================================
# Generating Boxplot
# =============================================================================

sns.boxplot(x= 'category', y= 'total_price', data= merged_df)
plt.xlabel('Pizza Category')
plt.ylabel('Total Price')
plt.title('Boxplot showing distribution of sales by category')
plt.show()


