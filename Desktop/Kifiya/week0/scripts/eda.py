import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('data/benin-malanville')

# Summary statistics
print(data.describe())

# Data quality checks
print(data.isnull().sum())

# Histograms
columns_to_plot = ['GHI', 'DNI', 'DHI', 'Tamb']
for col in columns_to_plot:
    plt.hist(data[col].dropna(), bins=30, alpha=0.7, label=col)
    plt.title(f'Distribution of {col}')
    plt.show()

# Correlation matrix
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
