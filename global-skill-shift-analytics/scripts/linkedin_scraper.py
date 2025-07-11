import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------- CONFIG -------------------------
skills = ["Python", "SQL", "Power BI", "Excel", "React", "AWS", "Machine Learning", "DevOps"]
job_data = []

# Set manual save path (like Google Trends)
save_path = r"C:\Users\hi\Desktop\global-skill-shift-analytics\data\linkedin_jobs.csv"

# ------------------- SETUP SELENIUM ---------------------
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# --------------------- SCRAPE JOBS ----------------------
for skill in skills:
    print(f"Scraping jobs for: {skill}")
    url = f"https://www.linkedin.com/jobs/search/?keywords={skill}&location=India"
    driver.get(url)
    time.sleep(5)

    try:
        jobs = driver.find_elements(By.CLASS_NAME, "base-search-card__info")
        for job in jobs[:10]:  # top 10 jobs only
            try:
                title = job.find_element(By.CLASS_NAME, "base-search-card__title").text.strip()
                company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip()
                location = job.find_element(By.CLASS_NAME, "job-search-card__location").text.strip()

                job_data.append({
                    "skill": skill,
                    "title": title,
                    "company": company,
                    "location": location
                })
            except Exception:
                continue
    except Exception as e:
        print(f"Error scraping {skill}: {e}")
        continue

driver.quit()

# ------------------ SAVE TO CSV -------------------------
if job_data:
    df = pd.DataFrame(job_data)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"\n✅ Data saved to: {save_path}")
else:
    print("\n⚠️ No data scraped. CSV not saved.")
