#!/usr/bin/env python3
"""
CORD-19 Data Analysis Script
============================

This script performs comprehensive analysis of COVID-19 research papers
from the CORD-19 dataset, including data cleaning, visualization, and 
key insights generation.

Author: [Your Name]
Date: September 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import warnings
import os

warnings.filterwarnings('ignore')

def setup_plotting():
    """Setup matplotlib and seaborn styling"""
    plt.style.use('default')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12

def load_and_explore_data(filename='metadata.csv'):
    """
    Load the CORD-19 dataset and perform initial exploration
    
    Args:
        filename (str): Path to the metadata CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    print("="*60)
    print("PART 1: DATA LOADING AND BASIC EXPLORATION")
    print("="*60)
    
    # Load data
    try:
        df = pd.read_csv(filename)
        print(f"✓ Successfully loaded data from {filename}")
    except FileNotFoundError:
        print(f"✗ Error: {filename} not found. Please ensure the file exists.")
        return None
    
    # Basic information
    print(f"\nDataset Shape: {df.shape}")
    print(f"Columns: {len(df.columns)}")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
    
    # Display column names
    print(f"\nColumn Names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i:2d}. {col}")
    
    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Data types
    print("\nData Types:")
    print(df.dtypes)
    
    # Missing values analysis
    print("\nMissing Values Analysis:")
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / len(df)) * 100
    missing_df = pd.DataFrame({
        'Column': missing_data.index,
        'Missing Count': missing_data.values,
        'Percentage': missing_percentage.values
    }).sort_values('Percentage', ascending=False)
    
    print(missing_df.to_string(index=False))
    
    # Basic statistics
    print("\nBasic Statistics for Numerical Columns:")
    print(df.describe())
    
    return df

