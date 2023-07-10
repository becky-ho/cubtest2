#載入需要的套件
import os
import time
import uuid
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(50)

# 自行設定視窗的寬與高
driver.set_window_size(430, 932)
# 印出瀏覽器視窗的大小，單位為像素
print ("視窗的寬為：" + str(driver.get_window_size().get("width")))
print ("視窗的高為：" + str(driver.get_window_size().get("height")))

driver.get("https://www.cathaybk.com.tw/cathaybk/")
time.sleep(2)
# 執行截圖(1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。)
screenshot_path = "cathaybk.png"  # 指定檔名
driver.save_screenshot(screenshot_path)
time.sleep(5)

#選單
menu = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/a")
menu.click()
time.sleep(2)

#我的產品
product = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div")
product.click()
time.sleep(3)

#信用卡列表
credit_card = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div")
credit_card.click()
time.sleep(5)
# 執行截圖(1. 進入信用卡列表選單後截圖)
screenshot_path = "credit_card.png"  # 指定檔名
driver.save_screenshot(screenshot_path)

# 計算信用卡選單(2.計算有幾項目在信用卡選單下面)
credit_card_items = len(driver.find_elements(By.XPATH,("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")))
# 輸出結果
print(f"信用卡列表中有 {credit_card_items} 個項目")
time.sleep(2)



#信用卡介紹
Card_introduction = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]")
Card_introduction.click()
time.sleep(2)


#停卡選單(1. 進入信用卡列表選單後計算(停發)信用卡數量並截圖)
Stop_Card1 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[1]")
Stop_Card1 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot1.png"  # 指定檔名
driver.save_screenshot(screenshot_path)


Stop_Card2 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[2]")
Stop_Card2 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot2.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card3 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[3]")
Stop_Card3 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot3.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card4 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[4]")
Stop_Card4 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot4.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card5 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[5]")
Stop_Card5 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot5.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card6 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[6]")
Stop_Card6 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot6.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card7 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[7]")
Stop_Card7 .click()
time.sleep(5)
# 執行截圖
screenshot_path = "custom_screenshot7.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card8 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[8]")
Stop_Card8 .click()
time.sleep(5)
screenshot_path = "custom_screenshot8.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card9 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[9]")
Stop_Card9 .click()
time.sleep(5)
screenshot_path = "custom_screenshot9.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card10 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[10]")
Stop_Card10 .click()
time.sleep(5)
screenshot_path = "custom_screenshot10.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



Stop_Card11 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[11]")
Stop_Card11 .click()
time.sleep(5)
screenshot_path = "custom_screenshot11.png"  # 指定檔名
driver.save_screenshot(screenshot_path)



# 計算停卡數量(2. 比對計算(停發)信用卡數量與截圖數量相同)
echild_elements = len(driver.find_elements(By.XPATH,("/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span")))

# 輸出結果
print(f"(停發)信用卡列表中有 {echild_elements} 個項目")
time.sleep(2)


