import hrefs as hrefs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import  time

#Open Chrome Browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://qa-recruitment-task.netlify.app")

# add an implicit wait
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,1000)", "") # scroll by pixel
# Find a product by xPath
findProductA = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[5]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/img")

# Hover over a product
actions = ActionChains(driver)
actions.move_to_element(findProductA).click().perform()

addtoCart = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[5]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/button").click()

time.sleep(3)
# Check if add to cart in the header section is clickable
headerBtn = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div/div[2]/button").click()

# removeBtn = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
clearBtn = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div/div[2]/div/div/div[3]/button").click()
actions = ActionChains()
actions.move_to_element(clearBtn).perform()
time.sleep(2)

driver.quit()
