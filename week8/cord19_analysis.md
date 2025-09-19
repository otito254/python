# CORD-19 Data Analysis

## Part 1: Data Loading and Basic Exploration

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Load the data
df = pd.read_csv('metadata.csv')
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
```

```python
# Examine first few rows
print("First 5 rows:")
print(df.head())
```

```python
# Data structure information
print("\nData types and info:")
print(df.info())
```

```python
# Check for missing values
print("\nMissing values by column:")
missing_data = df.isnull().sum()
missing_percentage = (missing_data / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing_data,
    'Percentage': missing_percentage
}).sort_values('Percentage', ascending=False)
print(missing_df)
```

```python
# Basic statistics for numerical columns
print("\nBasic statistics:")
print(df.describe())
```

## Part 2: Data Cleaning and Preparation

```python
# Handle missing data
print("Columns with high missing values (>50%):")
high_missing = missing_df[missing_df['Percentage'] > 50]
print(high_missing)

# Create a cleaned dataset
df_clean = df.copy()

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Extract year from publication date
df_clean['year'] = df_clean['publish_time'].dt.year

# Create abstract word count column
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').str.split().str.len()

# Fill missing values for important columns
df_clean['journal'] = df_clean['journal'].fillna('Unknown')
df_clean['authors'] = df_clean['authors'].fillna('Unknown')

print(f"Cleaned dataset shape: {df_clean.shape}")
print(f"Date range: {df_clean['year'].min()} - {df_clean['year'].max()}")
```

## Part 3: Data Analysis and Visualization

```python
# Set up plotting style
plt.style.use('default')
sns.set_palette("husl")
```

### 3.1 Publications by Year

```python
# Count papers by year
yearly_counts = df_clean['year'].value_counts().sort_index()
print("Papers by year:")
print(yearly_counts)

# Plot publications over time
plt.figure(figsize=(10, 6))
plt.bar(yearly_counts.index, yearly_counts.values)
plt.title('COVID-19 Research Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(yearly_counts.values):
    plt.text(yearly_counts.index[i], v + 5, str(v), ha='center')
plt.tight_layout()
plt.savefig('publications_by_year.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 3.2 Top Publishing Journals

```python
# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
print("Top 10 journals:")
print(top_journals)

# Plot top journals
plt.figure(figsize=(12, 6))
plt.barh(range(len(top_journals)), top_journals.values)
plt.yticks(range(len(top_journals)), top_journals.index)
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Publications')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_journals.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 3.3 Word Analysis of Titles

```python
# Most frequent words in titles
all_titles = ' '.join(df_clean['title'].fillna('').str.lower())
# Remove common stop words
stop_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']
words = [word for word in all_titles.split() if word not in stop_words and len(word) > 2]
word_freq = Counter(words)
top_words = word_freq.most_common(15)

print("Most frequent words in titles:")
for word, count in top_words:
    print(f"{word}: {count}")

# Plot word frequency
words, counts = zip(*top_words)
plt.figure(figsize=(12, 6))
plt.barh(range(len(words)), counts)
plt.yticks(range(len(words)), words)
plt.title('Most Frequent Words in Paper Titles')
plt.xlabel('Frequency')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('word_frequency.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 3.4 Word Cloud

```python
# Generate word cloud
if len(all_titles) > 0:
    wordcloud = WordCloud(width=800, height=400, 
                         background_color='white',
                         max_words=100).generate(all_titles)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Paper Titles')
    plt.tight_layout()
    plt.savefig('wordcloud.png', dpi=300, bbox_inches='tight')
    plt.show()
```

### 3.5 Distribution by Source

```python
# Count papers by source
source_counts = df_clean['source_x'].value_counts()
print("Papers by source:")
print(source_counts)

# Plot source distribution
plt.figure(figsize=(10, 6))
plt.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Papers by Source')
plt.axis('equal')
plt.tight_layout()
plt.savefig('source_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 3.6 Abstract Length Analysis

```python
# Abstract word count analysis
abstract_stats = df_clean['abstract_word_count'].describe()
print("Abstract word count statistics:")
print(abstract_stats)

# Plot abstract length distribution
plt.figure(figsize=(10, 6))
df_clean[df_clean['abstract_word_count'] > 0]['abstract_word_count'].hist(bins=30, alpha=0.7)
plt.title('Distribution of Abstract Word Counts')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('abstract_length_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Part 4: Key Findings Summary

```python
print("=== KEY FINDINGS ===")
print(f"Total papers analyzed: {len(df_clean)}")
print(f"Date range: {df_clean['year'].min():.0f} - {df_clean['year'].max():.0f}")
print(f"Peak publication year: {yearly_counts.idxmax()} ({yearly_counts.max()} papers)")
print(f"Most active journal: {top_journals.index[0]} ({top_journals.iloc[0]} papers)")
print(f"Most common word in titles: {top_words[0][0]} ({top_words[0][1]} occurrences)")
print(f"Average abstract length: {df_clean['abstract_word_count'].mean():.1f} words")
print(f"Most common source: {source_counts.index[0]} ({source_counts.iloc[0]} papers)")
```

This notebook provides a comprehensive analysis of the CORD-19 dataset including:
- Data loading and exploration
- Data cleaning and preparation  
- Multiple visualizations
- Key findings summary

Save this as `cord19_analysis.ipynb` or run as a Python script.