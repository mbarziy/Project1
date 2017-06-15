from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.facebook.com/'
browser = webdriver.Chrome()
browser.get(URL)

assert 'Facebook' in browser.title

email_input = browser.find_element_by_css_selector('input#email')
password_input = browser.find_element_by_xpath('//input[@name="pass"]')
login_button = browser.find_element(By.CSS_SELECTOR,'input[type=submit]')

#inputs = browser.find_elements_by_css_selector('input')
#for input in inputs:
#    input.clear()

email_input.send_keys('denis.zvezdov')
password_input.send_keys('wrong password')
login_button.click()

assert 'Log into Facebook' in browser.title

#browser.quit()