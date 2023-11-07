from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("www.google.com")