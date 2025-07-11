import pandas as pd

# Load scraped data
df = pd.read_csv("data/github_trending.csv")

# Remove rows with missing Repo or Skill
df.dropna(subset=["Repo", "Skill"], inplace=True)

# Convert Stars to numeric (remove 'k', 'M', etc.)
def convert_stars(star_str):
    try:
        star_str = str(star_str).lower().strip()
        if 'k' in star_str:
            return float(star_str.replace('k', '')) * 1000
        elif 'm' in star_str:
            return float(star_str.replace('m', '')) * 1000000
        else:
            return float(star_str.replace(',', ''))
    except:
        return 0

df['Stars'] = df['Stars'].apply(convert_stars)

# Save cleaned version
df.to_csv("data/github_trending_cleaned.csv", index=False)
print("✅ Cleaned GitHub data saved.")
