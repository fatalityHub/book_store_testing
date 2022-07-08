# #### Задание 1
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/") #1
time.sleep(5)
driver.execute_script("window.scrollBy(0,600);") #2
Selenium_Ruby = driver.find_element_by_partial_link_text("Selenium Ruby") #3
Selenium_Ruby.click()
reviews_tab = driver.find_element_by_class_name("reviews_tab") #4
reviews_tab.click()
star5 = driver.find_element_by_class_name("star-5") #5
star5.click()
comment = driver.find_element_by_id("comment") #6
comment.send_keys("Nice book!")
name_field = driver.find_element_by_id("author")
name_field.send_keys("Name")
email_field = driver.find_element_by_id("email")
email_field.send_keys("asd@dsa.com")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()

time.sleep(2)
driver.quit()

