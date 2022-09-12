from getkey import getkey, key
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

query = 'site:linkedin.com/in/ AND "PHP developer" AND "Islamabad"'
file_name = 'results_file.csv'

driver.get('https:www.google.com')
time.sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(query)
time.sleep(0.5)

search_query.send_keys(key.ENTER)
time.sleep(3)

src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
hrefs =  soup.find_all('a', href=True)
profileArray = []
for link in hrefs:
    if("https://pk.linkedin.com/in/" in link['href']):
        profilelink = link['href']
        profileArray.append(profilelink)
        
  
print(profileArray)
with open('profiles.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write multiple rows
    writer.writerow(profileArray)


