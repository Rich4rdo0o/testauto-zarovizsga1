from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)
time.sleep(1)

# web elements
side_a = driver.find_element_by_id('a')
side_b = driver.find_element_by_id('b')
submit_btn = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')


# method to not repeat
def square(a, b, c):
    side_a.send_keys(a)
    side_b.send_keys(b)
    submit_btn.click()
    time.sleep(0.5)
    assert result.text == c
    time.sleep(0.5)
    side_a.clear()
    side_b.clear()


# TC01 correct data
square('99', '12', '222')

# TC02 incorrect data
square('kiskutya', '12', 'NaN')

# TC03 empty data
submit_btn.click()
assert result.text == 'NaN'

driver.close()
