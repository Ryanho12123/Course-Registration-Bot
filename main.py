import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://utdirect.utexas.edu/registration/chooseSemester.WBX")

input_element = driver.find_element(By.ID, "username")
input_element.send_keys("rdh2837")
password = driver.find_element(By.ID, "password")
password.send_keys("duh1232004#12" + Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="regContent"]/div/form/input[5]'))
)

button = driver.find_element(By.XPATH, '//*[@id="regContent"]/div/form/input[5]')
button.click()

uniqueNumber = driver.find_element(By.XPATH, '//*[@id="s_unique_add"]')
uniqueNumber.send_keys("84715" + Keys.ENTER)






# registerButton = driver.find_element(By.XPATH, '//*[@id="primary"]/p[2]/a')
# registerButton.click()



time.sleep(10)

driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://google.com")

# <input class="field input" id="username" name="j_username" type="text" value="" autocomplete="off" size="30" aria-required="true" aria-label="UT EID" autofocus="autofocus" placeholder="UT EID">

