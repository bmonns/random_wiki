
from urllib import response
import requests
import os

def retrieve_wikipage():
    url = 'https://en.wikipedia.org/api/rest_v1/page/random/summary'
    response = requests.get(url).json()
    extract = '\n------------------------------------------------------------\n' + response['extract'] +'\n------------------------------------------------------------\n'

    print(extract)
    print("Would you like to read this article? (y/n): ",end='')
    answer = input()

    if answer == 'y':
       wiki_url = response['content_urls']['desktop']['page'] 
       os.system("open " + wiki_url)
       print('Web page opened in  browser\n')      

print("Welcome to the random wiki page generator\nHere is the first article")

new_articles = True
while new_articles:
    retrieve_wikipage()
    print('Would you like to view a new article? (y/n): ', end='')
    cont = input()
    if cont == 'n':
        new_articles = False


