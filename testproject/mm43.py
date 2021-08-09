from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)
time.sleep(1)

# web elements
email = driver.find_element_by_id('email')
submit_btn = driver.find_element_by_id('submit')

# TC03
submit_btn.click()
alert = driver.find_element_by_xpath('/html/body/div/div/form/div')
assert alert.text == 'Kérjük, töltse ki ezt a mezőt.'
time.sleep(0.5)

# TC02
email.send_keys('teszt@')
assert alert.text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
time.sleep(0.5)
elements1 = driver.find_elements_by_xpath('//div')

# TC01
email.clear()
email.send_keys('teszt@elek.hu')
time.sleep(0.5)
elements2 = driver.find_elements_by_xpath('//div')
assert (len(elements1) - 1) == len(elements2)
# -1 element means there is no validation error
# it was faster to start from TC03

# nálam magyarul jelennek meg a figyelmeztetések
# ha a feladatleírásban megadott angol szöveggel assertálnám akkor természetesen hibát dobna
# de nem hiszem hogy az a feladat lényege

driver.close()
