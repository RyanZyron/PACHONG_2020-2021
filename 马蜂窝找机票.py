from selenium import webdriver
import time,csv


class MFW:
    def __init__(self,city1,city2,maxpagenum):
        self.city1 = city1
        self.city2 = city2
        self.maxpagenum = maxpagenum - 1

    def run(self):

        driver = webdriver.Chrome(r'/Volumes/Samsung_T5/edgedriver_arm64/chromedriver')
        driver.implicitly_wait(5)

        driver.get('https://www.mafengwo.cn/flight/#/index')
        # J_FlightForm input[name="depCityName"]
        r = driver.find_element_by_css_selector('.depCity input[type="text"]')
        r.clear()
        driver.find_element_by_css_selector('.depCity input[type="text"]').send_keys(self.city1)
        l = driver.find_element_by_css_selector('.arrCity input[type="text"]')
        l.clear()
        driver.find_element_by_css_selector('.arrCity input[type="text"]').send_keys(self.city2)
        driver.find_element_by_css_selector('.flightpc-index-search >.flightpc-index-search-text').click()

        with open(f'测试111111.csv',
                  'w', newline='', encoding='gbk') as f:

            f_csv = csv.DictWriter(f,
                                   ['航司及航班号',
                                    '机型',
                                    '起飞时间',
                                    '起飞机场',
                                    '飞行时间',
                                    '到达时间',
                                    '到达机场'])
            f_csv.writeheader()
            # 暂停1秒
            time.sleep(1)
            rows = self.onepage(driver)
            f_csv.writerows(rows)
            i = 1
            while i <= self.maxpagenum:
                NextPageButton = driver.find_elements_by_css_selector('div.fltlist-pagination >.disabled')
                time.sleep(1)

                if NextPageButton:
                    break
                else:
                    driver.find_element_by_css_selector('div.fltlist-pagination div:last-child').click()
                    time.sleep(2)
                    rows = self.onepage(driver)
                    f_csv.writerows(rows)
                i += 1
            driver.close()

            # 是否到了最后一页



            # 是否到了最后一页

    def isLastPage(self, driver):
            # 如果下一页是链接，表示还有下一页
        NextPageButton = driver.find_element_by_css_selector('div.fltlist-pagination div:last-child')

        driver.implicitly_wait(2)
        hasLink = NextPageButton.find_elements_by_css_selector('.disabled')
        driver.implicitly_wait(10)
        if hasLink:  # 不是最后一页
            return True
        else:  # 是最后一页
            return False


    def onepage(self,driver):
        # 处理每页信息
        jobs = driver.find_elements_by_css_selector('.v-list-item-content')
        row = []
        for job in jobs:
            fields = job.find_elements_by_tag_name('div')
            stringFilelds = [field.text for field in fields]
            print(stringFilelds)
            data = {
                "航司及航班号": stringFilelds[2],
                "机型": stringFilelds[3],
                "起飞时间": stringFilelds[5],
                "起飞机场": stringFilelds[6],
                "飞行时间": stringFilelds[7],
                "到达时间": stringFilelds[12],
                "到达机场": stringFilelds[13],
            }
            row.append(data)
        return row



MFW(city1=str(input("出发城市是：")),city2=str(input("到达城市是：")),maxpagenum=int(input("您最多想找几页信息："))).run()