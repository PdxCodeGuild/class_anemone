import requests
from bs4 import BeautifulSoup

#saved_html = []

#with open('websites.txt', 'r') as file:
    #lines = file.read().split('\n')
   

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
#creating beautiful soup element
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")


#Identifying the appropriate tags for the information that we want to pull
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
#H2 tags from the websirte include information about the position that is being listed
job_elements = results.find_all("div", class_="card-content")

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    h2_element = job_element.find("h2", class_="title")
    h3_element = job_element.find("h3", class_="company")
    p_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    print(h2_element.text)
    print(h3_element.text)
    print(p_element.text)
#print(python_jobs)
 

#print(results.prettify())