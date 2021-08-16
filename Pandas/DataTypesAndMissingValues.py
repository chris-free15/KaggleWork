import pandas as pd

"""
- dtype shorthand for data type
- dtype(object) returns the data type

- can use dtype to grab the specific type of column
"""

reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

print(reviews.price.dtype)
print("------------")
print()

# can also get the data types for every column
print(reviews.dtypes)
print("------------")
print()

# you can convert the data type of one column into another type
reviews.points.astype('float64')

"""
- pandas also supports more data types such as categorical, timeseries, etc
"""

# Missing Data

"""
- Entries missing values are given Nan
    - remember pd.isnull() or pd.notnull()
"""
print(reviews[pd.isnull(reviews.country)])
print("------------")
print()

"""
- replacing missing values is a common operation
- fillna()
"""

print(reviews.region_2.fillna("Unknown"))
print("-----------------")
print()

"""
- alternatively, you may have a non-null value that we would like to replace. 
- example
    - changing twitter handles
- replace()
"""
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))
print("-----------------")
print()

# Exercise
"""
1.
What is the data type of the points column in the dataset?
"""
dtype = reviews.points.dtype

"""
2.
Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.
"""
point_strings = reviews.points.astype('str')


"""
3.
Sometimes the price column is null. How many reviews in the dataset are missing a price?
"""
n_missing_prices = reviews.price.isnull().sum()


"""
4.
What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending order. Your output should look something like this:
"""
reviews_per_region = reviews.region_1.fillna("Unkown").value_counts().sort_values(ascending=False)