import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os

# Setup
driver_path = r"C:\Users\hi\Desktop\global-skill-shift-analytics\drivers\chromedriver.exe"
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: hide browser
driver = webdriver.Chrome(service=service, options=options)

skills = ["Python", "SQL", "PowerBI", "Excel", "React", "AWS", "Machine-Learning", "DevOps"]
base_url = "https://github.com/trending/"

data = []

print("🚀 Scraping GitHub Trending...")

for skill in skills:
    print(f"→ {skill}...")
    try:
        url = base_url + skill.lower() + "?since=daily"
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        repos = soup.find_all("article", class_="Box-row")
        
        for repo in repos:
            title = repo.find("h2").text.strip().replace("\n", "").replace(" ", "")
            desc_tag = repo.find("p")
            description = desc_tag.text.strip() if desc_tag else ""
            stars_tag = repo.find("span", class_="Counter")
            stars = stars_tag.text.strip() if stars_tag else ""
            
            data.append({
                "Skill": skill,
                "Repo": title,
                "Description": description,
                "Stars": stars
            })
    except Exception as e:
        print(f"⚠️ Error scraping {skill}: {e}")

# Close driver
driver.quit()

# Convert to DataFrame and Save
df = pd.DataFrame(data)

# Check if there's valid data
if not df.empty:
    output_path = os.path.join("data", "github_trending.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Saved GitHub data to: {output_path}")
else:
    print("❌ No data scraped. Check site structure or headless rendering.")
