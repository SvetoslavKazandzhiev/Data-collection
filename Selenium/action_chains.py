from logging.config import valid_ident
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker')

driver.implicitly_wait(5)

cookie = driver.find_element(by=By.ID, value="bigCookie")
select_language = driver.find_element(by=By.ID, value="langSelect-EN")
cookie_count = driver.find_element(by=By.ID, value="cookies")
correct_values = ("id", ("productPrice" + str(i)) for i in range(1,-1,-1))
items = [driver.find_element(by=By.ID, value="correct_values")]

actions = ActionChains(driver)
actions.click(select_language)
actions.click(cookie)

for i in range(1000):
    actions.perform()
    count = int(cookie_count.text)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()