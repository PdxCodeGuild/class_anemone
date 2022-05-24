import requests
from bs4 import BeautifulSoup


#for url in ['https://realpython.github.io/fake-jobs/']:
  #  try:
  #      response = requests.get(url)
#
  #      response.raise_for_status()
  #  except HTTPError as http_err:
  #      print(f'HTTP ERROR OCCURED: {http_err}')
  #  except Exception as err: 
   #     print(f'other error occured: {err}')
  #  else:
  #      print('success')

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

job_elements = results.find_all("div", class_="card-content")

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
#print(python_jobs)
 

#print(results.prettify())