def clean_and_prepare_data(df):
    """
    Clean and prepare the dataset for analysis
    
    Args:
        df (pd.DataFrame): Raw dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    print("\n" + "="*60)
    print("PART 2: DATA CLEANING AND PREPARATION")
    print("="*60)
    
    df_clean = df.copy()
    
    # Convert publish_time to datetime
    print("Converting publish_time to datetime...")
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    
    # Extract year
    df_clean['year'] = df_clean['publish_time'].dt.year
    
    # Create abstract word count
    print("Creating abstract word count...")
    df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').str.split().str.len()
    
    # Fill missing values
    print("Filling missing values...")
    df_clean['journal'] = df_clean['journal'].fillna('Unknown')
    df_clean['authors'] = df_clean['authors'].fillna('Unknown')
    df_clean['source_x'] = df_clean['source_x'].fillna('Unknown')
    
    # Remove rows with no year information
    initial_count = len(df_clean)
    df_clean = df_clean.dropna(subset=['year'])
    final_count = len(df_clean)
    
    print(f"✓ Cleaned dataset shape: {df_clean.shape}")
    print(f"✓ Removed {initial_count - final_count} rows with missing years")
    print(f"✓ Date range: {df_clean['year'].min():.0f} - {df_clean['year'].max():.0f}")
    print(f"✓ Average abstract length: {df_clean['abstract_word_count'].mean():.1f} words")
    
    return df_clean

def analyze_temporal_trends(df_clean):
    """Analyze publication trends over time"""
    print("\n" + "="*60)
    print("PART 3.1: TEMPORAL ANALYSIS")
    print("="*60)
    
    # Publications by year
    yearly_counts = df_clean['year'].value_counts().sort_index()
    print("Publications by year:")
    for year, count in yearly_counts.items():
        print(f"  {year:.0f}: {count:,} papers")
    
    # Plot publications by year
    plt.figure(figsize=(12, 6))
    bars = plt.bar(yearly_counts.index, yearly_counts.values, color='steelblue', alpha=0.8)
    plt.title('COVID-19 Research Publications by Year', fontsize=16, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + max(yearly_counts.values) * 0.01,
                f'{int(height):,}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('publications_by_year.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✓ Peak publication year: {yearly_counts.idxmax():.0f} ({yearly_counts.max():,} papers)")
    
    return yearly_counts

def analyze_journals(df_clean):
    """Analyze journal publication patterns"""
    print("\n" + "="*60)
    print("PART 3.2: JOURNAL ANALYSIS")
    print("="*60)
    
    # Top journals
    top_journals = df_clean['journal'].value_counts().head(15)
    print("Top 15 journals:")
    for i, (journal, count) in enumerate(top_journals.items(), 1):
        print(f"  {i:2d}. {journal}: {count:,} papers")
    
    # Plot top journals
    plt.figure(figsize=(12, 8))
    bars = plt.barh(range(len(top_journals)), top_journals.values, color='orange', alpha=0.8)
    plt.yticks(range(len(top_journals)), top_journals.index)
    plt.title('Top 15 Journals Publishing COVID-19 Research', fontsize=16, fontweight='bold')
    plt.xlabel('Number of Publications')
    plt.gca().invert_yaxis()
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + max(top_journals.values) * 0.01, bar.get_y() + bar.get_height()/2,
                f'{int(width):,}', ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('top_journals.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✓ Most prolific journal: {top_journals.index[0]} ({top_journals.iloc[0]:,} papers)")
    
    return top_journals

def analyze_word_frequency(df_clean):
    """Analyze word frequency in titles"""
    print("\n" + "="*60)
    print("PART 3.3: WORD FREQUENCY ANALYSIS")
    print("="*60)
    
    # Combine all titles
    all_titles = ' '.join(df_clean['title'].fillna('').str.lower())
    
    # Remove stop words and short words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'between', 'study', 'analysis'
    }
    
    words = [word.strip('.,!?;:"()[]{}') for word in all_titles.split() 
             if word not in stop_words and len(word) > 2 and word.isalpha()]
    
    word_freq = Counter(words)
    top_words = word_freq.most_common(20)
    
    print("Top 20 most frequent words in titles:")
    for i, (word, count) in enumerate(top_words, 1):
        print(f"  {i:2d}. {word}: {count:,} occurrences")
    
    # Plot word frequency
    if top_words:
        words_list, counts_list = zip(*top_words)
        
        plt.figure(figsize=(12, 8))
        bars = plt.barh(range(len(words_list)), counts_list, color='green', alpha=0.8)
        plt.yticks(range(len(words_list)), words_list)
        plt.title('Most Frequent Words in Paper Titles', fontsize=16, fontweight='bold')
        plt.xlabel('Frequency')
        plt.gca().invert_yaxis()
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + max(counts_list) * 0.01, bar.get_y() + bar.get_height()/2,
                    f'{int(width):,}', ha='left', va='center')
        
        plt.tight_layout()
        plt.savefig('word_frequency.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    # Generate word cloud
    try:
        print("Generating word cloud...")
        # Filter words for word cloud (remove very common ones)
        filtered_words = ' '.join([word for word, count in word_freq.items() if count >= 5])
        
        wordcloud = WordCloud(width=800, height=400, 
                            background_color='white',
                            colormap='viridis',
                            max_words=100).generate(filtered_words)
        
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Paper Titles', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('wordcloud.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Word cloud generated successfully")
        
    except Exception as e:
        print(f"✗ Could not generate word cloud: {e}")
    
    print(f"✓ Most common word: '{top_words[0][0]}' ({top_words[0][1]:,} occurrences)")
    
    return top_words

def analyze_sources(df_clean):
    """Analyze distribution by data source"""
    print("\n" + "="*60)
    print("PART 3.4: SOURCE ANALYSIS")
    print("="*60)
    
    # Source distribution
    source_counts = df_clean['source_x'].value_counts()
    print("Papers by source:")
    for source, count in source_counts.items():
        percentage = (count / len(df_clean)) * 100
        print(f"  {source}: {count:,} papers ({percentage:.1f}%)")
    
    # Plot source distribution
    plt.figure(figsize=(10, 6))
    colors = plt.cm.Set3(np.arange(len(source_counts)))
    wedges, texts, autotexts = plt.pie(source_counts.values, labels=source_counts.index, 
                                      autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Distribution of Papers by Source', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('source_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✓ Primary source: {source_counts.index[0]} ({source_counts.iloc[0]:,} papers)")
    
    return source_counts

def analyze_abstracts(df_clean):
    """Analyze abstract characteristics"""
    print("\n" + "="*60)
    print("PART 3.5: ABSTRACT ANALYSIS")
    print("="*60)
    
    # Abstract statistics
    abstract_stats = df_clean['abstract_word_count'].describe()
    print("Abstract word count statistics:")
    for stat, value in abstract_stats.items():
        print(f"  {stat}: {value:.1f}")
    
    # Plot abstract length distribution
    valid_abstracts = df_clean[df_clean['abstract_word_count'] > 0]['abstract_word_count']
    
    plt.figure(figsize=(10, 6))
    plt.hist(valid_abstracts, bins=50, alpha=0.7, color='purple', edgecolor='black')
    plt.axvline(valid_abstracts.mean(), color='red', linestyle='--', 
               label=f'Mean: {valid_abstracts.mean():.1f}')
    plt.axvline(valid_abstracts.median(), color='orange', linestyle='--', 
               label=f'Median: {valid_abstracts.median():.1f}')
    plt.title('Distribution of Abstract Word Counts', fontsize=16, fontweight='bold')
    plt.xlabel('Word Count')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('abstract_length_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Papers with and without abstracts
    with_abstract = (df_clean['abstract_word_count'] > 0).sum()
    without_abstract = len(df_clean) - with_abstract
    print(f"Papers with abstracts: {with_abstract:,} ({with_abstract/len(df_clean)*100:.1f}%)")
    print(f"Papers without abstracts: {without_abstract:,} ({without_abstract/len(df_clean)*100:.1f}%)")
    
    return abstract_stats

def generate_summary_report(df_clean, yearly_counts, top_journals, top_words, source_counts, abstract_stats):
    """Generate a comprehensive summary report"""
    print("\n" + "="*60)
    print("COMPREHENSIVE SUMMARY REPORT")
    print("="*60)
    
    print(f"""
