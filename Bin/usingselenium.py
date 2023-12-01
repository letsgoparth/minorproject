
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# val = input("Enter a url: ")


# key = input("Enter a url: ")

# key = "laptop"

val = "view-source:https://in.indeed.com/jobs?q=python+developer&l=Delhi&from=searchOnHP&vjk=9c992ae9ab5c1d1cP"
wait = WebDriverWait(driver, 10)
driver.get(val)

get_url = driver.current_url

bs = BeautifulSoup(driver.page_source,"lxml")
print(bs.prettify())
wait.until(EC.url_to_be(val))

print(driver)

# element = driver.find_element(By.ID, "jcs-JobTitle css-jspxzf eu4oa1w0")
# text_content = element.text
# print(text_content)
print("just printed it")


# driver.find_element_by_css_selector('.button .c_button .s_button').click()


# if get_url == val:
#     page_source = driver.page_source
# soup = BeautifulSoup(page_source,features="html.parser")
# keyword=input("Enter a keyword to find instances of in the article:")
matches = soup.body.find_all(string=re.compile("companyName"))

# len_match = len(matches)
# title = soup.title.text
# file=codecs.open('article_scraping.txt', 'a+')
# file.write(title+"\n")
# file.write("The following are all instances of your keyword:\n")

# count=1

# for i in matches:
#     file.write(str(count) + "." +  i  + "\n")
#     count+=1

# file.write("There were "+str(len_match)+" matches found for the keyword.")
# file.close()

# driver.quit()