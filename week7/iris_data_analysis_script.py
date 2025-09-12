#!/usr/bin/env python3
"""
Data Analysis Assignment: Pandas and Matplotlib
Analyzing the Iris Dataset

This script demonstrates comprehensive data analysis using pandas for 
data manipulation and matplotlib/seaborn for visualization.

Author: Data Analysis Student
Assignment: Task 1-3 Data Analysis with Pandas and Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

def setup_plotting():
    """Configure plotting settings for better visualizations."""
    plt.style.use('seaborn-v0_8')
    sns.set_palette('husl')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12

def load_and_explore_data():
    """Task 1: Load and explore the Iris dataset."""
    print("="*60)
    print("TASK 1: LOAD AND EXPLORE THE DATASET")
    print("="*60)

    try:
        # Load the Iris dataset
        iris_sklearn = load_iris()
        iris_df = pd.DataFrame(data=iris_sklearn.data, columns=iris_sklearn.feature_names)
        iris_df['species'] = pd.Categorical.from_codes(iris_sklearn.target, iris_sklearn.target_names)

        print(f"✅ Dataset loaded successfully!")
        print(f"📊 Dataset shape: {iris_df.shape}")
        print()

        # Display first few rows
        print("First 10 rows of the dataset:")
        print(iris_df.head(10))
        print()

        # Dataset information
        print("Dataset Information:")
        print(iris_df.info())
        print()

        # Check for missing values
        print("Missing Values Check:")
        missing_values = iris_df.isnull().sum()
        print(missing_values)
        print(f"Total missing values: {missing_values.sum()}")

        if missing_values.sum() == 0:
            print("✅ No missing values found - dataset is clean!")
        else:
            print("⚠️ Missing values detected - cleaning required")
            # Handle missing values if any (fill or drop)
            iris_df = iris_df.dropna()  # or iris_df.fillna(method='mean')

        print("\nTASK 1 COMPLETED ✅\n")
        return iris_df

    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def analyze_data(iris_df):
    """Task 2: Perform basic data analysis."""
    print("="*60)
    print("TASK 2: BASIC DATA ANALYSIS")
    print("="*60)

    # Basic statistics
    print("Basic Statistics of Numerical Columns:")
    basic_stats = iris_df.describe()
    print(basic_stats)
    print()

    # Group analysis by species
    print("Group Analysis by Species:")
    print("Mean values by species:")
    species_means = iris_df.groupby('species').mean()
    print(species_means)
    print()

    print("Count by species:")
    species_counts = iris_df.groupby('species').size()
    print(species_counts)
    print()

    # Detailed groupby analysis
    print("Detailed statistics by species:")
    species_detailed = iris_df.groupby('species').agg({
        'sepal length (cm)': ['mean', 'std', 'min', 'max'],
        'petal length (cm)': ['mean', 'std', 'min', 'max']
    })
    print(species_detailed)
    print()

    # Key findings
    print("KEY FINDINGS FROM ANALYSIS:")
    print("1. Dataset contains 150 samples with 4 numerical features and 1 categorical target")
    print("2. No missing values detected - clean dataset")
    print("3. Equal distribution: 50 samples per species")
    print("4. Petal measurements show larger variation than sepal measurements")
    print("5. Clear differences between species in petal dimensions")
    print("6. Setosa species clearly distinct from Versicolor and Virginica")
    print()

    print("TASK 2 COMPLETED ✅\n")
    return species_means, basic_stats

def create_visualizations(iris_df):
    """Task 3: Create four different types of visualizations."""
    print("="*60)
    print("TASK 3: DATA VISUALIZATION")
    print("="*60)

    # 1. Line Chart - Sepal length trends across samples
    print("Creating Line Chart...")
    plt.figure(figsize=(12, 6))

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    for i, species in enumerate(iris_df['species'].unique()):
        species_data = iris_df[iris_df['species'] == species]
        plt.plot(species_data.index, species_data['sepal length (cm)'], 
                marker='o', markersize=4, linewidth=2, label=species.title(), 
                alpha=0.8, color=colors[i])

    plt.title('Sepal Length Trends Across Sample Index by Species', fontsize=16, fontweight='bold')
    plt.xlabel('Sample Index', fontsize=12)
    plt.ylabel('Sepal Length (cm)', fontsize=12)
    plt.legend(title='Species', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('line_chart_sepal_length_trends.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Line chart saved as 'line_chart_sepal_length_trends.png'\n")

    # 2. Bar Chart - Mean measurements comparison
    print("Creating Bar Charts...")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

    for i, feature in enumerate(features):
        ax = axes[i//2, i%2]
        means = iris_df.groupby('species')[feature].mean()
        bars = means.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.8)

        ax.set_title(f'Mean {feature.title()} by Species', fontweight='bold')
        ax.set_ylabel(f'{feature.title()}')
        ax.set_xlabel('Species')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3)

        # Add value labels on bars
        for bar in bars.patches:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{height:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig('bar_chart_mean_comparisons.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Bar charts saved as 'bar_chart_mean_comparisons.png'\n")

    # 3. Histogram - Distribution of petal length
    print("Creating Histograms...")
    plt.figure(figsize=(12, 8))

    # Overall histogram
    plt.subplot(2, 2, (1, 2))
    plt.hist(iris_df['petal length (cm)'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Overall Distribution of Petal Length', fontweight='bold', fontsize=14)
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)

    # Species-specific histograms
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    species_list = iris_df['species'].unique()

    for i, (species, color) in enumerate(zip(species_list, colors)):
        plt.subplot(2, 3, i+4)
        species_data = iris_df[iris_df['species'] == species]['petal length (cm)']
        plt.hist(species_data, bins=10, alpha=0.8, color=color, edgecolor='black')
        plt.title(f'{species.title()}', fontweight='bold')
        plt.xlabel('Petal Length (cm)')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('histogram_petal_length_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Histograms saved as 'histogram_petal_length_distribution.png'\n")

    # 4. Scatter Plot - Sepal Length vs Petal Length relationship
    print("Creating Scatter Plot...")
    plt.figure(figsize=(12, 8))

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    species_list = iris_df['species'].unique()

    for species, color in zip(species_list, colors):
        species_data = iris_df[iris_df['species'] == species]
        plt.scatter(species_data['sepal length (cm)'], species_data['petal length (cm)'],
                    c=color, label=species.title(), alpha=0.7, s=60, edgecolors='black', linewidth=0.5)

    plt.title('Sepal Length vs Petal Length by Species', fontweight='bold', fontsize=16)
    plt.xlabel('Sepal Length (cm)', fontsize=12)
    plt.ylabel('Petal Length (cm)', fontsize=12)
    plt.legend(title='Species', fontsize=10)
    plt.grid(True, alpha=0.3)

    # Add correlation coefficient
    correlation = iris_df['sepal length (cm)'].corr(iris_df['petal length (cm)'])
    plt.text(0.05, 0.95, f'Overall Correlation: {correlation:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.savefig('scatter_plot_sepal_vs_petal_length.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Scatter plot saved as 'scatter_plot_sepal_vs_petal_length.png'\n")

    print("TASK 3 COMPLETED ✅\n")

def additional_analysis(iris_df):
    """Additional analysis: Correlation matrix and pair plot."""
    print("="*60)
    print("ADDITIONAL ANALYSIS")
    print("="*60)

    # Correlation matrix heatmap
    print("Creating Correlation Matrix...")
    plt.figure(figsize=(10, 8))
    correlation_matrix = iris_df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0,
                square=True, linewidths=0.5, fmt='.3f')
    plt.title('Correlation Matrix of Iris Features', fontweight='bold', fontsize=16)
    plt.tight_layout()
    plt.savefig('correlation_matrix_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Correlation matrix saved as 'correlation_matrix_heatmap.png'\n")

    # Pair plot for comprehensive view
    print("Creating Pair Plot...")
    plt.figure(figsize=(12, 10))
    pair_plot = sns.pairplot(iris_df, hue='species', markers=['o', 's', '^'], 
                            diag_kind='hist', palette='husl')
    pair_plot.fig.suptitle('Pairwise Relationships in Iris Dataset', 
                           fontweight='bold', fontsize=16, y=1.02)
    plt.savefig('pairplot_comprehensive_view.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Pair plot saved as 'pairplot_comprehensive_view.png'\n")

def print_summary():
    """Print final summary and conclusions."""
    print("="*60)
    print("SUMMARY AND CONCLUSIONS")
    print("="*60)

    print("KEY INSIGHTS DISCOVERED:")
    print("1. Data Quality: Clean dataset with no missing values and balanced classes")
    print("2. Species Separation: Setosa clearly separable, Versicolor and Virginica show overlap")
    print("3. Feature Relationships: Strong correlation between petal measurements")
    print("4. Distribution Patterns: Bimodal distribution indicates natural clustering")
    print("5. Classification Potential: Clear separation suggests high accuracy achievable")
    print()

    print("TECHNICAL SKILLS DEMONSTRATED:")
    print("✅ Pandas data loading and exploration")
    print("✅ Missing value detection and handling")
    print("✅ Groupby operations and aggregations")
    print("✅ Statistical analysis with describe()")
    print("✅ Multiple visualization techniques")
    print("✅ Plot customization and styling")
    print("✅ Error handling and data validation")
    print()

    print("FILES GENERATED:")
    print("📁 line_chart_sepal_length_trends.png")
    print("📁 bar_chart_mean_comparisons.png")
    print("📁 histogram_petal_length_distribution.png")
    print("📁 scatter_plot_sepal_vs_petal_length.png")
    print("📁 correlation_matrix_heatmap.png")
    print("📁 pairplot_comprehensive_view.png")
    print()

    print("🎉 ASSIGNMENT COMPLETED SUCCESSFULLY!")

def main():
    """Main function to execute the complete analysis."""
    print("📊 PANDAS & MATPLOTLIB DATA ANALYSIS ASSIGNMENT")
    print("Analyzing the Iris Dataset")
    print("="*60)

    # Setup plotting environment
    setup_plotting()

    # Task 1: Load and explore data
    iris_df = load_and_explore_data()

    if iris_df is not None:
        # Task 2: Basic data analysis
        species_means, basic_stats = analyze_data(iris_df)

        # Task 3: Create visualizations
        create_visualizations(iris_df)

        # Additional analysis
        additional_analysis(iris_df)

        # Final summary
        print_summary()
    else:
        print("❌ Could not proceed with analysis due to data loading error")

if __name__ == "__main__":
    main()
