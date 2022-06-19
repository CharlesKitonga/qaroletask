import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://qa-recruitment-task.netlify.app/")
driver.execute_script("window.scrollBy(0, 1300)", "") #scroll by pixel

driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/input").click()

time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[5]/div/div[1]/div/div[2]/div/div[4]/div/div/input").click()

time.sleep(2)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div/div/div[5]/div/div[1]/div/div[2]/div/div[6]/div/div/input")))
element.click()

driver.quit()