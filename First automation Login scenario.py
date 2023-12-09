from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
print(driver.get_window_size())
print(driver.get_window_position())
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
print(driver.title)
driver.close()
driver.quit()
