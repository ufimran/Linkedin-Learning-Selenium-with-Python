from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

# element_id = driver.find_element(By.ID, "gsc-iw-id1")
# print(element_id)

element_name = driver.find_element(By.NAME, "submit")
print(element_name)

element_xpath = driver.find_element(By.XPATH, "//h1[@class='display-1']")
print(element_xpath)

# element_classname = driver.find_element(By.CLASS_NAME, "selenium-backers")
# print(element_classname)

driver.close()