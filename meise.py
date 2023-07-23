import re
import string
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from msedge.selenium_tools import Edge, EdgeChromiumDriverManager



def clear_input_field(element):
    element.clear()

def sleep():
    time.sleep(1)
def a(s):
    driver.find_element_by_link_text(s).click()
    sleep()
def an(s,num):
    if num==-1:return
    driver.find_elements_by_link_text(s)[num].click()
    sleep()

# def auto():
#     # 执行测试用例
#     for test_case in test_cases:
#         month, day, year = test_case
#         # print(month, day, year)
#         next_day = get_next_day(month, day, year)
#         print(next_day)
# def autoInt():
#     while True:
#         year=random.randint(1800,2090)
#         month=random.randint(-1, 13)
#         day=random.randint(-1, 32)
#         next_day = get_next_day(month, day, year)
#         print(next_day)
#
# def autoFloat():
#     while True:
#         year=round(random.uniform(1800,2090),2)
#         month=round(random.uniform(-1, 13),2)
#         day=round(random.uniform(-1, 32),2)
#         next_day = get_next_day(month, day, year)
#         print(next_day)
#
# def autoString():
#     while True:
#         length = 4  # 字符串长度
#         characters = string.ascii_letters + string.digits + string.punctuation
#         month = ''.join(random.choice(characters) for i in range(length))
#         day = ''.join(random.choice(characters) for i in range(length))
#         year = ''.join(random.choice(characters) for i in range(length))
#         next_day = get_next_day(month, day, year)
#         print(next_day)


def women():

    meinv = driver.find_element_by_link_text("美女")
    time.sleep(2)
    meinv.click()
    elements = driver.find_elements_by_partial_link_text("召见")

    i=0
    for item in elements:
        driver.find_elements_by_link_text("召见")[i].click()
        i+=1
        time.sleep(1)
        try:
            see = driver.find_element_by_link_text("召见")
            time.sleep(2)
            see.click()
            back = driver.find_element_by_link_text("返回后宫")
            time.sleep(2)
            back.click()
        except NoSuchElementException:
            back = driver.find_element_by_link_text("返回")
            time.sleep(2)
            back.click()

    try:
        nextPage = driver.find_element_by_link_text("下页")
        time.sleep(2)
        nextPage.click()
        elements = driver.find_elements_by_link_text("召见")
        nextPage = driver.find_element_by_link_text("上页")
        time.sleep(2)
        nextPage.click()
        i = 0
        for item in elements:

            nextPage = driver.find_element_by_link_text("下页")
            time.sleep(3)
            nextPage.click()
            time.sleep(2)
            driver.find_elements_by_link_text("召见")[i].click()
            i += 1
            time.sleep(1)
            try:
                see = driver.find_element_by_link_text("召见")
                time.sleep(3)
                see.click()
                back = driver.find_element_by_link_text("返回后宫")
                time.sleep(3)
                back.click()
            except NoSuchElementException:
                back = driver.find_element_by_link_text("返回")
                time.sleep(3)
                back.click()
    except NoSuchElementException:
        print("没有第二页")

    back = driver.find_element_by_link_text("返回首页")
    back.click()

def ziyuan():
    # 获取页面文本
    page_text = driver.page_source
    # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
    pattern = r'(农田|林场|石矿|铁矿)\d+(→)\d+级 (\d+:\d+:\d+)'
    match = re.search(pattern, page_text)

    if match:
        return
    else:
        a("资源")
        # 获取当前页面的源代码
        page_content = driver.page_source
        # 判断页面内容中是否存在"还需"的2个字
        if "还需" in page_content:
            a("返回首页")
            return
        else:
            # 获取页面内容
            page_content = driver.page_source
            # 分析页面内容并找到等级最小的序号
            page_content = page_content.replace("20级", "")
            lines = re.findall(r"<img.+?>(.+?)\s(\d+)级", page_content)

            # 初始化最小等级和序号
            min_level = float("inf")
            min_index = -1

            for i, line in enumerate(lines):
                level = int(line[1])  # 将提取到的等级转换为整数

                if level < min_level:
                    min_level = level
                    min_index = i
            an("升", min_index)
            a("返回首页")




