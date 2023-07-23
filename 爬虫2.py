from selenium import webdriver
import time,csv

class QCWY:

    def __init__(self,keyword,city,maxpagenum):
        self.keyword = keyword
        self.city = city
        self.maxpagenum = maxpagenum



    def run(self):
        driver = webdriver.Chrome(r'f:\chromedriver.exe')
        driver.implicitly_wait(10)

        driver.get('http://www.51job.com')
        # 输入关键字
        driver.find_element_by_id('kwdselectid').send_keys(self.keyword)

        # 选择城市
        driver.find_element_by_id('work_position_input').click()

        # 等待一秒，确保界面稳定
        time.sleep(1)

        # 选择城市，点击上方当前已经选中的城市，去掉这些
        selectedCityEles = driver.find_elements_by_css_selector(
            '#work_position_click_multiple_selected > span')

        for one in selectedCityEles:
            one.click()


        # 然后再选择我们要选择的城市
        cityEles = driver.find_elements_by_css_selector(
            '#work_position_click_center_right_list_000000 em')


        target = None
        for cityEle in cityEles:
            # 如果城市名相同，找到了
            if cityEle.text == self.city:
                target = cityEle
                break

        # 没有找到该名称的城市
        if target is None:
            input(f'{self.city} 不在热门城市列表中，请手动点击选中城市后,按回车继续...')
        else:
            target.click()

        # 保存城市选择
        driver.find_element_by_id('work_position_click_bottom_save').click()

        driver.find_element_by_css_selector('div.ush > button').click()

        with open(f'前途无忧招聘_关键词_{self.keyword}_城市_{self.city}.csv',
                  'w', newline='', encoding='gbk') as f:

            f_csv = csv.DictWriter(f,
                                   ['职位名称',
                                    '公司名详细链接',
                                    '称',
                                    '工作地点',
                                    '薪资',
                                    '发布时间',
                                    '职位信息'])
            f_csv.writeheader()

            for pageNo in range(1,self.maxpagenum+1):
                # 设置页码
                pageNoInput= driver.find_element_by_id('jump_page')
                pageNoInput.clear()
                pageNoInput.send_keys(str(pageNo))
                driver.find_element_by_css_selector('span.og_but').click()

                # 暂停1秒
                time.sleep(1)

                rows = self.handleOnePage(driver)
                f_csv.writerows(rows)

                # 是否到了最后一页
                if self.isLastPage(driver):
                    break

    # 是否到了最后一页
    def isLastPage(self,driver):
        # 如果下一页是链接，表示还有下一页
        NextPageButton = driver.find_element_by_css_selector('div.dw_page li:last-child')

        driver.implicitly_wait(2)
        hasLink = NextPageButton.find_elements_by_tag_name('a')
        driver.implicitly_wait(10)
        if hasLink: # 不是最后一页
            return False
        else: # 是最后一页
            return True

    def handleOnePage(self,driver):

        rows = []
        # 处理每页信息
        jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')

        for job in jobs:
            fields = job.find_elements_by_tag_name('span')
            stringFilelds = [field.text for field in fields]
            print(stringFilelds)


            data = {
                "职位名称": stringFilelds[0],
                "公司名称": stringFilelds[1],
                "工作地点": stringFilelds[2],
                "薪资": stringFilelds[3],
                "发布时间": stringFilelds[4],
                # "职位信息": detail,
                # "公司信息": gongsi
            }

            # 点击打开详细链接
            fields[0].click()

            # mainWindow变量保存当前窗口的句柄
            mainWindow = driver.current_window_handle
            # 新打开的窗口总是句柄列表中的最后一个
            driver.switch_to.window(driver.window_handles[-1])


            info = driver.find_elements_by_css_selector('.tCompany_main .job_msg')

            if info and len(info)==1:
                # 职位信息
                data["职位信息"] = info[0].text

            rows.append(data)

            # 关闭具体信息页
            driver.close()
            # 通过前面保存的老窗口的句柄，自己切换到老窗口
            driver.switch_to.window(mainWindow)

        return rows

QCWY(keyword='python', city='上海', maxpagenum=1).run()