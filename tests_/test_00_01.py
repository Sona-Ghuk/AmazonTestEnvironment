import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

login_button = driver.find_element(By.ID, '#nav-link-accountList')
login_button.click()

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("sona.ghukasyan@gmail.com")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

time.sleep(5)

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("hasiko07")

signin_button = driver.find_element(By.ID, "signInSubmit")
signin_button.click()

time.sleep(5)

driver.quit()