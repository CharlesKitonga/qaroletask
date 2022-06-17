from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import  time

#Open Chrome Browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://qa-recruitment-task.netlify.app")
driver.execute_script("window.scrollBy(0,1100)", "") # scroll by pixel

while True:
    current_page_number = int(driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div > div:nth-child(5) > div > div.style__Column-sc-4ctdae-1.eAPRKs > div > div.style__Column-sc-4ctdae-1.iTjutW > div > div > ol > li:nth-child(2)').text)
    next_page_link = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ol[1]/li[8] ")
    next_page_link.click()
    time.sleep(2)
