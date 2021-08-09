from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)
time.sleep(1)

# web elements
missing_city = driver.find_element_by_id('missingCity')
verify = driver.find_element_by_id('submit')
cities1 = driver.find_element_by_id('cites')
cities2 = driver.find_elements_by_xpath('//li')

# automatizálás elveit nézve rettenetes megoldás, de legalább megtalálja a várost
# gondolom listába kellene tenni a városokat, manipulálni a listákat és összehasonlítani
# de ez jelenleg meghaladja a képességeimet, viszont maradt rengeteg idő ezért gépeltem egy millió sort,
# nem tudom ez + vagy inkább - pontot ér :D

montgomery = driver.find_elements_by_xpath("//*[contains(text(), 'Montgomery')]")
assert (len(montgomery)) == 3
juneau = driver.find_elements_by_xpath("//*[contains(text(), 'Juneau')]")
assert (len(juneau)) == 3
phoenix = driver.find_elements_by_xpath("//*[contains(text(), 'Phoenix')]")
assert (len(phoenix)) == 3
little_rock = driver.find_elements_by_xpath("//*[contains(text(), 'Little Rock')]")
assert (len(little_rock)) == 3
sacramento = driver.find_elements_by_xpath("//*[contains(text(), 'Sacramento')]")
assert (len(sacramento)) == 3
denver = driver.find_elements_by_xpath("//*[contains(text(), 'Denver')]")
assert (len(denver)) == 3
hartford = driver.find_elements_by_xpath("//*[contains(text(), 'Hartford')]")
assert (len(hartford)) == 3
dover = driver.find_elements_by_xpath("//*[contains(text(), 'Dover')]")
assert (len(dover)) == 3
tallahassee = driver.find_elements_by_xpath("//*[contains(text(), 'Tallahassee')]")
assert (len(tallahassee)) == 3
atlanta = driver.find_elements_by_xpath("//*[contains(text(), 'Atlanta')]")
assert (len(atlanta)) == 3
honolulu = driver.find_elements_by_xpath("//*[contains(text(), 'Honolulu')]")
assert (len(honolulu)) == 3
boise = driver.find_elements_by_xpath("//*[contains(text(), 'Boise')]")
assert (len(boise)) == 3
springfield = driver.find_elements_by_xpath("//*[contains(text(), 'Springfield')]")
assert (len(springfield)) == 3
indianapolis = driver.find_elements_by_xpath("//*[contains(text(), 'Indianapolis')]")
assert (len(indianapolis)) == 3
des_moines = driver.find_elements_by_xpath("//*[contains(text(), 'Des Moines')]")
assert (len(des_moines)) == 3
topeka = driver.find_elements_by_xpath("//*[contains(text(), 'Topeka')]")
assert (len(topeka)) == 3
frankfort = driver.find_elements_by_xpath("//*[contains(text(), 'Frankfort')]")
assert (len(frankfort)) == 3
baton_rouge = driver.find_elements_by_xpath("//*[contains(text(), 'Baton Rouge')]")
assert (len(baton_rouge)) == 3
augusta = driver.find_elements_by_xpath("//*[contains(text(), 'Augusta')]")
assert (len(augusta)) == 3
annapolis = driver.find_elements_by_xpath("//*[contains(text(), 'Annapolis')]")
assert (len(annapolis)) == 3
boston = driver.find_elements_by_xpath("//*[contains(text(), 'Boston')]")
assert (len(boston)) == 3
lansing = driver.find_elements_by_xpath("//*[contains(text(), 'Lansing')]")
assert (len(lansing)) == 3
saint_paul = driver.find_elements_by_xpath("//*[contains(text(), 'Saint Paul')]")
assert (len(saint_paul)) == 3
jackson = driver.find_elements_by_xpath("//*[contains(text(), 'Jackson')]")
assert (len(jackson)) == 3
jefferson_city = driver.find_elements_by_xpath("//*[contains(text(), 'Jefferson City')]")
assert (len(jefferson_city)) == 3
helena = driver.find_elements_by_xpath("//*[contains(text(), 'Helena')]")
assert (len(helena)) == 3
lincoln = driver.find_elements_by_xpath("//*[contains(text(), 'Lincoln')]")
assert (len(lincoln)) == 3
carson_city = driver.find_elements_by_xpath("//*[contains(text(), 'Carson City')]")
assert (len(carson_city)) == 3
concord = driver.find_elements_by_xpath("//*[contains(text(), 'Concord')]")
assert (len(concord)) == 3
trenton = driver.find_elements_by_xpath("//*[contains(text(), 'Trenton')]")
assert (len(trenton)) == 3
santa_fe = driver.find_elements_by_xpath("//*[contains(text(), 'Santa Fe')]")
assert (len(santa_fe)) == 3
albany = driver.find_elements_by_xpath("//*[contains(text(), 'Albany')]")
assert (len(albany)) == 3
raleigh = driver.find_elements_by_xpath("//*[contains(text(), 'Raleigh')]")
assert (len(raleigh)) == 3
bismarck = driver.find_elements_by_xpath("//*[contains(text(), 'Bismarck')]")
assert (len(bismarck)) == 3
columbus = driver.find_elements_by_xpath("//*[contains(text(), 'Columbus')]")
assert (len(columbus)) == 3
oklahoma_city = driver.find_elements_by_xpath("//*[contains(text(), 'Oklahoma City')]")
assert (len(oklahoma_city)) == 3
salem = driver.find_elements_by_xpath("//*[contains(text(), 'Salem')]")
assert (len(salem)) == 3
harrisburg = driver.find_elements_by_xpath("//*[contains(text(), 'Harrisburg')]")
assert (len(harrisburg)) == 3
providence = driver.find_elements_by_xpath("//*[contains(text(), 'Providence')]")
assert (len(providence)) == 3
columbia = driver.find_elements_by_xpath("//*[contains(text(), 'Columbia')]")
assert (len(columbia)) == 3
pierre = driver.find_elements_by_xpath("//*[contains(text(), 'Pierre')]")
assert (len(pierre)) == 3
nashville = driver.find_elements_by_xpath("//*[contains(text(), 'Nashville')]")
assert (len(nashville)) == 3
austin = driver.find_elements_by_xpath("//*[contains(text(), 'Austin')]")
assert (len(austin)) == 3
salt_lake_city = driver.find_elements_by_xpath("//*[contains(text(), 'Salt Lake City')]")
assert (len(salt_lake_city)) == 3
montpelier = driver.find_elements_by_xpath("//*[contains(text(), 'Montpelier')]")
assert (len(montpelier)) == 3
richmond = driver.find_elements_by_xpath("//*[contains(text(), 'Richmond')]")
assert (len(richmond)) == 3
olympia = driver.find_elements_by_xpath("//*[contains(text(), 'Olympia')]")
assert (len(olympia)) == 3
charleston = driver.find_elements_by_xpath("//*[contains(text(), 'Charleston')]")
assert (len(charleston)) == 3
madison = driver.find_elements_by_xpath("//*[contains(text(), 'Madison')]")
assert (len(madison)) == 3
cheyenne = driver.find_elements_by_xpath("//*[contains(text(), 'Cheyenne')]")
assert (len(cheyenne)) == 3

# assertionerrort exceptionnel kellene kezelni és amelyik városnál dobja azt betenni sendkeysbe

# missing_city.send_keys('')
# verify.click()

driver.close()
