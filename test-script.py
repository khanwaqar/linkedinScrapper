from wsgiref.headers import Headers
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
option.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

# Creating a webdriver instance
#driver = webdriver.Chrome("/usr/bin/chromedriver")
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("developer.web289@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("rescue1122")		

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
profile_url = "https://www.linkedin.com/in/mirza-raheel-677b7232/"
time.sleep(10)
driver.get(profile_url) 

src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'ph5'})
  

# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()

location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Ectracting the Location
# The 2nd element in the location_loc variable has the location
location = location_loc[0].get_text().strip()

print("Name -->", name,
	"\nWorks At -->", works_at)

about = soup.find("div", {"id": "about"}).find_next_sibling("div", {"class", "display-flex ph5 pv3"}).find("div").get_text().strip()

print("About " , about)

driver.get(profile_url+"/details/experience/")
time.sleep(5)
exp_src = driver.page_source
  
# Now using beautiful soup
exp_soup = BeautifulSoup(exp_src, 'lxml')
experience = exp_soup.find_all("li", {"class", "pvs-list__paged-list-item"})

#print(experience)
# In case of an error, try changing the tags used here.

li_tags = experience
print("Length of Experience Nodes ", len(li_tags))
for li_tag in li_tags:
    try:
        job_title = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
        print("Job Title : ", job_title)
        company_name = li_tag.find("span", {"class", "t-normal"}).find("span").get_text().strip()
        print("Company Name : ", company_name)
        joining_date = li_tag.find("span", {"class", "t-black--light"}).find("span").get_text().strip()
        print("Joining Date : ", joining_date)
    except:
        continue

driver.get(profile_url+"/details/education/")
time.sleep(5)
edu_src = driver.page_source
  
# Now using beautiful soup
edu_soup = BeautifulSoup(edu_src, 'lxml')

# In case of an error, try changing the tags used here.

li_tags = edu_soup.find_all("li", {"class", "pvs-list__paged-list-item"})
print("Length of education Nodes ", len(li_tags))
for li_tag in li_tags:
    try:
        institute = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
        print("Institute : ", institute)
        degree = li_tag.find("span", {"class", "t-normal"}).find("span").get_text().strip()
        print("Degree : ", degree)
        duration = li_tag.find("span", {"class", "t-black--light"}).find("span").get_text().strip()
        print("Duration : ", duration)
    except:
        continue

driver.get(profile_url+"/details/skills/")
time.sleep(5)
skills_src = driver.page_source
  
# Now using beautiful soup
skills_soup = BeautifulSoup(skills_src, 'lxml')

# In case of an error, try changing the tags used here.

li_tags = skills_soup.find_all("li", {"class", "pvs-list__paged-list-item"})
print("Length of education Nodes ", len(li_tags))
for li_tag in li_tags:
    try:
        skill = li_tag.find("span", {"class", "t-bold"}).find("span").get_text().strip()
        print("Skill : ", skill)
    except:
        continue

driver.close()