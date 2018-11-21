import requests
import json

numberOfPages = 1
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

for pageNumber in range(numberOfPages):
    url_java_repos = 'https://api.github.com/search/repositories?q=stars%3A%3E%3D10+language%3Ajava&sort=stars&order=desc&page='+str(pageNumber+1)+'&per_page=100'
    url_kotlin_repos = 'https://api.github.com/search/repositories?q=stars%3A%3E%3D10+language%3Akotlin&sort=stars&order=desc&page='+str(pageNumber+1)+'&per_page=100' 
    r_java = requests.get(url_java_repos)
    r_kotlin = requests.get(url_kotlin_repos)
    input_java_repo.append(json.loads(r_java.text))
    input_kotlin_repo.append(json.loads(r_kotlin.text))

with open('java_repository_names', 'a') as text_file:
    for pageNumber in range(len(input_java_repo)):
        for repo in input_java_repo[pageNumber]['items']:
            date_repo = repo['created_at'][:-10]            
            lifespan = getLifespanInDays(getDateFormat(date_repo))
            text_file.write(repo['full_name']+', '+str(lifespan))
            text_file.write('\n')

with open('kotlin_repository_names', 'a') as text_file:
    for pageNumber in range(len(input_kotlin_repo)):
        for repo in input_kotlin_repo[pageNumber]['items']:            
            date_repo = repo['created_at'][:-10]
            lifespan = getLifespanInDays(getDateFormat(date_repo))
            text_file.write(repo['full_name']+', '+str(lifespan))
            text_file.write('\n')
