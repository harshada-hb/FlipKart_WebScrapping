from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("Mi 10")
driver.find_element_by_id("nav-search-submit-button").click()
Name=[]
urls=[]
content=driver.page_source
soup=BeautifulSoup(content)
html=soup.prettify('utf=-8')
adata=soup.findAll(["a","span"],class_=["a-link-normal a-text-normal\n","a-size-medium a-color a-text-normal\n"])
print(adata)

'''for x in adata:
    a_href=x.get("href")
    a_text=x.getText()
    urls.append(a_href)
    Name.append(a_text)'''

'''
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://w3schools.com")

print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.get("http://google.com")
print(driver.title)
time.sleep(5)
driver.back() #go back to w3schools.com site
print(driver.title)
time.sleep(5)

driver.forward() #go to google.com site
print(driver.title)
time.sleep(5)
driver.close()
'''