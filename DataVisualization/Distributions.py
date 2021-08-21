import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sea

iris_data = pd.read_csv('../iris.csv', index_col="Id")
print(iris_data.head())

# Histogram
# sea.distplot(a=iris_data['Petal Length (cm)'], kde=False)
"""
a= chooses the column we'd like to plot
kde= if not set to False will create  a different plot ( will fit a curve on top of it)
"""

# Density Plots
"""
Kernel Density Estimate
    - smoothed histogram
    - non parametric way to estimate the probability density function of a random variable

parameter: any measured quantity of a statistical population that summarises or describes the population
    - ex) mean, standard deviation

probability density function (pdf): of a continuous random variable, is a function whose value at any given sample
or point in the sample space can be interpreted as providing a relative likelihood that the value of the random
variable would equal that sample
 - since the absolute likelhood for continuous random variables to take on any particular value is 0, since
 there are infinite set of possible values, the value of the PDF at two different samples can be used to infer
 in any particular draw of the random variable how much more likely i is that the random variable would equal
 one sample compared to the other sample.
 - in a more precise sense, the PDF is used to specify the probability of the random variable falling within a particular range of values, as opposed to taking on any one value.

sample space: the set of possible values taken by the random variable
"""

# KDE Plot
# sea.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# 2D KDE Plots
# sea.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")

iris_set_data = pd.read_csv('../iris_setosa.csv', index_col="Id")
iris_ver_data = pd.read_csv('../iris_versicolor.csv', index_col='Id')
iris_vir_data = pd.read_csv('../iris_virginica.csv', index_col='Id')

"""# Histograms for each species
sea.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sea.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sea.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

# Add title
plt.title("Histogram of Petal Lengths, by Species")

# Force legend to appear
plt.legend()"""


# KDE plots for each species
sea.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sea.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sea.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")
plt.legend()
plt.show()

# Exercises
"""
1.
Load the data file corresponding to benign tumors into a DataFrame called cancer_b_data. The corresponding filepath is cancer_b_filepath. Use the "Id" column to label the rows.
Load the data file corresponding to malignant tumors into a DataFrame called cancer_m_data. The corresponding filepath is cancer_m_filepath. Use the "Id" column to label the rows.
# Paths of the files to read
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"

# Fill in the line below to read the (benign) file into a variable cancer_b_data
cancer_b_data = pd.read_csv(filepath_or_buffer=cancer_b_filepath, index_col='Id')

# Fill in the line below to read the (malignant) file into a variable cancer_m_data
cancer_m_data = pd.read_csv(filepath_or_buffer=cancer_m_filepath, index_col='Id')
"""


"""
2.
Use a Python command to print the first 5 rows of the data for benign tumors.
cancer_b_data.head()

Use a Python command to print the first 5 rows of the data for malignant tumors.
cancer_m_data.head()


# Fill in the line below: In the first five rows of the data for benign tumors, what is the
# largest value for 'Perimeter (mean)'?
max_perim = 87.46

# Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 842517?
mean_radius = 20.57
"""

"""
3.
Part A
Use the code cell below to create two histograms that show the distribution in values for 'Area (mean)' for both benign and malignant tumors. (To permit easy comparison, create a single figure containing both histograms in the code cell below.)
sns.distplot(a=cancer_b_data['Area (mean)'], label="Benign", kde=False)
sns.distplot(a=cancer_m_data['Area (mean)'], label="Malignant", kde=False)
plt.legend()

Part B
A researcher approaches you for help with identifying how the 'Area (mean)' column can be used to understand the difference between benign and malignant tumors. Based on the histograms above,

Do malignant tumors have higher or lower values for 'Area (mean)' (relative to benign tumors), on average?
Which tumor type seems to have a larger range of potential values?
Malignant tumors have higher values for Area on average and a larger range of potential values
"""

"""
4.
Part A
Use the code cell below to create two KDE plots that show the distribution in values for 'Radius (worst)' for both benign and malignant tumors. (To permit easy comparison, create a single figure containing both KDE plots in the code cell below.)
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True, label="Benign")
sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True, label="Malignant")

Part B
A hospital has recently started using an algorithm that can diagnose tumors with high accuracy. Given a tumor with a value for 'Radius (worst)' of 25, do you think the algorithm is more likely to classify the tumor as benign or malignant?
Malignant becuase the curve is higher than benign around the values of 25
"""