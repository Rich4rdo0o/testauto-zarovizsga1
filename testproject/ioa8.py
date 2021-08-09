from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)
time.sleep(1)

# web elements
num1 = driver.find_element_by_id('num1')
operand = driver.find_element_by_id('op')
num2 = driver.find_element_by_id('num2')
submit = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')


# TC01 checking results with all operands
def calculator():
    submit.click()
    if operand.text == '+':
        assert int(result.text) == (int(num1.text) + int(num2.text))
    elif operand.text == '-':
        assert int(result.text) == (int(num1.text) - int(num2.text))
    elif operand.text == '*':
        assert int(result.text) == (int(num1.text) * int(num2.text))
    # elif operand.text == '/':
    #     assert int(result.text) == (int(num1.text) / int(num2.text))
    # have not seen it dividing and not sure how would it work if the result is FLOAT


calculator()

# checking results to be sure
# print(result.text)
# print(int(num1.text) + int(num2.text))
# print(int(num1.text) - int(num2.text))
# print(int(num1.text) * int(num2.text))
# print(int(num1.text) / int(num2.text))

driver.close()
