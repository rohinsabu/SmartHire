"""
load_data.py

Loads the raw datasets and displays basic information.
"""

from pathlib import Path
import pandas as pd

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Dataset paths
RESUME_DATA = RAW_DATA_DIR / "UpdatedResumeDataSet.csv"
NAUKRI_DATA = RAW_DATA_DIR / "marketing_sample_for_naukri_com-jobs__20190701_20190830__30k_data.csv"
LINKEDIN_DATA = RAW_DATA_DIR / "postings.csv"

# Load Datasets 


print("Loading datasets...\n")

resume_df = pd.read_csv(RESUME_DATA)
naukri_df = pd.read_csv(NAUKRI_DATA)
linkedin_df = pd.read_csv(LINKEDIN_DATA)

print("Datasets loaded successfully!\n")

# Resume Dataset

print("=" * 60)
print("RESUME DATASET")
print("=" * 60)
print(f"Shape: {resume_df.shape}\n")
print("Columns:")
print(resume_df.columns.tolist())
print("\nInfo:")
resume_df.info()

# Naukri Dataset

print("\n" + "=" * 60)
print("NAUKRI DATASET")
print("=" * 60)
print(f"Shape: {naukri_df.shape}\n")
print("Columns:")
print(naukri_df.columns.tolist())
print("\nInfo:")
naukri_df.info()

# LinkedIn Dataset

print("\n" + "=" * 60)
print("LINKEDIN DATASET")
print("=" * 60)
print(f"Shape: {linkedin_df.shape}\n")
print("Columns:")
print(linkedin_df.columns.tolist())
print("\nInfo:")
linkedin_df.info()