from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv
file = open('profiles.csv')

type(file)
csvreader = csv.reader(file)

rows = []
profilesArray = []
for row in csvreader:
    rows.append(row)

file.close()

for profile_urlArr in rows:
  for profile_url in profile_urlArr:
  	profilesArray.append(profile_url)


driver = webdriver.Chrome(ChromeDriverManager().install())

i = 10
count = 0
while count < i:
    driver.get("https://www.youtube.com/watch?v=S_eu8Or4HvY")
    count = count + 1
    time.sleep(60)