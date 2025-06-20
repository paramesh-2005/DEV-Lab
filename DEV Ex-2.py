# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download stopwords
nltk.download('stopwords')

# Step 2: Load the dataset (✅ Corrected path, no invisible characters)
df = pd.read_csv(r'C:\Users\PARAMESHWARAN\Downloads\spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']  # Rename columns

# Step 3: Understand dataset structure
print("\n🔍 First 5 rows of the dataset:")
print(df.head())

print("\n📋 Dataset Info:")
print(df.info())

print("\n📊 Dataset Description:")
print(df.describe())

# Step 4: Check for null/missing values
print("\n🔎 Missing values:")
print(df.isnull().sum())

# Step 5: Analyze class distribution (✅ Fixed Seaborn warning)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='label', hue='label', palette='viridis', legend=False)
plt.title('Distribution of Spam vs Ham')
plt.xlabel('Message Type')
plt.ylabel('Count')
plt.show()

print("\n📊 Class Distribution:")
print(df['label'].value_counts(normalize=True))

# Step 6: Visualize data distribution
df['message_length'] = df['message'].apply(len)

plt.figure(figsize=(10, 6))
df[df['label'] == 'ham']['message_length'].plot.hist(bins=50, alpha=0.7, label='Ham')
df[df['label'] == 'spam']['message_length'].plot.hist(bins=50, alpha=0.7, label='Spam', color='red')
plt.legend()
plt.title('Histogram of Message Lengths')
plt.xlabel('Message Length')
plt.show()

# Step 7a: Text-specific analysis – Word Frequency
def clean_text(msg):
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    words = msg.lower().split()
    return [word for word in words if word not in stopwords.words('english')]

ham_words = []
spam_words = []

for msg in df[df['label'] == 'ham']['message']:
    ham_words += clean_text(msg)

for msg in df[df['label'] == 'spam']['message']:
    spam_words += clean_text(msg)

print("\n🔠 Most common words in Ham messages:")
print(Counter(ham_words).most_common(10))

print("\n🔠 Most common words in Spam messages:")
print(Counter(spam_words).most_common(10))

# Step 7b: Word Clouds
ham_msg = " ".join(df[df['label'] == 'ham']['message'])
spam_msg = " ".join(df[df['label'] == 'spam']['message'])

ham_wc = WordCloud(width=500, height=300, background_color='white').generate(ham_msg)
spam_wc = WordCloud(width=500, height=300, background_color='black', colormap='Reds').generate(spam_msg)

plt.figure(figsize=(10, 6))
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Ham Word Cloud')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Spam Word Cloud')
plt.show()

# Step 8: Statistical summary
print("\n📈 Statistical Summary of Message Length by Label:")
print(df.groupby('label')['message_length'].describe())

# Step 9: Conclusion
print("\n✅ Insights:")
print("1. Dataset is imbalanced: ~87% Ham, ~13% Spam.")
print("2. Spam messages are generally longer in length.")
print("3. Spam messages commonly contain promotional words like 'free', 'win', 'call'.")
print("4. Word clouds show distinct patterns in spam and ham vocabularies.")
