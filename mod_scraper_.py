from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

import pandas as pd
import re  # regular expression library
import string
import time
import csv

from mod_sqlite import *

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.get('https://hidemyna.me/en/proxy-list/')

counter = 1
num_pages_to_search = 4

# clear "proxies_raw.csv" file
f = open("./proxies_raw.csv", "w")
f.close()

# write titles of CSV columns
f = open("./proxies_raw.csv", "w")
f.write("{}".format("IP_address,Port,Country_City,Speed,Type,Anonymity,Last_Check"))
f.close()


def wait_until_page_visible(xpath):
    driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(
                              EC.element_to_be_clickable((By.XPATH, xpath))))


def find_element(xpath):
    return driver.find_element_by_xpath(xpath)


while counter < num_pages_to_search:
    try:
        wait_until_page_visible("//li[@class='arrow__right']/a")
        with open("./proxies_raw.csv", "a") as f:
            table = find_element("//table[@class='proxy__t']")

            # read each row as line
            for row in table.find_elements_by_xpath(".//tr"):
                line = [td.text.strip() for td in row.find_elements_by_xpath(".//td")]

                # remove special characters
                allow = string.ascii_letters + string.digits + '.' + ','
                line = re.sub('[^%s]' % allow, '', str(line))

                # If two protocol types are given ("HTTP, HTTPS"), unite them into one type.
                if line.count(",") + 1 == 8:
                    temp_arr = line.split(',')
                    temp_arr[4] = line.split(',')[4] + line.split(',')[5]
                    temp_arr[5] = line.split(',')[6]
                    temp_arr[6] = line.split(',')[7]
                    temp_arr = temp_arr[:7]
                    line = ','.join(temp_arr)
                print(line)

                # save each row into the 'proxies_raw.csv' file
                f.write(line + "\n")
                create_table()
                insert_into_table()


        # remove empty lines:
        df = pd.read_csv('proxies_raw.csv')
        df.to_csv('proxies_no_empty_lines.csv', index=False)

        # Add an ID column, and save into "proxies_with_id.csv"
        with open("./proxies_no_empty_lines.csv", 'r') as input, open('proxies_with_id.csv', 'w+') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')

            data = []
            row = next(reader)
            row.insert(0, 'ID')
            data.append(row)
            count = 0
            for row in reader:
                count += 1
                row.insert(0, count)
                data.append(row)
            writer.writerows(data)

        # save data into a SQLite database


        # click on the right arrow, to go to the next page
        driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
        print("Navigating to Page {}".format(counter+1))
        counter += 1
    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break
# time.sleep(1)
driver.quit()