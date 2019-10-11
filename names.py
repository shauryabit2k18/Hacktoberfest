from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

links=[]
driver.get("https://www.facebook.com/groups/BITMesra/members/")

SCROLL_PAUSE_TIME = 0.5
# get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0 , document.body.scrollHeight);")
    # wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height = last_height:
        break
    last_height = new_height

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findALL('div' , attrs = {'class':'clearfix _60rh _gse'}):
    links = a.find('a' , attrs = {'class':'_60rg _8o _8r lfloat _ohe'} , href = True)
    id.append(links.text)

df = pd.DataFrame({'links' : links})
df.to_csv('links.csv' , index = true , encoding='utf-8')