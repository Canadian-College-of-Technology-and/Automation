from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

# Make a full screen
driver.maximize_window()

# Let's wait for the browser response in general
driver.implicitly_wait(0)

# Navigating to the Moodle app website
driver.get('https://www.google.ca/')

# Checking that we're on the correct URL address and we're seeing correct title
if driver.current_url == 'https://www.google.ca/' and driver.title == 'Google': #Title has to be the same as in the orginal web page (case senitive)
    #i.e google= not working Google == working
    print(f'We\'re at google homepage -- {driver.current_url}')
    print(f'We\'re seeing title message -- "Google"')
    sleep(5)
    driver.close()
else:
    print(f'We\'re not at the google homepage. Check your code!')
    driver.close()
    driver.quit()