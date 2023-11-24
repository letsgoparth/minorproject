import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import csv

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
    new_match = []
    
    matches = re.findall(pattern, file_content)
    for match in matches:
        print(match)
        nm = match.split(" - ")
        if len(nm)>1:
            # print(nm[-2])
            new_match.append(nm[-2])
        else:
            new_match.append("null")
    return new_match

def get_experience(file_content):
    pattern = r'\((\d+-\d+) yrs\)'
    matches = re.findall(pattern, file_content)
    return matches

def get_allMandatorySkills(file_content):
    pattern = r'"title":"(.*?)".*?"mandatoryTags":\[(.*?)\]'
    
    skill_list = []
    
    matches = re.findall(pattern, file_content, re.DOTALL)
    for name in matches:
        mandatory_tags_part = name[1]
        skills = re.findall(r'"name":"(.*?)"', mandatory_tags_part)
        skill_list.append(skills)
    
    return skill_list
    
def get_Date(file_content):
    pattern = r'"createdTimeMs":(\d+)'
    timestamps = re.findall(pattern, file_content)
    matches = timestamps
    
    final_date = []
    # matches = [datetime.utcfromtimestamp(int(ts) / 1000.0) for ts in timestamps]
    for timestamp in matches:
        full_date = datetime.utcfromtimestamp(int(timestamp) / 1000.0)
        date = full_date.date()
        formatted_date = date.strftime("%d-%m-%Y")
        # print(formatted_date)
        final_date.append(formatted_date)
        
    return final_date

def write_CSV(list,csv_path):
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
    
        for row in list:
            csv_writer.writerow(row)
    print("Data has been written to"+str(csv_path))
    
#-------------------------------------------------------------------------------------------

url = "https://www.hirist.com/search/react.html?locIds=0&exp=0&ref=homepage"
file_path = "page_source.txt"

page_source=get_page_source(url)

# with open(file_path, 'r') as file:
#     page_source = file.read()
    
if page_source:
    save_to_file(page_source, file_path)

# print(get_companyName(page_source))
# print('\n')
# print(get_positionTitle(page_source))
# print('\n')
# print(get_language(page_source))
# print('\n')
# print(get_Location(page_source))
# print('\n')
# print(get_experience(page_source))
# print('\n')
# print(get_allMandatorySkills(page_source))
# print('\n')
# print(get_Date(page_source))
# print('\n')

main_list = list(zip(
    get_companyName(page_source),
    get_positionTitle(page_source),
    get_language(page_source),
    get_Location(page_source),
    get_experience(page_source),
    get_allMandatorySkills(page_source),
    get_Date(page_source)
    ))

# for row in main_list:
#     print(row)
#     print('\n')
    
write_CSV(main_list,"file.csv")




# for name in get_companyName(page_source):
#     print(name)

# for name in get_positionTitle(page_source):
#     print(name)
 
# for name in get_language(page_source):
#     print(name) 
 
# for name in get_Location(page_source):
#     print(name)

# for name in get_experience(page_source):
#     print(name)

# for name in get_allMandatorySkills(page_source):
#     print(name)




