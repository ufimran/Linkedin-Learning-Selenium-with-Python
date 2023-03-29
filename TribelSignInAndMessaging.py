from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.tribel.com/")
driver.maximize_window()


driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/a").click()
time.sleep(3.0)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/a").click()
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/div/div/section/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div[1]/input").send_keys("birir19773@syswift.com")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/div/div/section/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/input").send_keys("12345678Ii")
time.sleep(10.0)
# driver.find_element(By.CLASS_NAME, "rc-anchor-center-item rc-anchor-checkbox-holder").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/div/div/section/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/input").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div/div[3]/section/div/div/div/div[2]/div/div[2]/div/div[1]/input").send_keys("Oscar")
time.sleep(5)



# day = Select(driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]"))
# day.select_by_visible_text("12")
# time.sleep(1.0)
# month = Select(driver.find_element(By.NAME, "birthday_month"))
# month.select_by_visible_text("Jan")
# time.sleep(1.0)
# year = Select(driver.find_element(By.NAME, "birthday_year"))
# year.select_by_visible_text("1999")
#
# time.sleep(1.0)
# driver.find_element(By.XPATH, "//label[text()='Male']").click()
#
# time.sleep(1.0)
# driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
#
# time.sleep(10.0)
#
# act_title = driver.title
# exp_title = "Facebook-log in or sign up"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")


time.sleep(20.0)
driver.close()
