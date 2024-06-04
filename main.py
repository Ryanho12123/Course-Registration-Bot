import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
# from datetime import datetime
# import pause


import time

def WelcomeBanner():
    print("==========================================================================================")
    print("|                        Ryan Ho's Course Registration Bot                                 |")
    print("==========================================================================================")



def getDriver():
    print("\nInitializing/Checking webdriver....\n")
    # Initializes necessary Chrome driver for Selenium to use:
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.maximize_window
    driver.close()

def UTRegister():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.maximize_window

    driver = webdriver.Chrome()
    
    print("\nRegistering for courses...\n")
    # UT's Login Page
    loginURL = "https://utdirect.utexas.edu/registration/chooseSemester.WBX"
    driver.get(loginURL)

    utUsername = driver.find_element(By.ID, "username")
    utUsername.send_keys(EID)
    eidPassword = driver.find_element(By.ID, "password")
    eidPassword.send_keys(uTPassword + Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="regContent"]/div/form/input[5]'))
    )

    semesterButton = driver.find_element(By.XPATH, '//*[@id="regContent"]/div/form/input[5]')
    semesterButton.click()

    for i in range (len(courses)):
        uniqueNumber = driver.find_element(By.XPATH, '//*[@id="s_unique_add"]')
        uniqueNumber.send_keys(courses[i] + Keys.ENTER)
    
    time.sleep(10)

    driver.quit()


def main():
    WelcomeBanner()
    getDriver()
    global courses, EID, uTPassword, semester, num_of_courses

    print("\nPlease enter the necessary information to register...\n")
    # Defining a courses list that will store user-inputed CRN numbers:
    courses = []
    # Getting user-inputed data that will be inserted into the site pages:
    EID = input("What is your EID?: ").upper()[:9]
    uTPassword = getpass("What is your password?: ")
    semester = input("What semester are you applying for? (EXACTLY AS STATED ON UIS): ")
    num_of_courses = int(input("How many courses are you going to take?: "))
    print(f"You are taking {num_of_courses} courses")
    for idx in range(num_of_courses):
        CRN = input('Enter the Unique number of each course: ')
        courses.append(CRN)
    print("\nYou are taking these courses\n" + str(courses) + "\n")

    UTRegister()

if __name__ == '__main__':
    main()





# registerButton = driver.find_element(By.XPATH, '//*[@id="primary"]/p[2]/a')
# registerButton.click()



# time.sleep(10)

# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://google.com")

# <input class="field input" id="username" name="j_username" type="text" value="" autocomplete="off" size="30" aria-required="true" aria-label="UT EID" autofocus="autofocus" placeholder="UT EID">

