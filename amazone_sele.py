from selenium import webdriver
# from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')
driver.get('https://www.amazon.in/')
driver.maximize_window()
input_search=driver.find_element(By.ID,"twotabsearchtextbox")
search_button=driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
input_search.send_keys('smart phone under 15000')
# sleep(5)
search_button.click()
pro=driver.find_elements(By.XPATH,'//div[@class="sg-col-inner"]')
for i in pro:
    name=pro.find_element(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]').text
    print(name)