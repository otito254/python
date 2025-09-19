# CORD-19 Data Analysis Project

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A comprehensive data analysis project exploring COVID-19 research papers using the CORD-19 dataset. This project includes data exploration, visualization, and an interactive Streamlit web application.

## 🎯 Project Overview

This assignment demonstrates fundamental data science skills through:
- **Data Loading & Exploration**: Loading and examining the CORD-19 metadata
- **Data Cleaning**: Handling missing values and preparing data for analysis
- **Visualization**: Creating meaningful charts and graphs
- **Interactive Dashboard**: Building a Streamlit web application
- **Insights Generation**: Extracting key findings from the data

## 📊 Dataset Information

The project uses the CORD-19 (COVID-19 Open Research Dataset) metadata file containing:
- Paper titles and abstracts
- Publication dates and years
- Author information
- Journal names
- Source information (PMC, PubMed, etc.)
- DOI and other identifiers

**Note**: A sample dataset is included for demonstration purposes. For the full dataset, visit [Kaggle CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

## 🚀 Features

### Data Analysis
- **Temporal Analysis**: Publication trends over time
- **Journal Analysis**: Most active journals in COVID-19 research
- **Word Frequency**: Most common terms in paper titles
- **Source Distribution**: Papers by data source
- **Abstract Analysis**: Text length statistics

### Interactive Dashboard
- **Filter Controls**: Year range, journal, and source filters
- **Real-time Updates**: Dynamic visualizations based on selections
- **Multiple Views**: Timeline, journal, word analysis, and source tabs
- **Data Sample**: Preview of filtered dataset

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the data** (Optional)
   - Download `metadata.csv` from [Kaggle CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
   - Place it in the project root directory
   - Alternatively, use the provided sample dataset

## 🏃‍♂️ Running the Project

### Option 1: Jupyter Notebook Analysis
```bash
# If you have Jupyter installed
jupyter notebook cord19_analysis.ipynb
```

### Option 2: Python Script
```bash
# Run the analysis as a Python script
python -c "exec(open('cord19_analysis.py').read())"
```

### Option 3: Streamlit Web Application
```bash
# Launch the interactive dashboard
streamlit run streamlit_app.py
```

The Streamlit app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
Frameworks_Assignment/
│
├── streamlit_app.py          # Main Streamlit application
├── cord19_analysis.md        # Detailed analysis notebook/script
├── metadata.csv              # Sample CORD-19 dataset
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── visualizations/            # Generated visualizations
```

## 📈 Key Findings

Based on the sample dataset analysis:

1. **Publication Peak**: Highest number of publications in 2020-2021 (COVID-19 pandemic period)
2. **Top Journals**: Nature, Science, The Lancet leading in COVID-19 research publication
3. **Common Terms**: "COVID-19", "SARS-CoV-2", "coronavirus" most frequent in titles
4. **Data Sources**: PMC and PubMed are primary sources for research papers
5. **Research Focus**: Strong emphasis on clinical studies, vaccines, and treatment

## 🎨 Visualizations

The project generates several types of visualizations:

- **Bar Charts**: Publications by year, top journals, word frequency
- **Pie Chart**: Distribution by data source  
- **Histogram**: Abstract length distribution
- **Word Cloud**: Visual representation of title keywords
- **Interactive Plots**: Real-time filtering in Streamlit app

## 🧰 Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Static visualizations
- **Streamlit**: Interactive web application
- **WordCloud**: Text visualization
- **NumPy**: Numerical computations

## 🔍 Usage Examples

### Basic Data Exploration
```python
import pandas as pd
df = pd.read_csv('metadata.csv')
print(f"Dataset shape: {df.shape}")
print(df.head())
```

### Running Streamlit App
```bash
streamlit run streamlit_app.py
```

### Custom Analysis
```python
# Filter papers by year
df_2020 = df[df['year'] == 2020]
top_journals_2020 = df_2020['journal'].value_counts().head(10)
print(top_journals_2020)
```

## 📊 Sample Screenshots

*check visualization folder

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Assignment Requirements Checklist

- [x] **Data Loading**: Load and explore CORD-19 metadata
- [x] **Data Cleaning**: Handle missing values and prepare data
- [x] **Visualizations**: Create multiple types of charts
- [x] **Streamlit App**: Interactive web application
- [x] **Documentation**: Comprehensive README and comments
- [x] **GitHub Repository**: All files organized and uploaded

## 🐛 Troubleshooting

### Common Issues

1. **Module Not Found Error**
   ```bash
   pip install -r requirements.txt
   ```

2. **Data File Not Found**
   - Ensure `metadata.csv` is in the project root
   - Or run the data generation script first

3. **Streamlit Port Already in Use**
   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CORD-19 Dataset**: Allen Institute for AI
- **Streamlit Team**: For the excellent web app framework
- **Open Source Community**: For the amazing Python libraries

## 📧 Contact

- **Student**: [Your Name]
- **Email**: [your.email@university.edu]
- **GitHub**: [https://github.com/yourusername](https://github.com/yourusername)
- **Project Link**: [https://github.com/yourusername/Frameworks_Assignment](https://github.com/yourusername/Frameworks_Assignment)

---

**Note**: This project is completed as part of a data science frameworks assignment. The sample data provided is for educational purposes only.
