from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)
time.sleep(1)

# clicking 100x
submit_btn = driver.find_element_by_id('submit')

for _ in range(100):
    submit_btn.click()

# collecting the results
results = driver.find_elements_by_xpath('//li')
# print(len(results))

# putting the head results in another list
head = []
for i in results:
    if i.text == "fej":
        head.append(i)

# checking the number of heads
assert len(head) >= 30
# print(len(head))

driver.close()
