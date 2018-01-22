#单元测试
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='phantomjs')
driver.get('https://en.wikipedia.org/wiki/Monty_Python')
assert "Monty Python" in driver.title
driver.close()
