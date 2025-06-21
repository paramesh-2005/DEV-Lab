import seaborn as sns
import matplotlib.pyplot as plt

# Set the theme for all plots
sns.set_theme(style="darkgrid")

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# 1. Count Plot – How many survived vs. not?
plt.figure(figsize=(6, 4))
sns.countplot(data=titanic, x='survived')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# 2. Bar Plot – Survival rate by class
plt.figure(figsize=(6, 4))
sns.barplot(data=titanic, x='class', y='survived')
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()

# 3. Box Plot – Age distribution by class
plt.figure(figsize=(6, 4))
sns.boxplot(data=titanic, x='class', y='age')
plt.title("Age Distribution by Class")
plt.ylabel("Age")
plt.show()

# 4. Violin Plot – Age distribution by class and gender
plt.figure(figsize=(8, 5))
sns.violinplot(data=titanic, x='class', y='age', hue='sex', split=True)
plt.title("Age Distribution by Class and Gender")
plt.show()

# 5. Heatmap – Correlation matrix
plt.figure(figsize=(6, 5))
corr = titanic.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 6. Pair Plot – Explore relationships (age, fare, survived)
pairplot_data = titanic.dropna(subset=['age', 'fare', 'survived'])
sns.pairplot(pairplot_data, hue='survived', vars=['age', 'fare'])
plt.suptitle("Pairplot of Age and Fare by Survival", y=1.02)
plt.show()

# 7. FacetGrid – Survival rate by class and gender
g = sns.catplot(data=titanic, x='class', hue='survived', col='sex',
                kind='count', height=5, aspect=0.8)
g.fig.suptitle("Survival Count by Class and Gender", y=1.05)
plt.show()
