from os import link
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from parsel import selector, Selector
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
# specifies the path to the chromedriver.exe
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())

#write excel names into python list -> names
data = pd.read_excel('Customer_Profiling.xlsx') 
df = pd.DataFrame(data)
names = df["PARENT'S FULL NAME"].tolist()
linkedin_urls = []
res = []

def launchBrowser():
    driver.get('https://www.linkedin.com') 
    username = driver.find_element_by_id('session_key')
    username.send_keys('')
    password = driver.find_element_by_id('session_password')
    password.send_keys('') #password
    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
    log_in_button.click()
    cycle = 0
    for name in names:
        options = Options()
        ua = UserAgent(verify_ssl=False)
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        driver_changing = webdriver.Chrome(chrome_options=options, executable_path = ChromeDriverManager().install())
        query = f'site:linkedin.com/in/ AND "{name}"' #use loop to get all names
        url = "http://www.google.com/search?q=" + query
        driver_changing.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        search = soup.find('div', class_="yuRUbf")
        if search:
            linkedin_urls.append(search.a.get('href'))
        else:
            continue
    print(linkedin_urls)
    for url in linkedin_urls:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_title = soup.find('div', class_="text-body-medium break-words")
        job_title = job_title.text
        res.append(job_title)
    # driver.get('https:www.google.com')
    # search_query = driver.find_element_by_name('q')
    # search_query.send_keys('site:linkedin.com/in/ AND "Chye Ming Ng"')
    # search_query.send_keys(Keys.RETURN)
    # linkedin_urls = driver.find_elements_by_class_name("yuRUbf")
    # for item in linkedin_urls:
    #     print(item.get_attribute("href"))
    # print(len(linkedin_urls))
    print(res)
    while(True):
       pass


launchBrowser()

