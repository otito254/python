import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import numpy as np

# Set page config
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.sub-header {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 1rem;
}
.metric-container {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Load and cache data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('metadata.csv')
        # Data cleaning
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
        df['abstract_word_count'] = df['abstract'].fillna('').str.split().str.len()
        df['journal'] = df['journal'].fillna('Unknown')
        df['authors'] = df['authors'].fillna('Unknown')
        return df
    except FileNotFoundError:
        st.error("metadata.csv file not found. Please make sure the data file is in the correct location.")
        return None

# Main app
def main():
    # Title
    st.markdown('<h1 class="main-header">🦠 CORD-19 Data Explorer</h1>', unsafe_allow_html=True)
    st.markdown("**Comprehensive analysis of COVID-19 research papers**")
    
    # Load data
    df = load_data()
    if df is None:
        st.stop()
    
    # Sidebar
    st.sidebar.header("🔧 Controls")
    
    # Year filter
    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=int(df['year'].min()),
        max_value=int(df['year'].max()),
        value=(int(df['year'].min()), int(df['year'].max())),
        help="Filter papers by publication year"
    )
    
    # Journal filter
    top_journals = df['journal'].value_counts().head(10).index.tolist()
    selected_journals = st.sidebar.multiselect(
        "Select Journals",
        options=['All'] + top_journals,
        default=['All'],
        help="Filter by specific journals"
    )
    
    # Source filter
    sources = df['source_x'].unique().tolist()
    selected_sources = st.sidebar.multiselect(
        "Select Sources",
        options=['All'] + sources,
        default=['All'],
        help="Filter by data sources"
    )
    
    # Filter data
    filtered_df = df[
        (df['year'] >= year_range[0]) & 
        (df['year'] <= year_range[1])
    ]
    
    if 'All' not in selected_journals:
        filtered_df = filtered_df[filtered_df['journal'].isin(selected_journals)]
    
    if 'All' not in selected_sources:
        filtered_df = filtered_df[filtered_df['source_x'].isin(selected_sources)]
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📄 Total Papers",
            value=f"{len(filtered_df):,}",
            delta=f"{len(filtered_df) - len(df):,}" if len(filtered_df) != len(df) else None
        )
    
    with col2:
        st.metric(
            label="📅 Year Range",
            value=f"{filtered_df['year'].min():.0f}-{filtered_df['year'].max():.0f}"
        )
    
    with col3:
        st.metric(
            label="📚 Unique Journals",
            value=f"{filtered_df['journal'].nunique():,}"
        )
    
    with col4:
        avg_abstract_length = filtered_df['abstract_word_count'].mean()
        st.metric(
            label="📝 Avg Abstract Length",
            value=f"{avg_abstract_length:.0f} words"
        )
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Timeline Analysis", 
        "📚 Journal Analysis", 
        "☁️ Word Analysis", 
        "🔍 Source Analysis",
        "📊 Data Sample"
    ])
    
    with tab1:
        st.markdown('<h2 class="sub-header">Publication Timeline</h2>', unsafe_allow_html=True)
        
        # Publications by year
        yearly_counts = filtered_df['year'].value_counts().sort_index()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(yearly_counts.index, yearly_counts.values, color='#1f77b4', alpha=0.7)
        ax.set_title('COVID-19 Research Publications by Year', fontsize=16, fontweight='bold')
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Number of Publications', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Show yearly statistics
        st.markdown("**Yearly Statistics:**")
        yearly_stats = pd.DataFrame({
            'Year': yearly_counts.index,
            'Papers': yearly_counts.values,
            'Percentage': (yearly_counts.values / yearly_counts.sum() * 100).round(1)
        })
        st.dataframe(yearly_stats, use_container_width=True)
    
    with tab2:
        st.markdown('<h2 class="sub-header">Journal Analysis</h2>', unsafe_allow_html=True)
        
        # Top journals
        top_journals_data = filtered_df['journal'].value_counts().head(15)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.barh(range(len(top_journals_data)), top_journals_data.values, color='#ff7f0e', alpha=0.7)
        ax.set_yticks(range(len(top_journals_data)))
        ax.set_yticklabels(top_journals_data.index)
        ax.set_title('Top 15 Journals Publishing COVID-19 Research', fontsize=16, fontweight='bold')
        ax.set_xlabel('Number of Publications', fontsize=12)
        ax.invert_yaxis()
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2,
                   f'{int(width)}', ha='left', va='center')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Journal statistics
        st.markdown("**Journal Statistics:**")
        journal_stats = pd.DataFrame({
            'Journal': top_journals_data.index,
            'Papers': top_journals_data.values,
            'Percentage': (top_journals_data.values / len(filtered_df) * 100).round(2)
        })
        st.dataframe(journal_stats, use_container_width=True)
    
    with tab3:
        st.markdown('<h2 class="sub-header">Word Analysis</h2>', unsafe_allow_html=True)
        
        # Word frequency analysis
        all_titles = ' '.join(filtered_df['title'].fillna('').str.lower())
        stop_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'study']
        words = [word for word in all_titles.split() if word not in stop_words and len(word) > 2]
        word_freq = Counter(words)
        top_words = word_freq.most_common(20)
        
        # Word frequency chart
        if top_words:
            words, counts = zip(*top_words)
            
            fig, ax = plt.subplots(figsize=(12, 8))
            bars = ax.barh(range(len(words)), counts, color='#2ca02c', alpha=0.7)
            ax.set_yticks(range(len(words)))
            ax.set_yticklabels(words)
            ax.set_title('Most Frequent Words in Paper Titles', fontsize=16, fontweight='bold')
            ax.set_xlabel('Frequency', fontsize=12)
            ax.invert_yaxis()
            
            for i, bar in enumerate(bars):
                width = bar.get_width()
                ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                       f'{int(width)}', ha='left', va='center')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Word Cloud
            st.markdown("**Word Cloud:**")
            try:
                wordcloud = WordCloud(width=800, height=400, 
                                     background_color='white',
                                     colormap='viridis',
                                     max_words=100).generate(all_titles)
                
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                ax.set_title('Word Cloud of Paper Titles', fontsize=16, fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Could not generate word cloud: {e}")
    
    with tab4:
        st.markdown('<h2 class="sub-header">Source Analysis</h2>', unsafe_allow_html=True)
        
        # Source distribution
        source_counts = filtered_df['source_x'].value_counts()
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig, ax = plt.subplots(figsize=(10, 6))
            colors = plt.cm.Set3(np.arange(len(source_counts)))
            wedges, texts, autotexts = ax.pie(source_counts.values, labels=source_counts.index, 
                                            autopct='%1.1f%%', colors=colors, startangle=90)
            ax.set_title('Distribution of Papers by Source', fontsize=16, fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            st.markdown("**Source Statistics:**")
            source_stats = pd.DataFrame({
                'Source': source_counts.index,
                'Papers': source_counts.values,
                'Percentage': (source_counts.values / len(filtered_df) * 100).round(1)
            })
            st.dataframe(source_stats, use_container_width=True)
    
    with tab5:
        st.markdown('<h2 class="sub-header">Data Sample</h2>', unsafe_allow_html=True)
        
        # Show sample data
        st.markdown("**Sample of filtered data:**")
        sample_df = filtered_df[['title', 'authors', 'journal', 'year', 'source_x']].head(20)
        st.dataframe(sample_df, use_container_width=True)
        
        # Data info
        st.markdown("**Dataset Information:**")
        info_data = {
            'Metric': ['Total Rows', 'Total Columns', 'Memory Usage', 'Missing Values'],
            'Value': [
                len(filtered_df),
                len(filtered_df.columns),
                f"{filtered_df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB",
                filtered_df.isnull().sum().sum()
            ]
        }
        st.table(pd.DataFrame(info_data))
    
    # Footer
    st.markdown("---")
    st.markdown("**CORD-19 Data Explorer** | Built with Streamlit | Data Science Assignment")

if __name__ == "__main__":
    main()