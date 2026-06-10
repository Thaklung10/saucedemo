#import webdriver
from selenium import webdriver
#Import By for locators
from selenium.webdriver.common.by import By 
# import time module
import time
#module for explicity wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#launch browser
driver=webdriver.Edge()
time.sleep(2)
#For implicit wait = driver.implicity_wait(5)
#driver.implicity_wait(5)
#maximized window
driver.maximize_window()
#visit URL
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)
#find username
username=driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
#find password
password=driver.find_element(By.ID,"password" )
password.send_keys("secret_sauce")
#find login button
wait = WebDriverWait(driver, 10)


#login_button=driver.find_element(By.ID,"login-button")
login_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login-button']")))
#OR login_button = driver.find_element(*(By.XPATH,"//input[@id='login-button']"))
# from extension
login_button.click()
time.sleep(2)
# To use the action of mouse
#actions=ActionChains(driver)
#actions.double_click(login_button).perform()

#assert "inventory" in driver.current_url,"Failed! Login.unsuccessful"

# if "inventory" in driver.current_url:
#     print("Login successful")
# else:
#     print("Login unsucessful")

#To scroll down the screen by pixel
#driver.execute_script("window.scrollBy(0,500);")

#scroll to bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
#scroll bottom to top
#driver.execute_script("window.scrollTo(0,0);")

#Adding items in cart
sauce_labs_onesie=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
sauce_labs_onesie.click()

Tshirt_red=driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
Tshirt_red.click()
time.sleep(2)

#In Cart
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)
cartlogo=driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
cartlogo.click()
time.sleep(2)

#Chceckingout after selecting the item which we are going to purchase
checkout=driver.find_element(By.XPATH,"//*[@id='checkout']")
checkout.click()
time.sleep(2)

# Putting the information
first_name=driver.find_element(By.ID,"first-name")
first_name.send_keys("Bibek")

last_name=driver.find_element(By.ID,"last-name")
last_name.send_keys("Limbu")

postal_code=driver.find_element(By.ID,"postal-code")
postal_code.send_keys("22500")
time.sleep(2)

#Continuting the process
Continue=driver.find_element(By.ID,"continue")
Continue.click()
time.sleep(2)

#scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

#finish the process
finish=driver.find_element(By.ID,"finish")
finish.click()
time.sleep(2)

#To know the process is completed or not
#assert "checkout-complete.html" in driver.current_url,"Failed! Login.unsuccessful"
if "checkout-complete.html" in driver.current_url:
   print("Congratulation! Purchasing item/s is/are successful.")
else:
 print("Sorry! Purchase is unsuccessful.")
#Back to home
backtohome=driver.find_element(By.ID,"back-to-products")
backtohome.click()
time.sleep(2)
#To select the dropdown option
dropdown=Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
dropdown.select_by_value("lohi")
time.sleep(4)

# Logging out from the website
menu=driver.find_element(By.ID,"react-burger-menu-btn")
menu.click()
time.sleep(2)

logout=driver.find_element(By.ID,"logout_sidebar_link")
logout.click()
time.sleep(2)

assert "saucedemo" in driver.current_url,"Failed! Logout.Unsuccessful"
driver.quit()