def jianzhu():
    # 获取页面文本
    page_text = driver.page_source
    # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
    pattern = r'(内政厅|后　宫|选妃馆|招贤馆|集　市|兵　营|仓　库|粮　库|城　墙|暗　仓|神机营])\d+(→)\d+级 (\d+:\d+:\d+)'
    match = re.search(pattern, page_text)
    if match:
        return
    else:
        a("建筑")
        # 获取当前页面的源代码
        page_content = driver.page_source
        # 判断页面内容中是否存在"还需"的2个字
        if "还需" in page_content:
            a("返回首页")
            return
        else:
            # 获取页面内容
            page_content = driver.page_source
            # 分析页面内容并找到等级最小的序号
            page_content = page_content.replace("20级", "")
            lines = re.findall(r"<img.+?>(.+?)\s(\d+)级", page_content)

            # 初始化最小等级和序号
            min_level = float("inf")
            min_index = -1

            for i, line in enumerate(lines):
                level = int(line[1])  # 将提取到的等级转换为整数

                if level < min_level:
                    min_level = level
                    min_index = i
            an("升", min_index)
            a("返回首页")


def gonzi():
    a("任务")
    a("领取日薪俸")
    a("返回")
    a("领取周薪俸")
    a("返回")
    a("祭天祈福")
    a("设坛祭天")
    a("确定")
    a("返回")
    a("返回")
    a("返回首页")

def xuanjiang(username,city):
    a("武将")
    a("选将")
    # 获取页面文本
    page_text = driver.page_source
    # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
    pattern = r'(声望型|谋略型|元帅型|猛将型)'
    match = re.search(pattern, page_text)
    if match:
        print(f"${username} 的{city}有好武将")
    a("返回首页")
def xuanfei(username,city):
    a("美女")
    a("选妃")
    # 获取页面文本
    page_text = driver.page_source
    # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
    pattern = r'(★★★|★★★★|★★★★★|★★★★★★|★★★★★★★|★★★★★★★★|★★★★★★★★★|绝世美女|倾城美女|倾国美女)'
    match = re.search(pattern, page_text)
    if match:
        print(f"${username} 的{city}有好美女")
    a("返回首页")
def do(username,city):
    # women()
    ziyuan()
    jianzhu()

    # xuanjiang(username, city)
    # xuanfei(username,city)

def checkoutCity(username):
    userCity={
        "尊":["饕餮","睚眦","嘲风", "蒲牢", "狻猊", "霸下", "狴犴", "负屃", "螭吻", "囚牛","穷奇"][::-1],
              '禹白晴':["龟攻我","新的城市"][::-1],
              '袁腾飞':["佩琪打我","新的城市"][::-1],
              '呼延谷丝':["华为","新的城市"][::-1],
              '柴文石':["鳖答我","新的城市"][::-1],
              '神':["打我死妈","新的城市"][::-1],
              '东方求败':["傻猪打我","新的城市"][::-1],
              '魔':["天","新的城市"][::-1],
              '打客 服F':["阿呆吖"][::-1],
              '宇文紫山':["三上悠亚","新的城市"][::-1],
              '沈孤丝':["新的城市"][::-1]

              }

    user = driver.find_element_by_link_text(username)
    city=userCity[username]
    time.sleep(3)
    user.click()
    for item in city:
        time.sleep(3)
        driver.find_element_by_link_text(item).click()
        do(username,item)
        user = driver.find_element_by_link_text(username)
        time.sleep(3)
        user.click()
    a("返回首页")

def login():
    username = "18570694530"
    password = "w11226677"
    usernameInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))  # 替换为月份输入框的ID
    passwordInput = driver.find_element(By.NAME, "password")  # 替换为日期输入框的ID
    submit_button = driver.find_element(By.NAME, "submit")  # 替换为提交按钮的ID
    clear_input_field(usernameInput)
    usernameInput.send_keys(username)
    clear_input_field(passwordInput)
    passwordInput.send_keys(password)
    submit_button.click()
    sleep()
    element = driver.find_element_by_link_text("美色34服(卧虎藏龙)")
    element.click()
    sleep()


def checkoutUser(func):
    users=[
        # '尊',
        # '禹白晴','袁腾飞','呼延谷丝',
        '柴文石','神','东方求败','魔',
        '打客 服F',
        '宇文紫山']
    for username in users:
        user = driver.find_element_by_link_text(username)
        user.click()
        # gonzi()
        func(username)
        driver.find_element_by_link_text("系统").click()
        driver.find_element_by_link_text("切换人物").click()
    users=['沈孤丝']
    a("下一页")
    for username in users:
        user = driver.find_element_by_link_text(username)
        user.click()
        # gonzi()
        func(username)
        driver.find_element_by_link_text("系统").click()
        driver.find_element_by_link_text("切换人物").click()


if __name__ == '__main__':

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("http://haixing8.cn/commreg/channel.php?d=login.start&clienttype=WAP2")  # 替换为你要测试的Web应用的URL

    login()
    checkoutUser(checkoutCity)
    # checkout(username,women)