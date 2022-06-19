import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


#Open Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://qa-recruitment-task.netlify.app")
driver.execute_script("window.scrollBy(0,1200)", "") # scroll by pixel

sorting = Select(driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div/div/div[4]/div/div[2]/div/select"))
sorting.select_by_value('Price')
time.sleep(5)
sorting.select_by_value('Alphabetically')

time.sleep(5)

driver.quit()
