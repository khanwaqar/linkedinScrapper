from re import I
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com")
search_bar = driver.find_element("name", "search_query")
search_bar.clear()
search_bar.send_keys("Mirza Raheel chess")
search_bar.send_keys(Keys.RETURN)
time.sleep(10)
search_bar1 = driver.find_element("id", "main-link")
search_bar1.click()
time.sleep(10)
search_bar2 = driver.find_element("href", "playlists")
search_bar2.click()

