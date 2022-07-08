########## Задание 4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(5)
# my_acc = driver.find_element_by_partial_link_text("My Account")
# my_acc.click()
# time.sleep(5)
# login_mail = driver.find_element_by_id("username")
# login_mail.send_keys("asd122345@asdmail.com")
# login_pass = driver.find_element_by_id("password")
# login_pass.send_keys("!@#12345asdM!!")
# time.sleep(2)
# login_btn = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button.button")
# login_btn.click()
#
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(3)
# html_book = driver.find_element_by_partial_link_text("HTML5 Forms")
# html_book.click()
# time.sleep(3)
# name_book = driver.find_element_by_css_selector(".product_title.entry-title")
# name_book_text = name_book.text
# check_text = "HTML5 Forms"
#
# if check_text == name_book_text:
#     print("Test passed")
# else:
#     print("Test failed")
#
#
# time.sleep(2)
# driver.quit()

############# Задание 5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(5)
# my_acc = driver.find_element_by_partial_link_text("My Account")
# my_acc.click()
# time.sleep(3)
# login_mail = driver.find_element_by_id("username")
# login_mail.send_keys("asd122345@asdmail.com")
# login_pass = driver.find_element_by_id("password")
# login_pass.send_keys("!@#12345asdM!!")
# time.sleep(2)
# login_btn = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button.button")
# login_btn.click()
# time.sleep(2)
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(2)
# html_cat = driver.find_element_by_link_text("HTML")
# html_cat.click()
# time.sleep(2)
# item_count = driver.find_elements_by_css_selector(".products.masonry-done>.product")
# print(len(item_count))
# if len(item_count) == 3:
#     print("3 books")
# else:
#     print("false. value is:" +str(len(item_count)))
# time.sleep(3)
# driver.quit()

############# Задание 6
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(5)
# my_acc = driver.find_element_by_partial_link_text("My Account")
# my_acc.click()
# time.sleep(3)
# login_mail = driver.find_element_by_id("username")
# login_mail.send_keys("asd122345@asdmail.com")
# login_pass = driver.find_element_by_id("password")
# login_pass.send_keys("!@#12345asdM!!")
# time.sleep(2)
# login_btn = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button.button")
# login_btn.click()
# time.sleep(2)
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(2)
# default_sort = driver.find_element_by_css_selector("select>[value=menu_order]")
# def_check = WebDriverWait(driver, 10).until(EC.element_to_be_selected(default_sort))
# print(def_check)
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# time.sleep(2)
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# high_to_low = driver.find_element_by_css_selector("select>[value=price-desc]")
# high2 = high_to_low.get_attribute("value")
# assert element_check == high2
# time.sleep(2)
# driver.quit()


####################### задание 7
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(3)
# my_acc = driver.find_element_by_partial_link_text("My Account")
# my_acc.click()
# time.sleep(2)
# login_mail = driver.find_element_by_id("username")
# login_mail.send_keys("asd122345@asdmail.com")
# login_pass = driver.find_element_by_id("password")
# login_pass.send_keys("!@#12345asdM!!")
# time.sleep(2)
# login_btn = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button.button")
# login_btn.click()
# time.sleep(2)
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(2)
# android_book = driver.find_element_by_css_selector(".post-169 h3")
# android_book.click()
# time.sleep(3)
# old_price = "₹600.00"
# new_price = "₹450.00"
# old_price_element = driver.find_element_by_css_selector(".price> del >.woocommerce-Price-amount.amount").text
# new_price_element = driver.find_element_by_css_selector(".price> ins > span").text
# assert old_price_element == old_price
# assert new_price_element == new_price
# book_img = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".images")))
# book_img.click()
# close_cross = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
# close_cross.click()
#
# time.sleep(3)
# driver.quit()

#Задание 8
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(3)
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(2)
# add_basket = driver.find_element_by_css_selector(".post-182 > a.button")
# add_basket.click()
# time.sleep(2)
# cart_items = driver.find_element_by_css_selector(".cartcontents").text
# cart_price = driver.find_element_by_css_selector(".wpmenucart-contents > .amount").text
# assert cart_price == "₹180.00"
# assert cart_items == "1 Item"
# driver.find_element_by_css_selector(".cartcontents").click()
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal>td"),"₹180.00"))
# total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total>td"),""))
#
# time.sleep(3)
# driver.quit()


# Задание 9
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/") #1
# time.sleep(3)
# shop_btn = driver.find_element_by_partial_link_text("Shop")
# shop_btn.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,300);")
# add_basket1 = driver.find_element_by_css_selector(".post-182 > a.button")
# add_basket1.click()
# time.sleep(3)
# add_basket2 = driver.find_element_by_css_selector(".post-180 > a.button")
# add_basket2.click()
# time.sleep(2)
# driver.find_element_by_css_selector(".cartcontents").click()
# time.sleep(2)
# remove_first = driver.find_element_by_css_selector(".cart_item>.product-remove>a:nth-child(1)")
# remove_first.click()
# time.sleep(3)
# undo = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo.click()
# qnty = driver.find_element_by_css_selector(".quantity>input:nth-child(1)")
# qnty.clear()
# qnty.send_keys(3)
# update_basket = driver.find_element_by_css_selector("td.actions>input[value='Update Basket']")
# update_basket.click()
# time.sleep(2)
# qnty = driver.find_element_by_css_selector(".quantity>input:nth-child(1)")
# qnty_check = qnty.get_attribute('value')
# assert qnty_check == "3"
# apply_coupon = driver.find_element_by_css_selector("td.actions>div>input[value='Apply Coupon']")
# apply_coupon.click()
# time.sleep(5)
# error = driver.find_element_by_css_selector(".woocommerce-error").text
# assert error == "Please enter a coupon code."
#
# time.sleep(5)
# driver.quit()

########### Задание 10

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/") #1
time.sleep(3)
shop_btn = driver.find_element_by_partial_link_text("Shop")
shop_btn.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,300);")
add_basket1 = driver.find_element_by_css_selector(".post-182 > a.button")
add_basket1.click()
time.sleep(3)
driver.find_element_by_css_selector(".cartcontents").click()
time.sleep(3)
checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button")))
checkout_btn.click()
first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#billing_first_name")))
first_name.send_keys("Ivan")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Petrov")
email = driver.find_element_by_id("billing_email")
email.send_keys("asdads@asd.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("12345678890")
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("askdjakldjaldjlk asdasd")
town = driver.find_element_by_id("billing_city")
town.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Moscow")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("100000")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)
check_pay = driver.find_element_by_css_selector("[value='cheque']")
check_pay.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
received = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
pay_method = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"tfoot>tr:nth-child(3)>td"),"Check Payments"))
time.sleep(5)
driver.quit()