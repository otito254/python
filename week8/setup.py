#!/usr/bin/env python3
"""
Setup Script for CORD-19 Data Analysis Project
===============================================

This script helps set up the environment and verify installation.
"""

import subprocess
import sys
import os
import importlib

def check_python_version():
    """Check if Python version is compatible"""
    print("Checking Python version...")
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required. Current version:", sys.version)
        return False
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True

def install_requirements():
    """Install required packages"""
    print("\nInstalling required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install packages: {e}")
        return False

def verify_packages():
    """Verify that all required packages are installed"""
    print("\nVerifying package installation...")
    
    required_packages = [
        'pandas', 'matplotlib', 'seaborn', 'streamlit', 
        'numpy', 'wordcloud', 'PIL'
    ]
    
    failed_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                importlib.import_module('PIL')
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_packages.append(package)
    
    if failed_packages:
        print(f"\n❌ Failed to import: {', '.join(failed_packages)}")
        return False
    else:
        print("\n✅ All packages verified successfully")
        return True

def check_data_file():
    """Check if data file exists"""
    print("\nChecking data file...")
    if os.path.exists('metadata.csv'):
        print("✅ metadata.csv found")
        return True
    else:
        print("⚠️  metadata.csv not found")
        print("   - A sample dataset will be created when you run the analysis")
        print("   - For the full dataset, download from Kaggle CORD-19")
        return False

def create_directories():
    """Create necessary directories"""
    print("\nCreating directories...")
    
    directories = ['images', 'data', 'outputs']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory}/ directory")
        else:
            print(f"✅ {directory}/ directory exists")

def run_tests():
    """Run basic functionality tests"""
    print("\nRunning basic tests...")
    
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        
        # Test data creation
        test_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['x', 'y', 'z']
        })
        
        # Test plotting
        plt.figure(figsize=(6, 4))
        plt.plot([1, 2, 3], [1, 4, 2])
        plt.close()
        
        print("✅ Basic functionality test passed")
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def display_usage_instructions():
    """Display usage instructions"""
    print("\n" + "="*60)
    print("SETUP COMPLETE - USAGE INSTRUCTIONS")
    print("="*60)
    
    print("""
🚀 Getting Started:

1. Run the analysis script:
   python cord19_analysis.py

2. Launch the Streamlit app:
   streamlit run streamlit_app.py

3. View generated visualizations in the images/ folder

📁 Project Structure:
   ├── cord19_analysis.py     # Main analysis script
   ├── streamlit_app.py       # Interactive web app
   ├── metadata.csv           # Dataset (will be created if missing)
   ├── requirements.txt       # Python dependencies
   ├── README.md              # Project documentation
   └── images/                # Generated visualizations

💡 Tips:
   - The analysis creates sample data if metadata.csv is missing
   - All visualizations are saved as PNG files
   - The Streamlit app provides interactive exploration
   - Check README.md for detailed documentation

📚 Resources:
   - Kaggle CORD-19: https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge
   - Streamlit docs: https://docs.streamlit.io
   - Pandas docs: https://pandas.pydata.org/docs
""")

def main():
    """Main setup function"""
    print("CORD-19 Data Analysis Project Setup")
    print("=" * 40)
    
    all_checks_passed = True
    
    # Run all checks
    if not check_python_version():
        all_checks_passed = False
    
    if not install_requirements():
        all_checks_passed = False
    
    if not verify_packages():
        all_checks_passed = False
    
    check_data_file()  # This is optional
    
    create_directories()
    
    if not run_tests():
        all_checks_passed = False
    
    if all_checks_passed:
        print("\n🎉 Setup completed successfully!")
        display_usage_instructions()
    else:
        print("\n❌ Setup completed with some issues.")
        print("Please check the errors above and resolve them before proceeding.")

if __name__ == "__main__":
    main()