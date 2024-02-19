# San-Francisco-Salaries--Data-Cleaning-and-Analysis

A lot of people in the data science space and people I look up to have always said that the bulk of every data scientists’ work lies in data cleaning owing largely to the fact that it affects the kind of insights that we can drive from data and ultimately- the kind of model we build using the data.

Data cleaning is the bedrock of everything and this particular project really exposed me to that, I spent over 2 hours cleaning and validating the values in this data until I was confident that it was clean enough to answer some of the questions I prepared for this project.

Before analyzing the data, I took a look at the general overview of the data to see the kind of data cleaning that would be carried out. The dataset contains 13 columns and 148654 entries. 

Looking at some of the columns such as Benefits, BasePay, Notes, and Status, I could already see that we have missing data as they are not up to 148654 entries. Also, some of the columns have mismatched data types, a good example would be BasePay, OvertimePay, OtherPay, Benefits which are supposed to be floats so we can carry out quantitative analysis on them but they are in object form.

Lastly, we have the notes column which is not needed and that has even been made evident by the fact that it has zero entry so I dropped it.
The following columns were also dropped and the reasons are stated below as well:
1. ID: This is the employee ID which is not exactly needed for the type of questions we aim to answer with this data and besides, the index values can substitute for it
2. Notes: Notes has zero entries, it does not have any data to be analyzed
3. Agency: The agency column has just one single entry and that is San Francisco. The data is for San Francisco, there is no need repeating that in the dataset
4. Status: Out of 148654 entries that we are supposed to have for status column, over 70% of the data is missing and that is a very high number. Whatever data filling method we use, it would not represent the true state of things so it’s better to drop it.

## After the data was cleaned successfully, I answered the following questions:

1.	Find occurrence of the employee names (Top 5)
2.	Find the unique job titles
3.	Total number of jobs that contain "Captain"
4.	Display top 5 employee names from fire department
5.	Find the job title of Albert Pardini
6.	How much does he make, including benefits
7.	Highest basepay
8.	Index of employee with the highest basepay
9.	Employee with the highest basepay
10.	Average BasePay of all employee by year
11.	Average BasePay of all employee per job title
12.	Average BasePay of all employee with job title accountant
13.	Top 5 most common jobs
14.	Percentage of each Job title

Thank you for reading.
