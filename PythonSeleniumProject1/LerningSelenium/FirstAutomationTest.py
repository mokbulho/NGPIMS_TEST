from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.get("http://202.161.191.131:30010/login")
driver.maximize_window()
print(driver.title)
time.sleep(5)

driver.delete_all_cookies()
userid = driver.find_element(By.NAME, "email").send_keys("BP7705121323")
password = driver.find_element(By.NAME, "password").send_keys("12345")
element = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-4thj0p']")
element_list = element.text.split(" ")
Total = int(element_list[0])+int(element_list[2])
capchabox = driver.find_element(By.XPATH, "//input[@name='captchaResult']").send_keys(str(Total))
time.sleep(5)

login = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-1tfqlfq']").click()

driver.close()





