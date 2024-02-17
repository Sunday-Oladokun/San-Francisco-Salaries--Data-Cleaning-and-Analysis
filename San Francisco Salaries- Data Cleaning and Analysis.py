#!/usr/bin/env python
# coding: utf-8

# In[51]:


# Import pandas packages
import pandas as pd


# In[52]:


# Read the csv file
salaries_data = pd.read_csv("Salaries.csv")


# In[53]:


# Get a general overview if the imported dataset
salaries_data.info()


# In[54]:


# Check the top 5 rows of the dataset
salaries_data.head()


# ### DATA CLEANING

# Before analysing our data, let us take a look at a general overview of the data and see if there are null values, wrong data types etc

# In[55]:


salaries_data.info()


# The dataset contains 13 columns and 148654 entries for the columns. 
# 
# Looking at some of the columns such as Benefits, BasePay, Notes, and Status, we can already see that we have missing data as they are not up to 148654 entries.
# 
# Also, some of the columns have mismatched data types, a good example would be BasePay, OvertimePay, OtherPay, Benefits which are supposed to be floats so we can carry out quantitative analysis on them but they are in object form.
# 
# Lastly, we have the notes column which is not needed and that has even been made evident by the fact that it has zero entry.

# In[56]:


# Let us break the dataset into two categories- the columns with properly matched data types and the one that is mismatched

# Subsetting the columns with proper data types
proper_df = salaries_data[["Id", "EmployeeName", "JobTitle", "TotalPay", "TotalPayBenefits", "Year", "Agency", "Status"]]


# In[57]:


# Viewing the proper dataset
proper_df.head()


# In[58]:


# Subsetting the columns with improper data types
improper_df = salaries_data[["BasePay", "OvertimePay", "OtherPay", "Benefits", "Notes"]]


# In[59]:


# Viewing the improper dataset
improper_df.head()


# In[60]:


# Correcting the improper columns from object data types to numeric data types
improper_df_corrected = improper_df.apply(pd.to_numeric, errors="coerce")


# In[61]:


# Let us take a look at the corrected improper columns to see their data types
improper_df_corrected.info()


# Now that our columns with mismatched data types have been corrected, it is time to join the dataset back together and continue our data cleaning exercise

# In[62]:


# Concatenate the two datasets together
proper_salaries_data = pd.concat([proper_df, improper_df_corrected], axis=1)


# In[63]:


# Let us take a look at our dataset
proper_salaries_data.head()


# In[64]:


# From the info below, we now have the data types correctly matched to the columns
proper_salaries_data.info()


# In[65]:


# Shape of the proper dataset
shape = proper_salaries_data.shape
print("Number of rows:",shape[0])
print("Number of columns:",shape[1])


# In[66]:


# Let us handle missing data

# Check null data for each column
proper_salaries_data.isna().sum()


# In[67]:


# Let us put the null values in percentages and qauntify it relatively
def percentage_null(data):
    missing_percentages = {}
    total_rows = len(data)
    for column in data:
        missing_count = data[column].isnull().sum()
        missing_percent = (missing_count / total_rows) * 100
        missing_percentages[column] = missing_percent
    return missing_percentages


# In[68]:


percentage_null(proper_salaries_data)


# The following columns would be dropped and the reasons are stated below as well:
# 1. ID: This is the employee ID which is not exactly needed for the type of questions we aim to answer with this data and besides, the index values can substitute for it
# 2. Notes: Notes has zero entries, it does not have any data to be analysed
# 3. Agency: The agency column has just one single entry and that is San Francisco. The data is for San Francisco, there is no need repeating that in the dataset
# 4. Status: Out of 148654 entries that we are supposed to have for status column, over 70% of the data is missing and that is a very high number. Whatever data filling method we use, It would not represent the true state of things so its better to drop it.

# In[69]:


# Drop the ID, Notes, Agency, and Status columns and assign the datafram to a new variable since I am not dropping inplace
proper_salaries_data2 = proper_salaries_data.drop(["Id", "Notes", "Agency", "Status"], axis=1)


# In[70]:


proper_salaries_data2


# In[71]:


