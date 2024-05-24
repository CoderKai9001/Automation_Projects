from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


driver.get("https://orteil.dashnet.org/cookieclicker")

languageID = "langSelect-EN"
big_cookieID = "bigCookie"
cookie_countID = "cookies"
cursorUpgradeID = "product0"
cursorUpgradePriceID = "productPrice0"
grandmaUpgradeID = "product1"
grandmaUpgradePriceID = "productPrice1"
farmUpgradeID = "product2"
farmUpgradePriceID = "productPrice2"
mineUpgradeID = "product3"
mineUpgradePriceID = "productPrice3"
factoryUpgradeID = "product4"
factoryUpgradePriceID = "productPrice4"

def buyCursor(cursorUpgradeID, cursorUpgradePriceID, cookie_count):
    cursor_price = driver.find_element(By.ID, cursorUpgradePriceID).text
    cursor_price = cursor_price.replace(',', '')
    cursor_price = int(cursor_price)
    if cookie_count >= cursor_price:
        cursorUpgradeButton = driver.find_element(By.ID, cursorUpgradeID)
        cursorUpgradeButton.click()

def buyGrandma(grandmaUpgradeID, grandmaUpgradePriceID, cookie_count):
    grandma_price = driver.find_element(By.ID, grandmaUpgradePriceID).text
    grandma_price = grandma_price.replace(',', '')
    grandma_price = int(grandma_price)
    if cookie_count >= grandma_price:
        grandma = driver.find_element(By.ID, grandmaUpgradeID)
        grandma.click()

def buyFarm(farmUpgradeID, farmUpgradePriceID, cookie_count):
    farm_price = driver.find_element(By.ID, farmUpgradePriceID).text
    if farm_price != '':
        farm_price = farm_price.replace(',', '')
        farm_price = int(farm_price)
        if cookie_count >= farm_price:
            farmUpgradeButton = driver.find_element(By.ID, farmUpgradeID)
            farmUpgradeButton.click()

def buyMine(farmUpgradeID, farmUpgradePriceID, cookie_count):
    mine_price = driver.find_element(By.ID, mineUpgradePriceID).text
    if mine_price != '':
        mine_price = mine_price.replace(',', '')
        mine_price = int(mine_price)
        if cookie_count >= mine_price:
            mineUpgradeButton = driver.find_element(By.ID, mineUpgradeID)
            mineUpgradeButton.click()

def buyFactory(factoryUpgradeID, factoryUpgradePriceId, cookie_count):
    factory_price = driver.find_element(By.ID, factoryUpgradePriceID).text
    if factory_price != '':
        factory_price = factory_price.replace(',', '')
        factory_price = int(factory_price)
        if cookie_count >= factory_price:
            cursorUpgradeButton = driver.find_element(By.ID, factoryUpgradeID)
            cursorUpgradeButton.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, languageID))
)

languageElement = driver.find_element(By.ID, languageID)
languageElement.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, big_cookieID))
)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_countID))
)

cookie = driver.find_element(By.ID, big_cookieID)

while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_countID).text.split(" ")[0]
    cookie_count = cookie_count.replace(',', '')
    cookie_count = int(cookie_count)

    buyCursor(cursorUpgradeID, cursorUpgradePriceID, cookie_count)
    buyGrandma(grandmaUpgradeID, grandmaUpgradePriceID, cookie_count)
    buyFarm(farmUpgradeID, farmUpgradePriceID, cookie_count)
    buyMine(mineUpgradeID, mineUpgradePriceID, cookie_count)
    buyFactory(factoryUpgradeID, factoryUpgradePriceID, cookie_count)