📊 DATASET OVERVIEW
-------------------
• Total papers analyzed: {len(df_clean):,}
• Date range: {df_clean['year'].min():.0f} - {df_clean['year'].max():.0f}
• Unique journals: {df_clean['journal'].nunique():,}
• Unique authors: {df_clean['authors'].nunique():,}
• Data sources: {df_clean['source_x'].nunique():,}

📈 TEMPORAL TRENDS
------------------
• Peak publication year: {yearly_counts.idxmax():.0f} ({yearly_counts.max():,} papers)
• Average papers per year: {yearly_counts.mean():.1f}
• Growth trend: {"Increasing" if yearly_counts.iloc[-1] > yearly_counts.iloc[0] else "Decreasing"}

📚 JOURNAL INSIGHTS
-------------------
• Most prolific journal: {top_journals.index[0]}
  ({top_journals.iloc[0]:,} papers, {top_journals.iloc[0]/len(df_clean)*100:.1f}%)
• Top 3 journals account for: {top_journals.head(3).sum():,} papers ({top_journals.head(3).sum()/len(df_clean)*100:.1f}%)

🔤 CONTENT ANALYSIS
-------------------
• Most frequent word: "{top_words[0][0]}" ({top_words[0][1]:,} occurrences)
• Top 3 words: {', '.join([f'"{word}"' for word, _ in top_words[:3]])}
• Average abstract length: {abstract_stats['mean']:.1f} words
• Papers with abstracts: {(df_clean['abstract_word_count'] > 0).sum():,} ({(df_clean['abstract_word_count'] > 0).sum()/len(df_clean)*100:.1f}%)

🗃️ SOURCE DISTRIBUTION
----------------------
• Primary source: {source_counts.index[0]} ({source_counts.iloc[0]:,} papers, {source_counts.iloc[0]/len(df_clean)*100:.1f}%)
• Source diversity: {len(source_counts)} different sources
""")
    
    print("✓ Analysis complete!")
    print("✓ All visualizations saved as PNG files")
    print("✓ Summary report generated")

def main():
    """Main function to run the complete analysis"""
    print("CORD-19 Data Analysis")
    print("====================")
    print("Comprehensive analysis of COVID-19 research papers")
    print(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Setup
    setup_plotting()
    
    # Create output directory
    os.makedirs('images', exist_ok=True)
    
    # Part 1: Load and explore data
    df = load_and_explore_data()
    if df is None:
        return
    
    # Part 2: Clean and prepare data
    df_clean = clean_and_prepare_data(df)
    
    # Part 3: Analysis and visualization
    yearly_counts = analyze_temporal_trends(df_clean)
    top_journals = analyze_journals(df_clean)
    top_words = analyze_word_frequency(df_clean)
    source_counts = analyze_sources(df_clean)
    abstract_stats = analyze_abstracts(df_clean)
    
    # Part 4: Generate summary report
    generate_summary_report(df_clean, yearly_counts, top_journals, 
                          top_words, source_counts, abstract_stats)
    
    # Save cleaned data
    df_clean.to_csv('cleaned_metadata.csv', index=False)
    print("✓ Cleaned dataset saved as 'cleaned_metadata.csv'")

if __name__ == "__main__":
    main()