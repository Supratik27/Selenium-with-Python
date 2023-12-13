from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.implicitly_wait(2)
driver.maximize_window()
driver.switch_to.frame("singleframe")
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("1234567789")
# Back to main page
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()
driver.close()