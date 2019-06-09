import requests
from collections import namedtuple
from bs4 import BeautifulSoup

# url = "https://www.wunderground.com/weather/ca/montreal/IMONTREA66?utm_source=HomeCard&utm_content=Button&cm_ven=HomeCardButton"
#
# content = requests.get(url)
# if content.status_code == 200:
#     html_content = content.text
#     # print(html_content)
#
#     soup = BeautifulSoup(html_content, features="html.parser")
#
#     # print(soup.title)
#
#     location = soup.find('city-header').find('div').find('h1').get_text()
#     location = location.strip()
#     print("Location: ", location)
#
#     temp = soup.find('display-unit').find('span').find(class_='wu-value').get_text()
#     temp = temp.strip()
#     print("Current temperature: ", temp)
#
#     currCond = soup.find('city-current-conditions').find(class_='condition-icon').find('p').get_text()
#     currCond = currCond.strip()
#     print("Current conditions: ", currCond)
#
#     displayUnit = soup.find('display-unit').find(class_='wu-label').get_text()
#     displayUnit= displayUnit.strip()
#     print("Display unit: " + displayUnit)
#
#     print("=" * 45)
#
#     MeteoInfo = namedtuple('MeteoInfo', 'location, temp, currCond, displayUnit')
#     report = MeteoInfo(location=location, temp=temp, currCond=currCond, displayUnit=displayUnit)
#     print(report)
# else:
#     print('Not Found.')



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, WebDriverException
#
# options = Options()
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
# driver.get('https://hidemyna.me/en/proxy-list/')
# while True:
#     try:
#         driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='arrow__right']/a"))))
#         driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
#         print("Navigating to Next Page")
#     except (TimeoutException, WebDriverException) as e:
#         print("Last page reached")
#         break
# driver.quit()

#==========================
# To use Selenium, install:
# 1. Selenium (an appropriate version for a Google Chrome browser version)
# 2. chromedriver, and put it in /usr/local/bin/

# This program starts Google Chrome's home page, types "ChromeDriver" in the search box, and presses Submit
#===========================

# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(8) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(8) # Let the user actually see something!
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.get('https://hidemyna.me/en/proxy-list/')

counter = 0

while counter < 6:
    try:
        driver.execute_script("return arguments[0].scrollIntoView(true);", \
                              WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='arrow__right']/a"))))
        driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
        print("Navigating to Page {}".format(counter))
        counter += 1
    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break
time.sleep(5)
driver.quit()