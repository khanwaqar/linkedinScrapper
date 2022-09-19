from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json

def index_in_list(a_list, index):
    value = index < len(a_list)
    return value


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
driver.get("https://linkedin.com/uas/login")

time.sleep(5)

username = driver.find_element_by_id("username")

username.send_keys("developer.web289@gmail.com")

pword = driver.find_element_by_id("password")
pword.send_keys("rescue1122")		

driver.find_element_by_xpath("//button[@type='submit']").click()

# profilesArray = [
#  "https://www.linkedin.com/in/mirza-raheel-677b7232/",
#  "https://www.linkedin.com/in/hamid-ali-5bb93716b/",
#  "https://www.linkedin.com/in/waqarirshadkhan/",
#  "https://www.linkedin.com/in/musawir-mk/",
#  "https://www.linkedin.com/in/tamoorshayat/",
#  "https://www.linkedin.com/in/elahiehsan/",
#  "https://www.linkedin.com/in/amaadjaved/",
#  "https://www.linkedin.com/in/muhammad-usman-a408641a/",
#  "https://www.linkedin.com/in/hassan-raza-693351224/",
#  "https://www.linkedin.com/in/zehra-ahmed/"

#  ]
info = []
for profile_url in profilesArray:
  print(profile_url)
  profile = dict()
  time.sleep(3)
  driver.get(profile_url)
  src = driver.page_source
  soup = BeautifulSoup(src, 'lxml')
  try:
    profilePicHTML = soup.find("img", {'class', "pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view"})
    profile_pic = profilePicHTML['src']
  except:
    profile_pic = ""
  intro = soup.find('div', {'class': 'ph5'})
  try: 
    name_loc = intro.find("h1")
    name = name_loc.get_text().strip() 
  except:
    name = ""
  
  try:
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    works_at = works_at_loc.get_text().strip()
  except: 
    works_at = ""
  try:

    location_loc = intro.find_all("span", {'class': 'text-body-small'})
    company = ""
    if(index_in_list(location_loc, 0)): 
      company = location_loc[0].get_text().strip()
    
    university = ""
    if(index_in_list(location_loc, 1)):
      university = location_loc[1].get_text().strip()
    
    location = ""
    if(index_in_list(location_loc, 2)):
      location = location_loc[2].get_text().strip()
  except:
    company = ""
    university = ""
    location = ""
  
  profile['name'] = name
  profile['url'] = profile_url
  profile['profile_pic'] = profile_pic
  profile['designation'] = works_at
  profile['company'] = company
  profile['university'] = university
  profile['location'] = location
  
  print(profile)
  info.append(profile)

print(info)

fieldnames = ['name', 'url', 'profile_pic',  'designation', 'company', 'university',  'location']
with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(info)

with open('result.json', 'w') as fp:
    json.dump(info, fp)


driver.close()









