import requests # http requests
from bs4 import BeautifulSoup # Webscrape
from collections import defaultdict # Default dictionary: store a list with each key
import pandas as pd     # DF
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())



headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

# Skills & Place of Work
skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the # of pages to scrape: '))

indeed_posts=[]

for page in range(no_of_pages):
    
    # Connecting to India Indeed
        url = 'https://www.indeed.co.in/jobs?q=' + skill + \
            '&l=' + place + '&sort=date' +'&start='+ str(page * 10)
        
        # Get request to indeed with headers above (you don't need headers!)
        # response = requests.get(url, headers=headers)
        # html = response.text
        
        # Scrapping the Web (you can use 'html' or 'lxml')
        # soup = BeautifulSoup(html, 'lxml')

        
        dr = webdriver.Chrome()
        dr.get(url)
        bs = BeautifulSoup(dr.page_source,"lxml")
        print(bs.prettify())


#         # Outer Most Entry Point of HTML:
#         outer_most_point=soup.find('div',attrs={'id': 'mosaic-provider-jobcards'})
        
#         # "UL" lists where the data are stored:
        
#         for i in outer_most_point.find('ul'):
            
#         # Job Title:
        
#             job_title=i.find('h2',{'class':'jobTitle jobTitle-color-purple jobTitle-newJob'})
# #             print(job_title)
#             if job_title != None:
#                 jobs=job_title.find('a').text

#         # Company Name:
    
#             if i.find('span',{'class':'companyName'}) != None:
#                 company=i.find('span',{'class':'companyName'}).text   
                
#         # Links: these Href links will take us to full job description
        
#             if i.find('a') != None:
#                 links=i.find('a',{'class':'jcs-JobTitle'})['href']
                
#         # Salary if available:
        
#             if i.find('div',{'class':'attribute_snippet'}) != None:
#                 salary=i.find('div',{'class':'attribute_snippet'}).text

#             else:
#                 salary='No Salary'

#         # Job Post Date:

#             if i.find('span', attrs={'class': 'date'}) != None:
#                 post_date = i.find('span', attrs={'class': 'date'}).text

#         # Put everything together in a list of lists for the default dictionary
                        
#             indeed_posts.append([company,jobs,links,salary, post_date])
            
            
# # put together in list

# # (create a dictionary with keys and a list of values from above "indeed_posts")

# indeed_dict_list=defaultdict(list)

# # Fields for our DF 

# indeed_spec=['Company','job','link','Salary','Job_Posted_Date']