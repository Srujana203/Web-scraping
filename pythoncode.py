from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

driver = webdriver.Chrome()

names_list = pd.read_csv('names.csv')
names_sc = []

for name in names_list:
    driver.get('https://www.nsopw.gov/')
    driver.maximize_window()
    time.sleep(3)
    firstname_field = driver.find_element(By.NAME,"firstname")
    lastname_field = driver.find_element(By.NAME,"lastname")

    firstname = name.split(' ')[0]
    lastname = name.split(' ')[-1]
    firstname_field.clear()
    firstname_field.send_keys(firstname)
    lastname_field.clear()
    lastname_field.send_keys(lastname)

    submit_button = driver.find_element(By.ID,'searchbyname')
    submit_button.click()

    time.sleep(5)

    try:
        driver.find_element(By.ID,'confirmbtn').click()
        print('after click')
    except NoSuchElementException:
        pass

    elements = driver.find_elements(By.CLASS_NAME,"dataTables_empty")

    if elements:
        continue
    else:
        names_sc.append(name)

print(names_sc)

driver.quit()