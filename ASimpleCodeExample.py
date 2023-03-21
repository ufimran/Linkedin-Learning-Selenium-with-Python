from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")

driver.maximize_window()
elem = driver.find_element("name", "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()