import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
driver = webdriver.Chrome(executable_path = 'S:\Python\chromedriver')
driver.get('https://www.mayoclinic.org/diseases-conditions')
# List for the alphabets:
alphabets = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
alphabets.append('#')
Disease=dict.fromkeys(alphabets)
names=[]
for i in alphabets:
    link = driver.find_element_by_id('et_alphaListFilter_'+i+'_21249c04-8988-4f5a-9b92-8e63debc7bba')
    link.click()
    New_link = driver.current_url
    req = requests.get(New_link)
    print('-------------------')
    print(req.status_code)
    print(req.url)
    print('-------------------')
    data = req.text
    info = bs(data , 'html.parser')
    disease = info.find(class_ = 'index content-within')
    for j in disease.find_all('li'):
        name_link = driver.find_element(a)['href']
        name_link.click()
        # req = requests.get(name_link)
        # n = req.text
        # names = bs(n, 'html.parser')
        # n = names.find('h1')
        # print('StatusCode: ' + str(req.status_code))
        # print('URL : ' + req.url)
        # print('Text :' + n.text)
    print(type(disease))
    driver.back()