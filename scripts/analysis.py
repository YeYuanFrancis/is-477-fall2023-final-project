import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
column_names = ['Class', 'Alcohol', 'Malicacid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 
                'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins', 
                'Color_intensity', 'Hue', 'OD280_OD315_of_diluted wines', 'Proline']

df = pd.read_csv('data/wine/wine.data', names=column_names)

print(df.columns)
sns.histplot(df['Alcohol'])
plt.title('Distribution of Alcohol Content in Wines')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.savefig('results/alcohol_distribution.png')