from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.common import exceptions
driver = webdriver.Chrome(executable_path = 'S:\Python\chromedriver')
EmployeeDataList = []
def Find_Employee(agency):
    driver.get('http://kanview.ks.gov/PayRates/PayRates_Agency.aspx')
    butt = driver.find_element_by_partial_link_text(agency)
    butt.click()

    for i in range(5):
        link = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(i))
        link.click()
        data = bs(driver.page_source,'lxml')
        emp_table = data.table
        df = pd.read_html(str(emp_table),header=0)
        EmployeeDataList.append(df)
        driver.back()
agency = input()
Find_Employee(agency)
print(EmployeeDataList)
driver.close()