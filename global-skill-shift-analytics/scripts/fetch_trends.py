# scripts/fetch_trends.py

from pytrends.request import TrendReq
import pandas as pd
import time
import os

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=330)

# Skill list to track
skills = [
    'Python', 'SQL', 'Power BI', 'AWS', 'Machine Learning',
    'React', 'Cybersecurity', 'Data Science', 'DevOps', 'Cloud Computing'
]

# Final DataFrame
final_df = pd.DataFrame()

print("Fetching trends for skills...")

for skill in skills:
    try:
        pytrends.build_payload([skill], cat=0, timeframe='today 12-m', geo='', gprop='')
        data = pytrends.interest_over_time()
        
        if not data.empty:
            data = data.reset_index()[['date', skill]]
            data.rename(columns={skill: 'trend'}, inplace=True)
            data['skill'] = skill
            final_df = pd.concat([final_df, data], ignore_index=True)

        time.sleep(1)  # Avoid getting blocked
    except Exception as e:
        print(f"Error fetching {skill}: {e}")

# ✅ Build absolute path to save CSV
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(output_dir, exist_ok=True)  # Ensure data/ folder exists
output_path = os.path.join(output_dir, 'google_trends.csv')

# ✅ Save to CSV
final_df.to_csv(output_path, index=False)
print(f"✅ Trends data saved successfully to: {output_path}")