proper_salaries_data2.info()


# In[72]:


# We have a couple of rows where EmployeeName, JobTitle, and Payment details were not provided, we should drop them
proper_salaries_data2[(proper_salaries_data2["EmployeeName"] == "Not provided") & 
                      (proper_salaries_data2["JobTitle"] == "Not provided")]


# In[73]:


proper_salaries_data2.drop(proper_salaries_data2[(proper_salaries_data2["EmployeeName"] == "Not provided") & 
                                                 (proper_salaries_data2["JobTitle"] == "Not provided")].index, inplace=True)


# In[74]:


proper_salaries_data2.info()


# In[75]:


# Shockingly, we still have occurrencies of missing data from BasePay, OvertimePay, OtherPay, and Benefits
# They are numerical values and we could fill the missing values with the median values

median_BasePay = proper_salaries_data2["BasePay"].median()
median_OvertimePay = proper_salaries_data2["OvertimePay"].median()
median_OtherPay = proper_salaries_data2["OtherPay"].median()
median_Benefits = proper_salaries_data2["Benefits"].median()

proper_salaries_data2["BasePay"] = proper_salaries_data2["BasePay"].fillna(median_BasePay)
proper_salaries_data2["OvertimePay"] = proper_salaries_data2["OvertimePay"].fillna(median_OvertimePay)
proper_salaries_data2["OtherPay"] = proper_salaries_data2["OtherPay"].fillna(median_OtherPay)
proper_salaries_data2["Benefits"] = proper_salaries_data2["Benefits"].fillna(median_Benefits)


# In[76]:


proper_salaries_data2.info()
# Finally, we have a clean data


# ### EXPLORATORY DATA ANALYSIS

# In[77]:


# Find occurence of the employee names (Top 5)
proper_salaries_data2["EmployeeName"].value_counts(sort=True).head()


# In[78]:


# Find the unique job titles
proper_salaries_data2["JobTitle"].unique()


# In[79]:


# Find the number of unique job titles
proper_salaries_data2["JobTitle"].nunique()


# In[105]:


# Total number of jobs that contain "Captain"
proper_salaries_data2["JobTitle"].str.contains("CAPTAIN", case=False).sum()


# In[81]:


# Display top 5 employee names from fire department
proper_salaries_data2[proper_salaries_data2["JobTitle"].str.contains("fire",case=False)]["EmployeeName"].head()


# In[82]:


# Maximum, Minimum, and Average Base Pay
proper_salaries_data2["BasePay"].describe()


# In[84]:


# Find the job title of Albert Pardini
proper_salaries_data2[proper_salaries_data2["EmployeeName"] == "ALBERT PARDINI"]["JobTitle"]


# In[85]:


# How much does he make, including benefits
proper_salaries_data2[proper_salaries_data2["EmployeeName"] == "ALBERT PARDINI"]["TotalPayBenefits"]


# In[86]:


# Highest basepay
proper_salaries_data2["BasePay"].max()


# In[87]:


# Index of employee with the highest basepay
max_basepay = proper_salaries_data2["BasePay"].idxmax()
max_basepay


# In[88]:


# Employee with the highest basepay
proper_salaries_data2[proper_salaries_data2["BasePay"].max() == proper_salaries_data2["BasePay"]]["EmployeeName"]


# In[89]:


# Average BasePay of all employee by year
proper_salaries_data2.groupby("Year")["BasePay"].mean()


# In[90]:


# Average BasePay of all employee by per job title
proper_salaries_data2.groupby("JobTitle")["BasePay"].mean()


# In[91]:


# Average BasePay of all employee with job title accountant
proper_salaries_data2[proper_salaries_data2["JobTitle"] == "ACCOUNTANT"]["BasePay"].mean()


# In[95]:


# Top 5 most common jobs
proper_salaries_data2["JobTitle"].value_counts(sort=True).head()


# In[100]:


# Percentage of each Job title
proper_salaries_data2["JobTitle"].value_counts(sort=True, normalize=True) * 100


# In[94]:


# Export cleaned data
proper_salaries_data2.to_csv("Salaries Data.csv")

