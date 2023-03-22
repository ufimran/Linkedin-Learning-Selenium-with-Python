from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://wiki.python.org/moin/FrontPage")

searchBox = driver.find_element(By.ID, "searchinput")
searchBox.clear()
searchBox.send_keys("Beginner")
searchBox.send_keys(Keys.RETURN)
time.sleep(5)

select = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul/li[5]/form/div/select"))
select.select_by_visible_text("Raw Text")
time.sleep(10)

driver.close()