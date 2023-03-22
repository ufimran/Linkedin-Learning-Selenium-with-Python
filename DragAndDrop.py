from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://jqueryui.com/droppable")
driver.switch_to.frame(0)

action_chains = ActionChains(driver)

source = driver.find_element(By.XPATH, "/html/body/div[1]")
target = driver.find_element(By.XPATH, "/html/body/div[2]")


action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(3)
action_chains.drag_and_drop(source, target).perform()
time.sleep(3)

driver.close()