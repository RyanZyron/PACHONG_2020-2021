
from selenium import webdriver
import time,csv

driver = webdriver.Chrome(r'/Volumes/Samsung_T5/edgedriver_arm64/chromedriver')

driver.implicitly_wait(5)
page = 2
driver.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_2.shtml')
flights = driver.find_elements_by_css_selector('a[title^="截至"]')
print(flights)
"""
for flight in flights:
    fields = flight.find_elements_by_tag_name('div')
    stringFilelds = [field.text for field in fields]
    data = {
                "航班号": stringFilelds[0],
                "机型": stringFilelds[1],
                "航空公司": stringFilelds[2],
                "目的站点": stringFilelds[3],
                "计划起飞": stringFilelds[6],
                "实际起飞": stringFilelds[8],
                "登机口": stringFilelds[9],
                }
    rows.append(data)
    print(stringFilelds)
            
    page += 1

"""
driver.close()

