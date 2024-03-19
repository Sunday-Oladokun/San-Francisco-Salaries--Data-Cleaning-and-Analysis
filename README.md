# San Francisco Salaries: Data Cleaning and Analysis

## Introduction

Data cleaning is often regarded as the cornerstone of any data science endeavor, shaping the quality of insights derived and the efficacy of subsequent modeling efforts. This project delves into the meticulous process of cleaning and analyzing a dataset sourced from the city of San Francisco's salaries data.

## Data Cleaning Process

The dataset, comprising 13 columns and 148,654 entries, underwent extensive cleaning to ensure its integrity for analysis. Notable observations included missing data in columns such as Benefits, BasePay, Notes, and Status, alongside mismatched data types in certain columns like BasePay, OvertimePay, OtherPay, and Benefits.

The following columns were dropped due to redundancy or lack of relevance:
1. ID: Redundant for analysis purposes, as index values suffice.
2. Notes: Devoid of entries, rendering it unnecessary.
3. Agency: Contains only a single entry, San Francisco, redundant for a dataset pertaining solely to the city.
4. Status: Over 70% missing data, originating from Transparent California's dataset without provisions for the Status column.

## Analysis Questions Addressed

Upon successful data cleaning, the following questions were addressed:
1. Occurrence of the top 5 employee names.
2. Identification of unique job titles.
3. Total number of jobs containing "Captain."
4. Top 5 employee names from the fire department.
5. Job title of Albert Pardini.
6. Total earnings of Albert Pardini, including benefits.
7. Highest base pay recorded.
8. Index of the employee with the highest base pay.
9. Employee with the highest base pay.
10. Average BasePay of all employees by year.
11. Average BasePay of all employees per job title.
12. Average BasePay of all employees with the job title "Accountant."
13. Top 5 most common job titles.
14. Percentage breakdown of each job title.

## Conclusion

Through meticulous data cleaning and analysis, valuable insights were gleaned from the San Francisco salaries dataset. This project underscores the importance of rigorous data preprocessing in unlocking meaningful insights and informing evidence-based decision-making processes.

Thank you for reading.