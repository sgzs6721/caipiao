from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.390uc.com')

# assert 'baidu' in browser.title

elem = browser.find_element_by_name('wd')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()