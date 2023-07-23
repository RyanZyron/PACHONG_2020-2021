import time,csv
import requests,re

class QCWY:

    def __init__(self,keyword,city,maxpagenum):
        self.keyword = keyword
        self.city = city
        self.maxpagenum = maxpagenum



    def run(self):

        areaCode = self.getAreaCode()
        totalPage = None


        with open(f'前途无忧招聘_关键词_{self.keyword}_城市_{self.city}.csv',
                  'w', newline='', encoding='gbk') as f:

            f_csv = csv.DictWriter(f,
                                   ['职位名称',
                                    '详细链接',
                                    '公司名称',
                                    '工作地点',
                                    '薪资',
                                    '发布时间',
                                    '职位信息'])
            f_csv.writeheader()

            for pageNo in range(1,self.maxpagenum+1):
                headers = {
                    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
                    'Host': 'search.51job.com',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Cookie': 'guid=1ad595306c11a03a55dac236b622d7cf; adv=adsnew%3D1%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Furl%253D0000000ZX-6UukFJV5Go8fZlcCEq7tFNTglsmR8mRlzUgA_Y0xJRotWHnJ-wnNS93kLv9cjXcmgqw3IqXfLndYvLo8QY3hRDsyV5b32vP-SMy5s-g_Vdrfux-eylqi1Emau_BR-EFN17Srdi9WVkw-_K948tFo7nDBqyuH7kDsdByEAzSLzuY0Eysff2J28F3_qqS4_jjPEPPxUcQER9heMeRE22.7b_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIO0hWEzxkZeMgxJNkOhzxzP7Si1xOvP5dkOz5LOSQ6HJmmlqoZHYqrVMuIo9oEvpSMG34QQQYLgFLIW2IlXk2-muCyr1FkzTf.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPH7JUvc0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqPH7JUvc0ThPv5HD0IgF_gv-b5HDdnH6YnHnvnHf0UgNxpyfqnHczPHc3P1b0UNqGujYknjmYPjm4nfKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00mLFW5Hm1nHcz%2526ck%253D797.11.119.354.166.299.326.412%2526dt%253D1594260533%2526wd%253D51job%2526tpl%253Dtpl_11534_22672_18815%2526l%253D1518413614%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60080200%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%B5%CF%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA01%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA04%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA01%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21',
                    'Connection': 'keep-alive'
                }

                url = f'https://search.51job.com/list/{areaCode},000000,0000,00,9,99,{self.keyword},2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
                print(url)

                res = requests.get(url, headers = headers, verify=False)
                time.sleep(1)
                resBody = res.content.decode('gbk')
                # print(resBody)

                # 判断总共多少页
                if totalPage is None:
                    pattern = r'id=\"hidTotalPage\".*?value=\"(.*?)\"'
                    tp = re.findall(pattern,resBody)[0]
                    print(f'总共 {tp} 页')
                    totalPage = int(tp)

                pattern = r'<div class=\"el\">.*?class=\"t1.*?\">.*?<a.*?>(?P<job>.*?)</a>.*?class=\"t2\"><a.*?>(?P<company>.*?)</a>.*?class=\"t3\">(?P<addr>.*?)</span>.*?class=\"t4\">(?P<salary>.*?)</span>.*?class=\"t5\">(?P<date>.*?)</span>'


                p = re.compile(pattern, re.DOTALL)
                for match in p.finditer(resBody):


                    row = {
                        "职位名称": match.group('job').strip(),
                        "公司名称": match.group('company'),
                        "工作地点": match.group('addr'),
                        "薪资": match.group('salary'),
                        "发布时间": match.group('date'),
                    }

                    f_csv.writerow(row)

                # 是否到了最后一页
                if pageNo == totalPage :
                    break



    def getAreaCode(self):
        '''https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js
        经过抓包，分析得出，地区码的请求在

        '''

        res = requests.get('https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js')
        part1 = res.text.split('area=')[1].split(';')[0]
        code2area = eval(part1)
        # print(code2area)

        # 创建反向查询字典
        area2code = {v: k for k, v in code2area.items()}
        # print(area2code)

        if self.city not in area2code:
            print(f'查无此地: {self.city}')
            exit(2)

        return area2code[self.city]

QCWY(keyword='python', city='上海', maxpagenum=1).run()