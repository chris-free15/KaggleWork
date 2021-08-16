import pandas as pd

"""
map
    - allows transformations among data in a DataFrame or Series one value at a time for entire column

groupwise analysis
    - want to do something specific to the group of data
"""

reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
pd.set_option("display.max_rows", 10)

# value_counts() wrote manually
print(reviews.groupby('points').points.count())
print("--------------")
print()
"""
 groupby()
    - created a group of reviews which alloted the same point values to the given wines
        - then for each groups we called points() column and counted how many times it appears
    - returns a groupby dataframe object
"""


# can recreate the summary functions we've created before using groupby()
print(reviews.groupby('points').price.min())
# the minimum priced wine for each point rating
print("--------------")
print()

"""
- can think of each group as a slice of the DataFrame containing only data values that match.
"""

# example of selecting thename of the first wine reviewed from each winery in the dataset
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
print("--------------")
print()

# can also group by more than one column
# best wine by country and province
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
print("--------------")
print()

"""
another helpful groupby() method
    - agg()
        - run a buynch of different functions on a DataFrame simultaneously
"""
print(reviews.groupby(['country']).price.agg([len, min, max]))
print("--------------")
print()

# Multi-indexes
"""
https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
- multiple levels
- require two levels of labels to retrieve a value
- has methods for dealing iwth multi-index objects
- can quickly convert back to a regular index with reset_index()
"""
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# 425 rows x 1 column (multi-indexed)
# country, province, len all 1 column
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi))
print("---------------")
print()

# Sorting
"""
groupby()
    - returned data in index order, not in value order
    
sort_values()
    - allows us to sort the data by value instead of index
"""
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
# can also do descending order. ascending is default
# countries_reviewed.sort_values(by='len', ascending=False)
print(countries_reviewed)
print("-------------")
print()

# can revert back to sorting by index
# countries_reviewed.sort_index()

# we can also sort by more than one column at a time
print(countries_reviewed.sort_values(by=['country', 'len']))
print("------------------")
print()


# Exercises
"""
1.
Who are the most common wine reviewers in the dataset? Create a Series whose index is the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote.
"""
reviews_written = reviews.groupby(['taster_twitter_handle']).size()
# or
reviews_written = reviews.groupby(['taster_twitter_handle']).taster_twitter_handle.count()

"""
2.
What is the best wine I can buy for a given amount of money? Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
"""
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

"""
3.
What are the minimum and maximum prices for each variety of wine? Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.
"""
price_extremes = reviews.groupby('variety').price.agg([min,max])

"""
4.
What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).
"""
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

"""
5.
Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the taster_name and points columns.
"""
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

"""
6.
What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs. For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.
"""
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)
