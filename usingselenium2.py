from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# DRIVER_PATH = 'chromedriver.exe'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))



service = Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.formula1.com/en.html")

# Print page source on screen
print(driver.page_source)

# ...
driver.quit()