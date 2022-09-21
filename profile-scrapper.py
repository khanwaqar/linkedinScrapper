from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json

def index_in_list(a_list, index):
    value = index < len(a_list)
    return value


# file = open('profiles.csv')

# type(file)
# csvreader = csv.reader(file)

# rows = []
# profilesArray = []
# for row in csvreader:
#     rows.append(row)

# file.close()

# for profile_urlArr in rows:
#   for profile_url in profile_urlArr:
#   	profilesArray.append(profile_url)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com/uas/login")

time.sleep(5)

username = driver.find_element_by_id("username")

username.send_keys("developer.web289@gmail.com")

pword = driver.find_element_by_id("password")
pword.send_keys("rescue1122")		

driver.find_element_by_xpath("//button[@type='submit']").click()

profilesArray = [
 "https://www.linkedin.com/in/mirza-raheel-677b7232/",
 "https://www.linkedin.com/in/waqarirshadkhan/",
 "https://www.linkedin.com/in/musawir-mk/",
 "https://www.linkedin.com/in/tamoorshayat/",
 "https://www.linkedin.com/in/elahiehsan/",
 ]

info = []
for profile_url in profilesArray:
  print(profile_url)
  profile = dict()
  time.sleep(20)
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
  try:
    about = soup.find("div", {"id": "about"}).find_next_sibling("div", {"class", "display-flex ph5 pv3"}).find("div").get_text().strip()
  except:
    about = ""

  experiences = []
  educations = []
  skills = []
  
  driver.get(profile_url+"/details/experience/")
  time.sleep(5)
  exp_src = driver.page_source
    
  # Now using beautiful soup
  exp_soup = BeautifulSoup(exp_src, 'lxml')
  li_tags = exp_soup.find_all("li", {"class", "pvs-list__paged-list-item"})
  for li_tag in li_tags:
      experience = dict()
      try:
          experience['job_title'] = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
          experience['company_name'] = li_tag.find("span", {"class", "t-normal"}).find("span").get_text().strip()
          experience['joining_date'] = li_tag.find("span", {"class", "t-black--light"}).find("span").get_text().strip()
      except:
          continue
      experiences.append(experience)

  driver.get(profile_url+"/details/education/")
  time.sleep(5)
  edu_src = driver.page_source
  edu_soup = BeautifulSoup(edu_src, 'lxml')
  li_tags = edu_soup.find_all("li", {"class", "pvs-list__paged-list-item"})
  for li_tag in li_tags:
      education = dict()
      try:
          education['institute'] = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
          education['degree'] = li_tag.find("span", {"class", "t-normal"}).find("span").get_text().strip()
          education['duration'] = li_tag.find("span", {"class", "t-black--light"}).find("span").get_text().strip()
      except:
          continue
      educations.append(education)
  
  driver.get(profile_url+"/details/skills/")
  time.sleep(5)
  skills_src = driver.page_source
  skills_soup = BeautifulSoup(skills_src, 'lxml')
  li_tags = skills_soup.find_all("li", {"class", "pvs-list__paged-list-item"})
  for li_tag in li_tags:
      try:
          skill = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
          skills.append(skill)
      except:
          continue
  
  profile['name'] = name
  profile['url'] = profile_url
  profile['profile_pic'] = profile_pic
  profile['designation'] = works_at
  profile['company'] = company
  profile['university'] = university
  profile['location'] = location
  profile['about'] = about
  profile['experience'] = experiences
  profile['education'] = educations
  profile['skills'] = skills
  
  print(profile)
  info.append(profile)

print(info)

fieldnames = ['name', 'url', 'profile_pic',  'designation', 'company', 'university',  'location', 'about', 'experience', 'education', 'skills']
with open('data_test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(info)

with open('result_test.json', 'w') as fp:
    json.dump(info, fp)


driver.close()









