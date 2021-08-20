import pandas as pd

pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea

insurance_data = pd.read_csv('../insurance.csv')

# scatterplots take x and y axis
sea.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
# suggests that bmi and insurance cost are positively correlated
# positive correlation: relationship between two variables who move in the same direction
# either both decrease or both increase together

# to add a regression life we can change from scatterplot to regplot
sea.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# color-coded scatter plots
sea.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
# color coded smokers and non smokers
# easier to see that smokers pay MUCH more

# use sea.lmplot to add two  regression lines
# corresponding to smokers and non smokers
sea.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

# categorical scatter plot
sea.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])

# Exercsises
"""
1.
Read the candy data file into candy_data. Use the "id" column to label the rows.
candy_data = pd.read_csv(candy_filepath, index_col='id')
"""

"""
2.
Use a Python command to print the first five rows of the data.
candy_data.head()

# Fill in the line below: Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)
more_popular = '3 Musketeers'

# Fill in the line below: Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)
more_sugar = 'Air Heads'
"""

"""
3.
Create a scatter plot that shows the relationship between 'sugarpercent' (on the horizontal x-axis) and 'winpercent' (on the vertical y-axis). Don't add a regression line just yet -- you'll do that in the next step!
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

Does the scatter plot show a strong correlation between the two variables? If so, are candies with more sugar relatively more or less popular with the survey respondents?
No strong correlation 
"""

"""
4.
Part A¶
Create the same scatter plot you created in Step 3, but now with a regression line!
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

Part B
According to the plot above, is there a slight correlation between 'winpercent' and 'sugarpercent'? What does this tell you about the candy that people tend to prefer?
Since regression line has a slightly positive slope this tells us there's a positive correlation
between win% and sugar%.
"""

"""
5.
In the code cell below, create a scatter plot to show the relationship between 'pricepercent' (on the horizontal x-axis) and 'winpercent' (on the vertical y-axis). Use the 'chocolate' column to color-code the points. Don't add any regression lines just yet -- you'll do that in the next step!
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])
"""

"""
6
Part A
Create the same scatter plot you created in Step 5, but now with two regression lines, corresponding to (1) chocolate candies and (2) candies without chocolate.
sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)

Part B
Using the regression lines, what conclusions can you draw about the effects of chocolate and price on candy popularity?
1. Since regression line has slightly positive slope, more expensive chocolate candies tend to be more popular.
2. If candies don't have chocolate they're more popular when cheaper.
"""

"""
7.
Part A
Create a categorical scatter plot to highlight the relationship between 'chocolate' and 'winpercent'. Put 'chocolate' on the (horizontal) x-axis, and 'winpercent' on the (vertical) y-axis.
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])

Part B
You decide to dedicate a section of your report to the fact that chocolate candies tend to be more popular than candies without chocolate. Which plot is more appropriate to tell this story: the plot from Step 6, or the plot from Step 7?
step 7 shows this fact
"""