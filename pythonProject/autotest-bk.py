#載入需要的套件
import os
import string
import time
import uuid
from datetime import datetime
from random import random

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()
driver.implicitly_wait(50)


# 截圖設定
# screenshot_dir = "screenshots"  # 指定資料夾名稱
# os.makedirs(screenshot_dir, exist_ok=True)  # 建立資料夾（如果不存在）
# # # 獲取當前時間
# # current_time = datetime.now().strftime("%Y%m%d%H%M%S")
# current_time = time.time()
# #

# 創建截圖儲存資料夾（如果不存在）
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)


# 定義截圖函式
def take_screenshot(step):
    # 生成亂數字串
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # 生成檔名
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_filename = f"screenshot_{step}_{timestamp}_{random_string}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)






# 自行設定視窗的寬與高
driver.set_window_size(430, 932)
# 印出瀏覽器視窗的大小，單位為像素
print ("視窗的寬為：" + str(driver.get_window_size().get("width")))
print ("視窗的高為：" + str(driver.get_window_size().get("height")))

driver.get("https://www.cathaybk.com.tw/cathaybk/")
time.sleep(2)
# 執行截圖
# screenshot_path = "custom_screenshot1.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# 執行截圖
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
# 執行截圖
driver.save_screenshot(screenshot_path)

# screenshot_path = "credit_card.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)

# 計算信用卡選單步驟
# 等待信用卡項目元素出現
credit_card_items = WebDriverWait(driver, 10).until(visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div")))

# 計算信用卡項目數量
num_of_credit_cards = len(driver.find_elements(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div"))

# 輸出結果
print(f"信用卡列表中有 {num_of_credit_cards} 個項目")
time.sleep(2)


#信用卡介紹
Card_introduction = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]")
Card_introduction.click()
time.sleep(2)


#停卡選單
Stop_Card1 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[1]")
Stop_Card1 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot2.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# 執行截圖
driver.save_screenshot(screenshot_path)


Stop_Card2 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[2]")
Stop_Card2 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot3.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card3 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[3]")
Stop_Card3 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot4.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card4 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[4]")
Stop_Card4 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot5.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card5 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[5]")
Stop_Card5 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot6.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card6 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[6]")
Stop_Card6 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot7.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card7 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[7]")
Stop_Card7 .click()
time.sleep(5)
# 執行截圖
# screenshot_path = "custom_screenshot8.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card8 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[8]")
Stop_Card8 .click()
time.sleep(5)
# screenshot_path = "custom_screenshot9.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card9 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[9]")
Stop_Card9 .click()
time.sleep(5)
# screenshot_path = "custom_screenshot10.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card10 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[10]")
Stop_Card10 .click()
time.sleep(5)
# screenshot_path = "custom_screenshot11.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)



Stop_Card11 = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[11]")
Stop_Card11 .click()
time.sleep(5)
# screenshot_path = "custom_screenshot12.png"  # 指定檔名
# driver.save_screenshot(screenshot_path)
# # 執行截圖
# driver.save_screenshot(screenshot_path)






# 找到指定 <div> 元素下的子元素
echild_elements = len(driver.find_elements(By.XPATH,("/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span")))

# # 計算子元素數量
# num_child_elements = len(echild_elements)

# 輸出結果
print(f"指定 <div> 元素下有 {echild_elements} 個子元素")