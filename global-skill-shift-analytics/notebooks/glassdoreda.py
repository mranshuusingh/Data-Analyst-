import pandas as pd
import os

# Define your CSV paths (update names if your file names differ)
folder_path = r"C:\Users\hi\Desktop\global-skill-shift-analytics"  # folder where your 3 CSV files are stored
files = ["eda_data.csv", "glassdoor_jobs.csv", "salary_data_cleaned.csv"]

# Load and combine
dfs = [pd.read_csv(os.path.join(folder_path, f)) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Drop rows missing important values
df.dropna(subset=["Job Title", "Company Name", "avg_salary", "job_state", "Industry"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize job titles
df["Job Title"] = df["Job Title"].str.title()

# Ensure salary columns are numeric
salary_cols = ["min_salary", "max_salary", "avg_salary"]
for col in salary_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows with null salaries after conversion
df.dropna(subset=salary_cols, inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save the cleaned data
output_path = "data/us_jobs_cleaned.csv"
df.to_csv(output_path, index=False)

print("✅ US job data cleaned and saved to:", output_path)
