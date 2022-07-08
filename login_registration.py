######## Задание 2

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
my_acc = driver.find_element_by_partial_link_text("My Account")
my_acc.click()
time.sleep(5)
reg_mail = driver.find_element_by_id("reg_email")
reg_mail.send_keys("asd122345@asdmail.com")
reg_pass = driver.find_element_by_id("reg_password")
reg_pass.send_keys("!@#12345asdM!!")
time.sleep(5)
register_btn = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row>.woocommerce-Button.button")
register_btn.click()

time.sleep(2)
driver.quit()


# задание 3

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
my_acc = driver.find_element_by_partial_link_text("My Account")
my_acc.click()
time.sleep(5)
login_mail = driver.find_element_by_id("username")
login_mail.send_keys("asd122345@asdmail.com")
login_pass = driver.find_element_by_id("password")
login_pass.send_keys("!@#12345asdM!!")
time.sleep(2)
login_btn = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button.button")
login_btn.click()
logout_elem = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"),"Logout"))

time.sleep(2)
driver.quit()