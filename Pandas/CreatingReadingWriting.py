import pandas as pd

"""
DataFrame
    - table (array of entries)
        - entry ( row/record) and a column)
"""

table_ex1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(table_ex1)
print("----------------")
print()

"""
- columns: yes, no
- two rows/entries
"""

table_ex2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(table_ex2)
print("----------------")
print()
"""
- entries are not limited to ints
"""


"""
- default constructor pd.DataFrame()
- takes a dictionary
    - keys = column names
    - indexed entries are values
        - these can be labeled
"""

table_ex3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(table_ex3)
print("----------------")
print()
"""
Series
    - sequence of values (list)     
        - has index as well. single column of values
"""

series_ex1 = pd.Series([1,2,3,4,5])
print(series_ex1)
print("----------------")
print()

series_ex2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(series_ex2)
print("----------------")
print()

# Reading Data Files
"""
CSV table of values separated by commas
"""
wine_reviews = pd.read_csv("../winemag-data-130k-v2.csv")

print(wine_reviews.shape)
"""
shape shows the dimensions
(129971, 14)
130k rows, 14 columns
"""

print(wine_reviews.head())
# first 5 rows... head just like from terminal

"""
pd.read_csv() has over 30 optional parameters

********
if dataset has a built in index you can make pandas use it 
with parameter index_col = 0
"""

wine_reviews = pd.read_csv("../winemag-data-130k-v2.csv", index_col=0)
# DO NOT READ IN THE FILE MORE THAN ONCE.. this is just to follow tutorial

print(wine_reviews.head())


# EXERCISES
# 1)
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

#2)
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=["2017 Sales", "2018 Sales"])

#3)
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 can"], index=["Flour", "Milk", "Eggs", "Spam"], name="Dinner")

#4)
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

#5)
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
# animals.to_csv("cows_and_goats.csv")