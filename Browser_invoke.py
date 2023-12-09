from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://pypi.org/")
driver.minimize_window()
driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
driver.set_window_size(500, 500)
print(driver.get_window_size())
print(driver.get_window_position())
print(driver.title)

