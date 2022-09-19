from getkey import getkey, key

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv
driver = webdriver.Chrome(ChromeDriverManager().install())

query = 'site:linkedin.com/in/ AND "React Native" AND "Islamabad"'
file_name = 'results_file.csv'

driver.get('http:www.google.com/')
time.sleep(4)

search_query = driver.find_element_by_name('q')
search_query.send_keys(query)
time.sleep(3)

search_query.send_keys(key.ENTER)
time.sleep(3)

isNextPage = True
profileArray = []

#nextPageURL = nextpage['href']
# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
while(isNextPage):
    src = driver.page_source
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    hrefs =  soup.find_all('a', href=True)
    for link in hrefs:
        if("https://pk.linkedin.com/in/" in link['href']):
            profilelink = link['href']
            profileArray.append([profilelink])
    print(profileArray)
    try:
        nextpage = driver.find_element_by_id("pnnext")
        nextpage.click()
    except:
        print("\nNo More Pages to Scrap\n")
        nextpage = False
    if(nextpage):
        time.sleep(5)
    else:
        isNextPage = False

with open('profiles.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(profileArray)


