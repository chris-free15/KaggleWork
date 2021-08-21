import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea

"""
Trends: a pattern of change
    - use lineplot
Relationships:
    - barplot: useful for comparing quantities between different groups
    - heatmaps: to find color-coded patterns in tables of numbers
    - scatter plots: show relationship between two continuos variabels
        - if color-coded can show the relationship with a third categorical variable
    - regplot: a regression line in the scatter plot
    - lmplot: useful for drawing multiple regression  lines
    - swarmplot: categorical scatter plots. shows the relationship between a continues variable
        and a categorical variable
Distrbution: show possible values that we can expect to see in a variable with
 how likely they are
    - distplot: histograms show the distribution of a single numerical value
    - kdeplot: KDE or 2D KE plots show an estimated, smooth distribution of a single numerical or two
        variables
    - joinplot: command is useful for simultaneously displaying a 2D KDE plot with corresponding
        KDE plots for each individual variable
    
categorical variable: a variable that can take on one of a limited, usually fixed, number of
possible values on the basis of a qualitative property.
"""

# Changing Styles with seaborn

spotify_data = pd.read_csv('../spotify.csv', index_col='Date', parse_dates=True)

# Line Chart
sea.set_style("darkgrid")

plt.figure(figsize=(12,6))
sea.lineplot(data=spotify_data)
plt.show()
