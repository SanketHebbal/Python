from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
username = input("Enter username ->")
password = input("Enter password ->")

eleUser = driver.find_element_by_xpath('//*[@id="email"]')
eleUser.send_keys(username)

elePass = driver.find_element_by_xpath('//*[@id="pass"]')
elePass.send_keys(password)

elePass.submit()
