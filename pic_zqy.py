import threading
import time
import requests
from selenium import webdriver
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

# types = ['日历', '动漫', '风景', '美女', '游戏', '影视', '动态', '唯美', '设计', '可爱', '汽车', '花卉', '动物', '节日', '人物', '美食', '水果', '建筑', '体育', '军事', '非主流', '其他', '王者荣耀', '护眼', 'LOL'，'首页开始']
types_en = ['rili', 'dongman', 'fengjing', 'meinv', 'youxi', 'yingshi', 'dongtai', 'weimei', 'sheji', 'keai', 'qiche',
            'huahui', 'dongwu', 'jieri', 'renwu', 'meishi', 'shuiguo', 'jianzhu', 'tiyu', 'junshi', 'feizhuliu', 'qita',
            's/wangzherongyao', 's/huyan', 's/lol', '']


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, urls1, name, n):
        threading.Thread.__init__(self)
        self.urls1 = urls1
        self.n = n
        self.name = name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        browser = webdriver.PhantomJS()
        for url in self.urls1:
            try:
                browser.get(url)
                print(self.name + url)
                m = browser.find_element_by_xpath('//div[@id="main"]/div[@class="endpage"]/div[@class="pic"]/p/a')
                href2 = m.get_attribute('href')
                browser.get(href2)
                urll = browser.find_element_by_xpath('//*[@id="endimg"]/tbody/tr/td/a')
                href3 = urll.get_attribute('href')
                img = requests.get(href3, headers=headers).content
                print(img)
                cha = r'~`!@#$%^&()-={}:;'
                path = "C:\\Users\\86132\\Desktop\\images\\img" + self.name + str(self.n) + random.choice(cha) + str(
                    random.randint(0, 100)) + ".jpg"
                with open(path, 'wb') as f:
                    f.write(img)
                    time.sleep(1)
                    print(self.name + '----在地点' + str(self.n) + '获取第' + str(self.n) + '张图片\n………………………………………………………………………………')
                    self.n += 1
            except:
                continue
        browser.quit()


def T1(url, n):
    browser = webdriver.PhantomJS()
    browser.get(url)
    x = browser.find_elements_by_xpath('//div[@class="list"]/ul/li/a')
    print('本次旅行将带回' + str(len(x)) + '张高清图片,坐稳了！！！')
    urls1 = []
    for i in x:
        href = i.get_attribute('href')
        urls1.append(href)
    browser.quit()
    return urls1


def ts(num, low, urls1):
    nn = 1
    urls1a = urls1[0:num - 1]
    urls1b = urls1[num - 1:num * 2 - 1]
    urls1c = urls1[num * 2 - 1:num * 3 - 1]
    urls1d = urls1[num * 3 - 1:num * 4 + low - 1]
    # 创建新线程
    t1 = myThread(urls1a, "线程-爬大", nn)
    t2 = myThread(urls1b, "线程-爬二", nn)
    t3 = myThread(urls1c, '线程-爬三', nn)
    t4 = myThread(urls1d, '线程-爬小', nn)
    # 开启线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # 等待线程结束
    t1.join()
    t2.join()
    t3.join()
    t4.join()


def main():
    n = int(input('需要n*20张素材图片，n='))
    print(
        '1-日历, 2-动漫, 3-风景, 4-美女, 5-游戏,\n 6-影视, 7-动态, 8-唯美, 9-设计, 10-可爱, \n11-汽车, 12-花卉, 13-动物, 14-节日, 15-人物, \n16-美食, 17-水果, 18-建筑, 19-体育, 20-军事, \n21-非主流, 22-其他, 23-王者荣耀, 24-护眼, 25-LOL\n26--首页开始')
    yu = int(input('(0-26)请输入：'))
    url = 'http://www.netbian.com/' + types_en[yu - 1] + '/'
    urls1 = T1(url, n)
    num = int(len(urls1) / 4)
    low = len(urls1) % 4
    ts(num, low, urls1)
    k = 1
    if n >= 2:
        for k in range(1, n):
            url = 'http://www.netbian.com/' + types_en[yu - 1] + '/' + 'index_' + str(k + 1) + '.htm'
            urls1 = T1(url, n)
            num = int(len(urls1) / 4)
            low = len(urls1) % 4
            ts(num, low, urls1)
    else:
        print('###########################-------okokokokok-------###############################')


if __name__ == '__main__':
    main()
