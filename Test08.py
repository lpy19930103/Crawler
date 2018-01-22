#解析js
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path='phantomjs')
driver.get("https://www.jianshu.com/search?q=python%E7%88%AC%E8%99%AB&page=1")
try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'note-list')))
finally:
    print(driver.find_element_by_class_name('content').text)
    driver.close()
