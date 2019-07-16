import os
from selenium import webdriver
import pyautogui


print(pyautogui.displayMousePosition())
'''chromedriver = "C:\\Users\\Sanket\\Desktop\\Python Practice\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https:google.com")

ele = driver.find_element_by_css_selector('#gbw > div > div > div.gb_Zd.gb_f.gb_7f.gb_Xf > div:nth-child(1) > a')
print(ele)
print(ele.text)
ele.click()
driver.quit()
'''
