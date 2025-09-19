# Let's create a sample CORD-19 metadata file for demonstration
# Since we can't download the actual file, I'll create a realistic sample
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create sample data that mimics CORD-19 metadata structure
n_papers = 1000

# Sample journals
journals = [
    'Nature', 'Science', 'Cell', 'The Lancet', 'New England Journal of Medicine',
    'PLOS ONE', 'BMJ', 'Journal of Medical Virology', 'Virology Journal',
    'International Journal of Infectious Diseases', 'Clinical Infectious Diseases',
    'Emerging Infectious Diseases', 'Journal of Virology', 'Vaccine',
    'Antiviral Research', 'medRxiv', 'bioRxiv'
]

# Sample sources
sources = ['PMC', 'Elsevier', 'PubMed', 'WHO', 'arXiv', 'medRxiv', 'bioRxiv']

# Generate sample titles related to COVID-19
title_keywords = [
    'COVID-19', 'SARS-CoV-2', 'coronavirus', 'pandemic', 'vaccine', 'treatment',
    'infection', 'transmission', 'symptoms', 'diagnosis', 'antibody', 'immunity',
    'outbreak', 'prevention', 'therapy', 'antiviral', 'epidemiology', 'clinical'
]

def generate_title():
    words = random.sample(title_keywords, random.randint(2, 5))
    return ' '.join(words).title() + ' Study'

def generate_abstract():
    sentences = [
        "This study investigates COVID-19 related phenomena.",
        "We analyzed data from multiple sources.",
        "Results show significant findings regarding SARS-CoV-2.",
        "The implications for public health are discussed.",
        "Further research is needed to confirm these findings."
    ]
    return ' '.join(random.sample(sentences, random.randint(2, 4)))

# Generate sample data
data = {
    'cord_uid': [f'cord-{i:06d}' for i in range(n_papers)],
    'sha': [f'sha{i:06d}' if random.random() > 0.3 else None for i in range(n_papers)],
    'source_x': [random.choice(sources) for _ in range(n_papers)],
    'title': [generate_title() for _ in range(n_papers)],
    'doi': [f'10.1000/sample.{i}' if random.random() > 0.2 else None for i in range(n_papers)],
    'pmcid': [f'PMC{random.randint(1000000, 9999999)}' if random.random() > 0.4 else None for _ in range(n_papers)],
    'pubmed_id': [random.randint(10000000, 99999999) if random.random() > 0.3 else None for _ in range(n_papers)],
    'license': [random.choice(['cc-by', 'cc-by-nc', 'no-cc', None]) for _ in range(n_papers)],
    'abstract': [generate_abstract() if random.random() > 0.1 else None for _ in range(n_papers)],
    'publish_time': [],
    'authors': [f'Author {i}, Co-Author {i}' if random.random() > 0.1 else None for i in range(n_papers)],
    'journal': [random.choice(journals) if random.random() > 0.1 else None for _ in range(n_papers)],
    'mag_id': [random.randint(1000000000, 9999999999) if random.random() > 0.5 else None for _ in range(n_papers)],
    'who_covidence_id': [f'WHO-{random.randint(1000, 9999)}' if random.random() > 0.8 else None for _ in range(n_papers)],
    'arxiv_id': [f'2020.{random.randint(1000, 9999)}' if random.random() > 0.9 else None for _ in range(n_papers)],
    'pdf_json_files': [f'document_parses/pdf_json/{i}.json' if random.random() > 0.6 else None for i in range(n_papers)],
    'pmc_json_files': [f'document_parses/pmc_json/{i}.json' if random.random() > 0.7 else None for i in range(n_papers)],
    'url': [f'https://example.com/paper/{i}' if random.random() > 0.5 else None for i in range(n_papers)]
}

# Generate publish dates (focus on 2019-2022)
start_date = datetime(2019, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = (end_date - start_date).days

for _ in range(n_papers):
    if random.random() > 0.05:  # 95% have dates
        random_days = random.randint(0, date_range)
        pub_date = start_date + timedelta(days=random_days)
        # Weight towards 2020-2021 (COVID-19 peak)
        if random.random() < 0.6:
            pub_date = datetime(random.choice([2020, 2021]), 
                              random.randint(1, 12), 
                              random.randint(1, 28))
        data['publish_time'].append(pub_date.strftime('%Y-%m-%d'))
    else:
        data['publish_time'].append(None)

# Create DataFrame
df = pd.DataFrame(data)

# Save the sample dataset
df.to_csv('metadata.csv', index=False)
print(f"Created sample dataset with {len(df)} papers")
print(f"Columns: {list(df.columns)}")
print(f"Sample data:")
print(df.head())