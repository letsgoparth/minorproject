import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_page_source(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        page_source = str(soup)
        return page_source

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def save_to_file(page_source, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page_source)
            
        print(f"Page source saved to {filename}")

    except Exception as e:
        print(f"Error saving to file: {e}")

def get_companyName(file_content):
    
    pattern = r'"companyName":"([^"]+)"'

    matches = re.findall(pattern, file_content)
    return matches

def get_Location(file_content):
    
    pattern = r'"location":\[\{"id":\d+,"name":"([^"]+)"\}\]'

    matches = re.findall(pattern, file_content)
    return matches

def get_language(file_content):
    
    pattern = r'"mandatoryTags":\[\{"id":\d+,"name":"([^"]+)"'

    matches = re.findall(pattern, file_content)
    return matches

def get_positionTitle(file_content):
    pattern = r'"title":"(.*?)"'

    matches = re.findall(pattern, file_content)
    return matches

def get_experience(file_content):
    pattern = r'\((\d+-\d+) yrs\)'
    matches = re.findall(pattern, file_content)
    return matches

def get_allMandatorySkills(file_content):
    pattern = r'"title":"(.*?)".*?"mandatoryTags":\[(.*?)\]'
    
    matches = re.findall(pattern, file_content, re.DOTALL)
    return matches
    
def get_Date(file_content):
    pattern = r'"createdTimeMs":(\d+)'
    timestamps = re.findall(pattern, file_content)
    matches = timestamps
    # matches = [datetime.utcfromtimestamp(int(ts) / 1000.0) for ts in timestamps]
    return matches    

#-------------------------------------------------------------------------------------------

url = "https://www.hirist.com/search/python-p1.html?locIds=0&exp=0"
file_path = "page_source.txt"

# page_source=get_page_source(url)

with open(file_path, 'r') as file:
    page_source = file.read()
    
# if page_source:
#     save_to_file(page_source, file_path)

for name in get_companyName(page_source):
    print(name)

for name in get_positionTitle(page_source):
    print(name)
 
for name in get_language(page_source):
    print(name) 
 
for name in get_Location(page_source):
    print(name)

for name in get_experience(page_source):
    print(name)

for name in get_allMandatorySkills(page_source):
    mandatory_tags_part = name[1]

    skills = re.findall(r'"name":"(.*?)"', mandatory_tags_part)
    print(skills)

for timestamp in get_Date(page_source):
    full_date = datetime.utcfromtimestamp(int(timestamp) / 1000.0)
    date = full_date.date()
    formatted_date = date.strftime("%d-%m-%Y")
    print(formatted_date)