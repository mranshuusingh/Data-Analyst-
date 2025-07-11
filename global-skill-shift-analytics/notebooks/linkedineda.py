import pandas as pd;
df = pd.read_csv("C:\\Users\\hi\\Desktop\\global-skill-shift-analytics\\data\\linkedin_jobs.csv")

# Drop rows where all main fields are blank
df_cleaned = df.dropna(subset=["title", "company", "location"], how="all")

# Save it again
df_cleaned.to_csv("C:\\Users\\hi\\Desktop\\global-skill-shift-analytics\\data\\linkedin_jobs_cleaned.csv", index=False)
print("✅ Cleaned data saved.")
