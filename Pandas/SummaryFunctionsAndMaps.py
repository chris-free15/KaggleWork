import pandas as pd

"""
- Summary functions
    - statistics across parts of your data
    - describe()
"""

reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

print(reviews.points.describe())
# high-level summary of attributes.
# count, mean, std, etc. for numerical data obv
print("------------")
print()

print(reviews.taster_name.describe())
# string data.. unique, top, frequency
print("------------")
print()

"""
helpful pandas functions available in DataFrame or a series
mean, unique, value_counts
"""

print(reviews.points.mean())
print("------------")
print()

print(reviews.taster_name.unique())
print("------------")
print()

print(reviews.points.value_counts())
print("------------")
print()

# Maps
"""
map()
    - map a function to certain values
    - expects a single value from the series and returns a transformed version of that value
    *- returns a new Series where all the values have been transformed by function
apply()
    - transform a whole DataFrame by calling a custom function on each row
    *- returns a new DataFrame
"""

# remean score where wines received 0
# example of map
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))
print("------------")
print()


def remean_points(row):
    row.points = row.points - review_points_mean
    return row


reviews.apply(remean_points, axis='columns')
#
print(reviews)
print("------------")
print()


"""
- Can also you standard operations between Series of equal length
    - can be faster than using map() or apply(), but not as verbose
    - >, <, ==, and so on
"""
reviews_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)
print("------------")
print()

# Exercises
"""
1.
What is the median of the points column in the reviews DataFrame?
"""
median_points = reviews.points.median()

"""
2.
What countries are represented in the dataset? (Your answer should not include any duplicates.)
"""
countries = reviews.country.unique()

"""
3.
How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
"""
reviews_per_country = reviews.country.value_counts()

"""
4.
Create variable centered_price containing a version of the price column with the mean price subtracted.

(Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.)
"""
centered_price = reviews.price - reviews.price.mean()

"""
5.
I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
"""
# idxmax() returns max value
bargain_index = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_index, 'title']
print(bargain_wine)

"""
6.
There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series descriptor_counts counting how many times each of these two words appears in the description column in the dataset.
"""
# want a series with # of tropical, fruity
tropical_count = reviews.description.map(lambda words: "tropical" in words).sum()
fruity_count = reviews.description.map(lambda words: "fruity" in words).sum()
descriptor_counts = pd.Series([tropical_count, fruity_count], index=["tropical", "fruity"])

"""
7.
We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

Create a series star_ratings with the number of stars corresponding to each review in the dataset.
"""
def calculate_star(row):
    if row.country == "Canada":
        return 3
    if row.points >= 95:
        return 3
    elif row.points >= 85 and row.points < 95:
        return 2
    else:
        return 1
star_ratings = reviews.apply(calculate_star, axis='columns')
print()
print(star_ratings)