import requests
from bs4 import BeautifulSoup
import csv

# URL of LinkedIn Jobs page (Example: Data Analyst jobs in India)
url = "https://www.linkedin.com/jobs/search/?keywords=data%20analyst&location=India"

# Set headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Make request to LinkedIn (May require authentication)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find job postings
jobs = soup.find_all("div", class_="base-search-card__info")


# Open CSV file for writing
with open("linkedin_jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write headers (column names)
    writer.writerow(["Job Title", "Company", "Location"])
    
    # Loop through scraped jobs and write data
    for job in jobs:
        title = job.find("h3").text.strip()
        company = job.find("h4").text.strip()
        location = job.find("span", class_="job-search-card__location").text.strip()
        writer.writerow([title, company, location])

print("ok Data saved successfully to linkedin_jobs.csv!")

# Extract job details
for job in jobs:
    title = job.find("h3").text.strip()
    company = job.find("h4").text.strip()
    location = job.find("span", class_="job-search-card__location").text.strip()
    print(f"Job Title: {title}, Company: {company}, Location: {location}")
