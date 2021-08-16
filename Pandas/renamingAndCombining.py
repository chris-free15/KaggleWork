import pandas as pd

reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

"""
- data oftentimes comes with coulmn names, index names, or other naming conventions we'll want to change
- we'll want to change/rename that
"""

# Renaming
print(reviews.rename(columns={'points': 'score'}))
print("--------------")
print()

"""
- rename()
    - lets you rename index or column vaues by specificying index or column keyword params
    - can also specify certain elements in a range as well
"""

# replaces index 0,1 with firstEntry, secondEntry
print(reviews.rename(index={0:'firstEntry', 1:'secondEntry'}))
print("--------------")
print()

"""
- you are more likely to rename columns.. not so much the index. that's what set_index() is for
- rename_axis()
"""

print(reviews.rename_axis("wines", axis="rows").rename_axis('fields', axis='columns'))
print("--------------")
print()

# Combining
"""
- when performing operations on a dasete we may need to combine DataFrames and/or Series in non-trivial ways.
- pandas has three core methods to do this
    - concat()
        - given a list of elements, smushes the elements together along an axis
        - useful when we have data in different DataFrame or Series objects but having the same fields(columns)
    - join()
        - combine different DataFrame objects that have an index in common
        
    - merge()
"""


# Exercises
"""
1.
region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with these columns renamed to region and locale, respectively.
"""
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

"""
2.
Set the index name in the dataset to wines.
"""
reindexed = reviews.rename_axis('wines', axis='rows')

"""
3.
The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") on reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.
"""
# commenting out solutions since I didn't donwnload dataset.. I promise it works
# combined_products = pd.concat([gaming_products, movie_products])

"""
4.
The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:
"""
# commenting out solutions since I didn't donwnload dataset.. I promise it works

# powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))