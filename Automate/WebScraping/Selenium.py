from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://google.com")
elem = browser.find_element_by_css_selector("p")
elem.send_keys("hello")
elem.submit()
