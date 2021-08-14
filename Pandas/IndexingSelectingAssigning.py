import pandas as pd

reviews = pd.read_csv("../winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)

"""
- * Just like Python objects, Pandas carries over native accessors (attributes of the object)

- can access with object notation or indexing

- indexing has advantages
    - reserved characters are accessible via reviews['bad name']
    - can index certain values reviews['country][1:50]
- pandas is pretty much a fancy dictionary
"""

print(reviews.country)
print("----------------")
print()

print(reviews['country'])
print("----------------")
print()

# Indexing In Pandas

"""
- index-based selection: (iloc)
    - selecting data based on numerical position in data
    - dataset a big matrix 
****
    - exclusive
        - 0:10 will select entries 0,....,9
    -uses Python stdlib indexing scheme
****
* both loc and iloc are row-first, column-second
unlike native python (column-first, row-second)
"""

print(reviews.iloc[0])
print("----------------")
print()


# getting a column with iloc
print(reviews.iloc[:, 0])
print("----------------")
print()

"""
: operator
    - everything 
    
[-5:] 
    - would return last 5 numbers
negative numbers can be used in selection
    - counting from the end of values
"""

# first, second, third row
print(reviews.iloc[:3, 0])
# same as reviews.iloc[1:3,0]
print("----------------")
print()


"""
**** can also pass a list to iloc***
"""
print(reviews.iloc[[0,1,2,3,4,5], 0])
print("----------------")
print()

"""
- label-based selection (loc)
 - data index value, NOT it's position
 - uses the information in the indices to do its work
 ****
    - inclusive
        - 0:10 will select entries 0,....,10
 ****
"""
# getting the first entry in reviews
print(reviews.loc[0, 'country'])
print("----------------")
print()

loc_ex1 = reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
print(loc_ex1)
print("----------------")
print()

# Manipulating the index
"""
label-based selection is mutable
 - can change many different parts of the data
"""
reviews.set_index("title")

# Conditional Selection
"""
- We're able to conditionally filter and get back only data that satisfies
    - combine logic operators (&, |, 
"""
print(reviews.country == 'Italy')
# would show column of True/False.. Along with the indexes obviously

# only return the rows where country is Italy
print(reviews.loc[reviews.country == 'Italy'])
print("----------------")
print()

# return rows where country is Italy AND reviews points >= 90
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print("----------------")
print()

# return rows where country is Italy OR reviews points >= 90
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])
print("----------------")
print()


"""
Pandas comes with built-in conditional selectors

- isin
    -select data whose values "is in" list of values

- isnull, notnull
    - highlight values which are or are not empty
"""

# reviews in country Italy or France
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
# return rows where country is Italy AND reviews points > 90
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print("----------------")
print()

# filttering wines lacking a price tag in dataset
print(reviews.loc[reviews.price.notnull()])
# return rows where country is Italy AND reviews points > 90
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print("----------------")
print()

# Assigning Data
reviews['critic'] = 'everyone'
# all reviews['critic'] now would return column of everyone

# Exercises

"""
#1) Select the description column from reviews and assign the result to the variable desc.
"""
desc = reviews['description']

"""
2.
Select the first value from the description column of reviews, assigning it to variable first_description
"""
first_description = reviews['description'][0]

"""
3.
Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
"""
first_row = reviews.iloc[0]

"""
4.
Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.

Hint: format your output as a pandas Series.
"""
first_descriptions = reviews['description'][0:10]

"""
5.
Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
"""
sample_reviews = reviews.iloc[[1,2,3,5,8]]

"""
6.
Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. 
"""
df = reviews.loc[[0,1,10,100], ["country", "province", "region_1", "region_2"]]

"""
7.
Create a variable df containing the country and variety columns of the first 100 records.
"""
df = reviews.loc[0:99, ['country', 'variety']]


"""
8.
Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
"""
italian_wines = reviews.loc[reviews.country == 'Italy']


"""
9.
Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
"""

top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]