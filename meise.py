import math
import re
import string
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from msedge.selenium_tools import Edge, EdgeChromiumDriverManager


# 清空输入框
def clear_input_field(element):
    element.clear()
# 延时防止网页拉黑
def sleep():
    time.sleep(0.5)
# 点击链接
def a(s):
    driver.find_element_by_link_text(s).click()
    sleep()
# 点击第几个链接
def an(s,num):
    if num==-1:return
    driver.find_elements_by_link_text(s)[num].click()
    sleep()
# 点击xpath
def ax(src):
    driver.find_element_by_xpath(src).click()
    sleep()

# 召见（满足）美女
def meet():
    a("美女")
    num=1
    try:
        page_text = driver.page_source
        pattern = r'已有(\d+)人'
        num = re.findall(pattern, page_text)[0]
        num=int(num)
        num=math.ceil(num/6)
    except:
        pass

    for i in range(num):
        elements = driver.find_elements_by_partial_link_text("召见")
        for index,item in enumerate(elements):
            an("召见",index)
            try:
                a("召见")
                driver.back()
                driver.back()
            except NoSuchElementException:
                driver.back()
        try:
            a("下页")
        except:
            pass

    a("返回首页")

# 资源升级
def resources(nong):
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
            # 使用JavaScript获取页面的文字内容
            text = driver.execute_script("return document.body.innerText")
            # 统计关键词出现次数
            keyword = "农田"
            count = text.count(keyword)

            # 初始化最小等级和序号
            min_level = float("inf")
            min_index = -1

            for i, line in enumerate(lines):
                if nong:
                    if i < count:continue
                level = int(line[1])  # 将提取到的等级转换为整数

                if level < min_level:
                    min_level = level
                    min_index = i
            an("升", min_index)
            a("返回首页")

# 建筑升级
def build():
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

# 每日任务
def daily():
    a("任务")
    a("活动")
    a("领取日薪俸")
    a("返回")
    a("领取周薪俸")
    a("返回")
    a("祭天祈福")
    a("设坛祭天")
    a("确定")
    a("返回")
    a("返回")
    try:
        a("讲武堂")
        ax("/html/body/div/div/div/div/div/div/div/div/div/div/p[1]/a[4]")
    except:
        pass

    a("任务")
    try:
        a("琉球诛魔")
        a("领取奖励")
        a("返回")

    except:
        pass
    a("任务")
    try:
        a("琉球诛魔")
        a("报名琉球诛魔（13:00:00-第二天12:30:00）")
        an("选将",0)
        ax("/html/body/div/div/div/div/div/div/div/div/div/div/p[1]/a[2]")
        an("选择",0)
        a("返回")
        a("报名")
        a("鼓舞士气")
        a("确定")
    except:
        pass
    a("任务")
    try:
        a("占星卜运")
        a("占卜1次")
        a("星运背包")
        a("绿色")
        a("绿色星运全部炼化灵力")
        a("确定")
    except:
        pass
    a("任务")
    a("首页")
    try:
        a("联盟")
        a("联盟活动")
        an("点亮",0)
    except:
        pass
    a("首页")

# 选将
def general(username,city):
    a("武将")
    a("选将")
    # 获取页面文本
    page_text = driver.page_source
    # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
    pattern = r'<a href=".+?">(..型)</a>'
    types = re.findall(pattern, page_text)
    # print(types)
    pattern = r'(声望型|谋略型|元帅型|猛将型)'
    match = re.search(pattern, page_text)
    while match:
        k = 0
        # 遍历数组并判断是否为猛将型或元帅型
        for index,type_name in enumerate(types):
            if type_name == '猛将型' or type_name == '元帅型' or type_name == '声望型' or type_name == '谋略型':
                try:
                    an("招募",index-k);
                    a("返回")
                    k += 1
                    print(f"${username} 的{city}招募{type_name}武将成功")
                except:
                    print(f"${username} 的{city}招募{type_name}武将失败")
            else:
                pass
        page_text = driver.page_source
        match = re.search(pattern, page_text)
    a("返回首页")

# 选妃
def beauty(username,city):
    a("美女")
    a("选妃")
    # 获取页面文本
    page_text = driver.page_source
    pattern = r'星级:(无|★+|..美女) '
    types = re.findall(pattern, page_text)
    # print(types)
    pattern = r'(★★★|★★★★|★★★★★|★★★★★★|★★★★★★★|★★★★★★★★|★★★★★★★★★|绝世美女|倾城美女|倾国美女)'
    match = re.search(pattern, page_text)
    while match:
        arget_types = {'★★★', '★★★★', '★★★★★', '★★★★★★', '★★★★★★★', '★★★★★★★★', '★★★★★★★★★', '绝世美女', '倾城美女', '倾国美女'}
        k=0
        # 使用for循环遍历数组并打印类型名称和下标
        for index,type_name in enumerate(types):
            if type_name in arget_types:
                try:
                    an("迎娶",index-k)
                    a("返回")
                    k+=1
                    print(f"${username} 的{city}招募{type_name}美女成功")
                except:
                    print(f"${username} 的{city}招募{type_name}美女失败")
            else:
                pass
        page_text = driver.page_source
        match = re.search(pattern, page_text)
    a("返回首页")

def do(username,city,control):
    if control.get("general"): general(username, city)
    if control.get("beauty"): beauty(username,city)
    if control.get("meet"):meet()
    if control.get("resources"):resources(True)
    if control.get("build"):build()


def checkoutCity(username,control):
    userCity={
        "尊":["饕餮","睚眦","嘲风", "蒲牢", "狻猊", "霸下", "狴犴", "负屃", "螭吻", "囚牛","穷奇"][::-1],
              '禹白晴':["龟攻我","再来一发","新的城市"][::-1],
              '袁腾飞':["佩琪打我","烽火江山","新的城市"][::-1],
              '呼延谷丝':["华为","新的城市"][::-1],
              '柴文石':["鳖答我","新的城市"][::-1],
              '神':["打我死妈","新的城市"][::-1],
              '东方求败':["傻猪打我","新的城市"][::-1],
              '魔':["天","新的城市"][::-1],
              '打客 服F':["阿呆吖"][::-1],
              '宇文紫山':["三上悠亚","新的城市"][::-1],
              '沈孤丝':["新的城市"][::-1]
              }
    city=userCity[username]
    a(username)
    for item in city:
        a(item)
        do(username,item,control)
        a(username)
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
    a("美色34服(卧虎藏龙)")


def checkoutUser(func,control):
    users=[
        '尊',
        '禹白晴',
        '袁腾飞','呼延谷丝',
        '柴文石','神','东方求败','魔',
        '打客 服F',
        '宇文紫山']
    for username in users:
        a(username)
        if control.get("daily"): daily()
        func(username,control)
        a("系统")
        a("切换人物")
    users=['沈孤丝']
    a("下一页")
    for username in users:
        a(username)
        if control.get("daily"): daily()
        func(username,control)
        a("系统")
        a("切换人物")


if __name__ == '__main__':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("http://haixing8.cn/commreg/channel.php?d=login.start&clienttype=WAP2")  # 替换为你要测试的Web应用的URL

    login()
    control1={
        'meet':True,
        'resources':True,
        'build':True,
        'general': True,
        'beauty': True,
        'daily':True,
    }
    control2={
        'meet':False,
        'resources':True,
        'build':True,
        'general': False,
        'beauty': False,
        'daily':False,
    }

    checkoutUser(checkoutCity,control1)