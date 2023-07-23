from selenium import webdriver
import time,csv
# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
class QCWY:
    def __init__(self,keyword,city,maxpagenum):
        self.keyword = keyword
        self.city = city
        self.maxpagenum = maxpagenum

    def run(self):
        driver = webdriver.Chrome(r'f:\chromedriver.exe')
        driver.implicitly_wait(10)

        driver.get('http://www.51job.com')
        #输入关键字
        driver.find_element_by_id('kwdselectid').send_keys(self.keyword)
        #选择城市
        driver.find_element_by_id('work_position_input').click()
        #等待两秒
        time.sleep(1)
        #点掉所有的城市
        selectedCityEles = driver.find_elements_by_css_selector(
            '#work_position_click_multiple_selected>span')
        for one in selectedCityEles:
            one.click()

        cityEles = driver.find_elements_by_css_selector(
            '#work_position_click_center_right_list_000000 em')

        target = None
        for cityEle in cityEles:
            if cityEle.text == self.city:
                target = cityEle
                break

        if target is None:
            input(f'{self.city}不在热门城市中')
        else:
            target.click()
        #保存城市选择后点击搜索
        driver.find_element_by_id('work_position_click_bottom_save').click()

        driver.find_element_by_css_selector('div.ush > button').click()
        # 处理每页信息
        jobs = driver.find_elements_by_css_selector("#resultList div[class=el]")
        for job in jobs:
            fileds = job.text
            fileds_text = fileds.split()
            print(fileds_text)

QCWY(keyword="python" , city="杭州" , maxpagenum=1).run()
