from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://demo.automationtesting.in")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("123abc")
driver.find_element(By.CSS_SELECTOR, "#enterimg").click()
dropdown = driver.find_element(By.CSS_SELECTOR, "#Skills")
sel = Select(dropdown)
sel.select_by_value("Certifications")
driver.close()