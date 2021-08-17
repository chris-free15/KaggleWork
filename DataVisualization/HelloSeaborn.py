import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea
"""
https://seaborn.pydata.org/index.html
"""

fifa_data = pd.read_csv('../fifa.csv', index_col="Date", parse_dates=True)

# width and height
plt.figure(figsize=(16,6))

# line chart
sea.lineplot(data=fifa_data)

# needs to be called to show the graph
plt.show()
