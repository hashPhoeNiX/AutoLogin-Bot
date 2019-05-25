from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

usr = 'yourUsername or email'
pwd = 'yourPassword'

chrome_path = 'path/to/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_path)
browser.get(('https://www.facebook.com/'))

# filling and submitting log in details
username = browser.find_element_by_id('email')
username.send_keys(usr)
password = browser.find_element_by_id('pass')
password.send_keys(pwd)
loginButton = browser.find_element_by_id('u_0_2')
loginButton.click()


# # if there is transition between pages e.g. gmail log in
# pwd = WebDriverWait(browser, 10).until(
#     ec.presence_of_element_located('passwd')
# )
# pwd.send_keys(log_details['pass'][0])

# signInButton = browser.find_element_by_id('signIn')
# signInButton.click()