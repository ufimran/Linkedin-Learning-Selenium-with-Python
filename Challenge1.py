from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

# element_id = driver.find_element(By.ID, "q")
# print(element_id)

# element_name = driver.find_element(By.NAME, "q")
# print(element_name)

heading_xpath =  driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div/div/h1")
print(heading_xpath)

# element_classname= driver.find_element(By.CLASS_NAME, "selenium-sponsors")
# print(element_classname)

driver.close()