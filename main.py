import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=4127605218&f_LF=f_AL&geoId=105374601&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

#Click the X from the Pop-up
try:
    x_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/button')
    x_button.click()
except Exception as e:
    print("Element not found:", e)

#Click the Sign-in button
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()
time.sleep(1.5)

#Search for the places for credentials and sign-in button
user = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
let_sign_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')

#Insert the values
user.send_keys(EMAIL, Keys.TAB)
password.send_keys(PASSWORD)
let_sign_in.click()
time.sleep(10)

job_bar = driver.find_elements(By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/ul')
for job in job_bar:
    print(job.id)
#Search for the button Save and Follow
#save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
#follow_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/section/section/div[1]/div[1]/button')

#Click the buttons
#save_button.click()
#driver.execute_script("arguments[0].scrollIntoView();", follow_button)
#time.sleep(1)
#follow_button.click()

#driver.quit()
