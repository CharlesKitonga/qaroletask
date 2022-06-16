from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Open Chrome Web Browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://qa-recruitment-task.netlify.app")

print(driver.title)  # Get Page Title

time.sleep(5)

driver.close()  # close all browsers
