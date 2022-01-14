from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.set_page_load_timeout("5")
driver.get("https://www.google.com/")
driver.maximize_window()
f = driver.find_element_by_name("q")
f.send_keys("sony india")
time.sleep(10)
f.send_keys(Keys.RETURN)
