'''
import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.myjobmag.co.ke/")
response.raise_for_status() 
soup = BeautifulSoup(response.text, "html.parser")
data = response.text
print(data)
'''
 # Raise an exception for unsuccessful requests

# Raise an exception for unsuccessful requests
import requests
from bs4 import BeautifulSoup
import json

def scrape_jobs(url):
  """Scrapes job listings from a website and returns them as a JSON object."""

  # Make a GET request to the website
  response = requests.get(url)

  # Check for successful response
  if response.status_code != 200:
    print("Error fetching webpage!")
    return None

  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find the right section containing job listings (modify based on the website's structure)
  job_listings_section = soup.find('div', class_='left-section')  # Replace with the appropriate class name 

  # If the section is not found, exit
  if not job_listings_section:
      print("Job listings section not found!")
      return None

  # Print a message to indicate successful section identification
  print("Found job listings section!")

  # Find all categories within the listings section (modify based on structure)
  categories = job_listings_section.find_all('ul', class_='job-list')  # Replace with the appropriate class name 
  print(f"Number of categories found: {len(categories)}")

  job_list = categories[0].text.split("\n")
  # Create an empty list to store job data
  for job in job_list:
    print(job)
    
  jobs = []

  # Loop through each category
  for category in categories:
    # Find job listings within each category (modify based on structure)
    job_listings = category.find_all('job-list')  # Replace with the appropriate tag containing job listings
    print(f"Number of job listings in category: {len(job_listings)}")

    # Loop through each job listing
    for job in job_listings:
      # Extract job details (modify based on what information you need)
      # Assuming links are within anchor tags with a specific class
      link_tag = job.find('a', class_='job-item')  # Replace with the appropriate class name for job links
      if link_tag:
          link = link_tag['href']
      else:
          link = None

      # Assuming titles are within specific tags
      title_tag = job.find('h3', class_='mag-b')  # Replace with the appropriate class name for job titles
      if title_tag:
          title = title_tag.text.strip()
      else:
          title = None

      # Create a dictionary for each job (add more fields if needed)
      job_data = {
        "title": title,
        "link": link
      }

      # Add the job data to the list
      if title and link:  # Only add jobs with both title and link
          jobs.append(job_data)

  # Convert the list of jobs to a JSON object with indentation
  json_data = json.dumps(jobs, indent=4)

  return json_data

# Example usage
url = "https://www.myjobmag.co.ke/"  # Replace with the actual website URL
json_data = scrape_jobs(url)

# Print the JSON data
if json_data:
  print(json_data)
else:
  print("Failed to scrape jobs!")
