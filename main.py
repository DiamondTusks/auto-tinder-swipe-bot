from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FB_USERNAME = ""
FB_PASSWORD = ""

chrome_driver_path = "/Users/me/Documents/development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.tinder.com/")

time.sleep(2)
# cookie_accept_button = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_accept_button = driver.find_element(By.XPATH, '//*[@id="s1362659109"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_accept_button.click()

time.sleep(2)
# login_button = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button = driver.find_element(By.XPATH, '//*[@id="s1362659109"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(2)
# fb_login_button = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login_button = driver.find_element(By.XPATH, '//*[@id="s-365721967"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login_button.click()

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

time.sleep(2)
fb_username_input = driver.find_element(By.NAME, 'email')
fb_username_input.send_keys(FB_USERNAME)
fb_password_input = driver.find_element(By.NAME, 'pass')
fb_password_input.send_keys(FB_PASSWORD)
fb_password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
# allow_location = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[1]')
allow_location = driver.find_element(By.CLASS_NAME, '.onboarding__modal button')
allow_location.click()

time.sleep(2)
notification_button = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[1]')
notification_button.click()
time.sleep(10)

for _ in range(100):
    like_button = driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
    like_button.send_keys(Keys.ARROW_RIGHT)
    time.sleep(3)


