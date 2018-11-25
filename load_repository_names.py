import sys
import requests
import json
import datetime
from datetime import date
import time

def test_case():
    return 5, 1

def user_spec_sample(sample_size):   
    if(sample_size == 5):
        print("Test case is running ...")
        return test_case()
    elif(sample_size == 100):
        return sample_size, 1
    elif(sample_size == 200):
        return sample_size, 2
    elif(sample_size == 300):
        return sample_size, 3
    elif(sample_size == 400):
        return sample_size, 4
    elif(sample_size == 500):    
        return sample_size, 5
    elif(sample_size == 1000):    
        return sample_size, 10
    else:
        print("Please use 100, 200, 300, 400, 500 or 1000 as a sample size. Test case (sample size = 5) will be executed now.")
        return test_case()

input_java_repo = []
input_kotlin_repo = []

def getLifespanInDays(givenDate):
    datetime_now = getDateFormat(datetime.datetime.today().strftime('%Y-%m-%d'))    
    delta = datetime_now-givenDate
    return delta.days

def getDateFormat(givenDate):
    year = int(givenDate[:-6])
    month = int(givenDate[5:7])
    day = int(givenDate[8:10])
    return (date(year, month, day))

try:
    user_argument = (int(sys.argv[1]))
    sample_size_and_pages = user_spec_sample(user_argument)
    number_of_pages = sample_size_and_pages[1]
    per_page = sample_size_and_pages[0]
except IndexError:
    print("Please use 100, 200, 300, 400, 500 or 1000 as an argument for the sample size. Test case (sample size = 5) will be executed now.")
    sample_size_and_pages = test_case()
    number_of_pages = sample_size_and_pages[0]
    per_page = sample_size_and_pages[1]
       
for page_number in range(number_of_pages):
    url_java_repos = 'https://api.github.com/search/repositories?q=stars%3A%3E%3D10+language%3Ajava&sort=stars&order=desc&page='+str(page_number+1)+'&per_page='+str(per_page)
    url_kotlin_repos = 'https://api.github.com/search/repositories?q=stars%3A%3E%3D10+language%3Akotlin&sort=stars&order=desc&page='+str(page_number+1)+'&per_page='+str(per_page)
    r_java = requests.get(url_java_repos)
    r_kotlin = requests.get(url_kotlin_repos)
    input_java_repo.append(json.loads(r_java.text))
    input_kotlin_repo.append(json.loads(r_kotlin.text))
    time.sleep(10)

with open('java_repository_names', 'a') as text_file:
    for page_number in range(len(input_java_repo)):
        for repo in input_java_repo[page_number]['items']:
            date_repo = repo['created_at'][:-10]            
            lifespan = getLifespanInDays(getDateFormat(date_repo))         
            text_file.write(repo['full_name']+', '+str(lifespan)+', '+str(repo['open_issues'])+', '+str(repo['stargazers_count']))
            text_file.write('\n')

with open('kotlin_repository_names', 'a') as text_file:
    for page_number in range(len(input_kotlin_repo)):
        for repo in input_kotlin_repo[page_number]['items']:            
            date_repo = repo['created_at'][:-10]
            lifespan = getLifespanInDays(getDateFormat(date_repo)) 
            text_file.write(repo['full_name']+', '+str(lifespan)+', '+str(repo['open_issues'])+', '+str(repo['stargazers_count']))
            text_file.write('\n')
