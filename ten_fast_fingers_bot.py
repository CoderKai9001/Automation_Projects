from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#define driver
driver = webdriver.Chrome()

driver.get("https://10fastfingers.com/")
# defining tag attributes beforehand for simplicity's sake
TnCAllowID = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
typingTestCLASS = "list-group-item "
inputBoxID = "inputfield"
highlightedWordCLASS = "highlight"

# setup for starting test
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, TnCAllowID))
)

TnCAllowButton = driver.find_element(By.ID, TnCAllowID)
TnCAllowButton.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, typingTestCLASS))
)

typingTestButton = driver.find_element(By.CLASS_NAME, typingTestCLASS)
typingTestButton.click()
# setup end

#locate input text area
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, inputBoxID))
)
inputBox = driver.find_element(By.ID, inputBoxID)

count = 0
while True:
    #break condition as 10FastFingers only loads a maximum of 388 words
    if count == 386:
        break
    #wait for tag to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, highlightedWordCLASS))
    )
    #locate highlighted word
    currentWord = driver.find_element(By.CLASS_NAME, highlightedWordCLASS).text
    print(currentWord)
    # enter the word into input text area
    for x in currentWord:
        inputBox.send_keys(x)
    time.sleep(0.0375)
    inputBox.send_keys(Keys.SPACE)
    #increament the word count
    count+=1

# loop to keep page open
while True:
    time.sleep(1)