import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea

spotify_data = pd.read_csv('../spotify.csv', index_col='Date', parse_dates=True)


# Line chart showing daily global streams of each song

# size of window
plt.figure(figsize=(14,6))

# can add a title
plt.title("Daly global streams of popular songs in 2017-2018")

# sea.lineplot(data=spotify_data)
# plt.show()

# Plot a subset of data
print(list(spotify_data.columns))

sea.lineplot(data=spotify_data['Shape of You'], label='Shape of You')
sea.lineplot(data=spotify_data['Despacito'], label='Despacito')
#horizontal axis label
plt.xlabel("Date")

plt.show()

# Exercises
"""
1.
# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)
"""

"""
2.
Use a Python command to print the last 5 rows of the data.
museum_data.tail()

# Fill in the line below: How many visitors did the Chinese American Museum 
# receive in July 2018?
ca_museum_jul18 = 2620

# Fill in the line below: In October 2018, how many more visitors did Avila 
# Adobe receive than the Firehouse Museum?
avila_oct18 = 19280-4622
"""

"""
3.
The Firehouse Museum claims they ran an event in 2014 that brought an incredible number of visitors, and that they should get extra budget to run a similar event again. The other museums think these types of events aren't that important, and budgets should be split purely based on recent visitors on an average day.

To show the museum board how the event compared to regular traffic at each museum, create a line chart that shows how the number of visitors to each museum evolved over time. Your figure should have four lines (one for each museum).
# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data)
# Add title
plt.title("Monthly Visitors to Los Angeles City Museums")
"""

"""
4.
Create a line chart that shows how the number of visitors to Avila Adobe has evolved over time. (If your code returns an error, the first thing that you should check is that you've spelled the name of the column correctly! You must write the name of the column exactly as it appears in the dataset.)
sns.lineplot(data=museum_data['Avila Adobe'])

Part B
Does Avila Adobe get more visitors:

in September-February (in LA, the fall and winter months), or
in March-August (in LA, the spring and summer)?
Using this information, when should the museum staff additional seasonal employees?
September-February
"""