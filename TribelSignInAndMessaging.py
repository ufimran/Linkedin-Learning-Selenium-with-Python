from selenium import webdriver
from selenium.webdriver.common.by import By
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
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/div/div/section/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/input").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/textarea").send_keys("Hi")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div").click()
time.sleep(10.0)

driver.close()
