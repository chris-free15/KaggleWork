
"""
Order By
    - usually the lasts clause in your query
    - sorts the results returned by other part of the query
"""

# Dates
"""
Date
data types:
    - DATE, DATETIME
DATE
    - YYYY-[M]M-[D]D
    - YYYY: Four-digit year
    - [M]M: One or two digit month
    - [D]D: One or two digit day
    
DATETIME
    - same format, but with time added at the end
    
EXTRACT
    SELECT Name, EXTRACT(DAY from Date) AS Day
    SELECT Name, Extract(WEEK from Date) AS Week
"""


# Query to find out the number of accidents for each day of the week
query = """
        SELECT COUNT(consecutive_number) AS num_accidents, 
               EXTRACT(DAYOFWEEK FROM timestamp_of_crash) AS day_of_week
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
        GROUP BY day_of_week
        ORDER BY num_accidents DESC
        """

# Exercises

"""
1.
Which countries spend the largest fraction of GDP on education?

To answer this question, consider only the rows in the dataset corresponding to indicator code SE.XPD.TOTL.GD.ZS, and write a query that returns the average value in the value column for each country in the dataset between the years 2010-2017 (including 2010 and 2017 in the average).

Requirements:

Your results should have the country name rather than the country code. You will have one row for each country.
The aggregate function for average is AVG(). Use the name avg_ed_spending_pct for the column created by this aggregation.
Order the results so the countries that spend the largest fraction of GDP on education show up first.


# Your code goes here
country_spend_pct_query = \"""
                          SELECT country_name, AVG(value) AS avg_education_spending_perecent
                          FROM `bigquery-public-data.world_bank_intl_education.international_education`
                          WHERE indicator_code = 'SE.XPD.TOTL.GD.ZS' and year >= 2010 and year <= 2017
                          GROUP BY country_name
                          ORDER BY avg_ed_spending_pct DESC
                          \"""

# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
country_spend_pct_query_job = client.query(country_spend_pct_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
country_spending_results = country_spend_pct_query_job.to_dataframe()

# View top few rows of results
print(country_spending_results.head())

# Check your answer
q_1.check()
"""

"""
2.
The last question started by telling you to focus on rows with the code SE.XPD.TOTL.GD.ZS. But how would you find more interesting indicator codes to explore?

There are 1000s of codes in the dataset, so it would be time consuming to review them all. But many codes are available for only a few countries. When browsing the options for different codes, you might restrict yourself to codes that are reported by many countries.

Write a query below that selects the indicator code and indicator name for all codes with at least 175 rows in the year 2016.

Requirements:

You should have one row for each indicator code.
The columns in your results should be called indicator_code, indicator_name, and num_rows.
Only select codes with 175 or more rows in the raw database (exactly 175 rows would be included).
To get both the indicator_code and indicator_name in your resulting DataFrame, you need to include both in your SELECT statement (in addition to a COUNT() aggregation). This requires you to include both in your GROUP BY clause.
Order from results most frequent to least frequent.

# Your code goes here
code_count_query = \"""
                   SELECT indicator_code, indicator_name, COUNT(1) AS num_rows
                   FROM `bigquery-public-data.world_bank_intl_education.international_education`
                   WHERE year = 2016
                   GROUP BY indicator_name, indicator_code
                   HAVING COUNT(1) >= 175
                   ORDER BY COUNT(1) DESC
                   \"""

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
code_count_query_job = client.query(code_count_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
code_count_results = code_count_query_job.to_dataframe()

# View top few rows of results
print(code_count_results.head())

# Check your answer
q_2.check()
"""