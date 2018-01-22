#模拟填写表单
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='phantomjs')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitField = driver.find_element_by_id('submit')

# firstnameField.send_keys('lipy')
# lastnameField.send_keys('sunhl')
# submitField.click()

actions = ActionChains(driver).click(firstnameField).send_keys("lipy").click(lastnameField).send_keys(
    'sunhl').send_keys(Keys.RETURN)
actions.perform()
print(driver.find_element_by_tag_name("body").text)
driver.close()