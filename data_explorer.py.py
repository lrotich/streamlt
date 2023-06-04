import csv

# Open the CSV file
with open('iris.data.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Read each row in the CSV file
    for row in reader:
        # Display the row
        print(row)
print("Question ONE")

import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Calculate the average sepal length for each species
average_sepal_length = df.groupby('species')['sepal_length'].mean()

# Display the average sepal length for each species
print(average_sepal_length)
print("Queston Two")
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Select the two features for the scatter plot
feature1 = 'sepal_length'
feature2 = 'sepal_width'

# Create a scatter plot
plt.scatter(df[feature1], df[feature2], c='b', alpha=0.5)

# Set the labels and title of the plot
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.title(f'Scatter Plot: {feature1} vs {feature2}')

# Display the scatter plot
plt.show()
print("Queston Three")
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Specify the species to filter
target_species = 'versicolor'

# Filter the data based on the specified species
filtered_data = df[df['species'] == target_species]

# Display the filtered data
print(filtered_data)
print("Questin Four")
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import tkinter
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Specify the species to filter
target_species = 'versicolor'

# Filter the data based on the specified species
filtered_data = df[df['species'] == target_species]


# Create a pairplot for the filtered data
sns.pairplot(filtered_data, hue='species')

# Display the pairplot
plt.show()

print("Question Five")
#import tkinter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('TkAgg')


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Specify the feature to visualize
target_feature = 'sepal_length'

# Filter the data for the selected feature
selected_feature_data = df[target_feature]

# Create a histogram of the selected feature
sns.histplot(selected_feature_data, kde=True)

# Set the labels and title of the plot
plt.xlabel(target_feature)
plt.ylabel('Count')
plt.title(f'Distribution of {target_feature}')

# Display the histogram
plt.savefig("dataexplorer.png")
#plt.show()
