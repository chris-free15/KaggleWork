import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea

flight_data = pd.read_csv('../flight_delays.csv', index_col="Month")

# Bar Chart

# dimensions
plt.figure(figsize=(10, 6))

# title
plt.title("Average Arrival Delay for Spirit Airline Fights, by Month")

sea.barplot(x=flight_data.index, y=flight_data["NK"])

plt.ylabel("Arrival delay in minutes")


# Heatmap

# dimensions
plt.figure(figsize=(14,7))

# annot=True ensures that all values for each cell appear.
sea.heatmap(data=flight_data, annot=True)

plt.xlabel("Airline")

# Exercises
""""
1.
Read the IGN data file into ign_data. Use the "Platform" column to label the rows.
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
"""

"""
2.
# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score = 7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'

"""

"""
3.
Part A
Create a bar chart that shows the average score for racing games, for each platform. Your chart should have one bar for each platform.
plt.figure(figsize=(10,6))
sns.barplot(x=ign_data['Racing'], y=ign_data.index)

Part B¶
Based on the bar chart, do you expect a racing game for the Wii platform to receive a high rating? If not, what gaming platform seems to be the best alternative?
No, xbox one has the highest ratings. So, that one
"""

"""
4.Part A
Use the data to create a heatmap of average score by genre and platform.
plt.figure(figsize=(14,7))
sns.heatmap(data=ign_data, annot=True)

Part B
Which combination of genre and platform receives the highest average ratings? Which combination receives the lowest average rankings?
highest= Simulation & ps4
lowest=gameboy color shooter & fighting
"""