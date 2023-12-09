from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Taking the checkboxes value to selected in a list
List = ["Cricket", "Movies"]
service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://demo.automationtesting.in")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("123abc")
driver.find_element(By.CSS_SELECTOR, "#enterimg").click()
# All the checkbox elements are taken in checkboxes as a list
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))
# Iterating over the List
for checkbox in checkboxes:
    if checkbox.get_attribute("value") in List:
        checkbox.click()
driver.close()
