from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions 

import time

# ------ 登入的帳號與密碼 ------
username = 'xxxxxxxxxx'
password = 'xxxxxxxxxx'

username = input('輸入臉書帳號\n') or username
password = input('輸入臉書密碼\n') or password

# ------ 輸入想要推推的貼文網址 ------ 
spec_url = 'xxxxxxxxxx'
spec_url = input('輸入想要推推的貼文\n') or spec_url


# ------ 設定要前往的網址 ------
url = 'https://www.facebook.com'  

# ------ 透過Browser Driver 開啟 Chrome ------
driver = webdriver.Edge()        

# ------ 前往該網址 ------
driver.get(url)   


# ------ 輸入賬號密碼 ------
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element_by_id("email")
elem.send_keys(username)

elem = driver.find_element_by_id("pass")
elem.send_keys(password)        

elem.send_keys(Keys.RETURN)
time.sleep(5)


#------ 檢查有沒有被擋下來 ------
if len(driver.find_elements_by_xpath("//*[contains(text(), '你的帳號暫時被鎖住')]")) > 0:
    driver.find_elements_by_xpath("//*[contains(text(), '是')]")[1].click()

#------ 切換頁面 ------
driver.get(spec_url)


#------ 在留言欄輸入「推推」------
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='oo9gr5id lzcic4wl jm1wdb64 l9j0dhe7 gsox5hk5 mdldhsdk ii04i59q notranslate']")))
e = driver.find_element_by_css_selector("div[class='oo9gr5id lzcic4wl jm1wdb64 l9j0dhe7 gsox5hk5 mdldhsdk ii04i59q notranslate']")

while(1):

    try:

        e.send_keys('推推')
        e.send_keys(Keys.RETURN)


    except exceptions.StaleElementReferenceException as msg:

        e = driver.find_element_by_css_selector("div[class='oo9gr5id lzcic4wl jm1wdb64 l9j0dhe7 gsox5hk5 mdldhsdk ii04i59q notranslate']")
        e.send_keys('推推')
        e.send_keys(Keys.RETURN)

    time.sleep(3600) 

e.clear()
