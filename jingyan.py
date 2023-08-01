import os
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

def clear_input_field(element):
    element.clear()

def sleep():
    pass
    # time.sleep(0)
def a(s):
    driver.find_element_by_link_text(s).click()
    sleep()
def an(s,num):
    if num==-1:return
    driver.find_elements_by_link_text(s)[num].click()
    sleep()
def ax(src):
    driver.find_element_by_xpath(src).click()
    sleep()

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

import math ,pytesseract ,cv2
from PIL import Image


# # 转化图像为白底黑字，一定要转化，能提高识别准确性
# def transformedImage():
#
#     # 计算两个颜色之间的欧几里得距离
#     def color_distance(c1, c2):
#         r1, g1, b1, a1 = c1
#         r2, g2, b2, a2 = c2
#         return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2 + (a1-a2)**2)
#
#     # 打开原图
#     img = Image.open(r'captcha.png')
#     # 创建一个白色的背景图像
#     bg_img = Image.new('RGBA', img.size, (255, 255, 255, 255))
#     # 定义相似颜色的阈值，5~200之间为最佳值，5~500为有效值
#     threshold = 100
#
#     # 遍历所有像素点
#     for x in range(img.width):
#         for y in range(img.height):
#             # 获取当前像素点的颜色
#             color = img.getpixel((x, y))
#             # 如果原图当前坐标颜色与给定颜色相似，则在背景图中相同的坐标写入黑色像素点
#             if color_distance(color, (247, 245, 244, 255)) < threshold:
#                 bg_img.putpixel((x, y), (0,0,0,255))
#
#     # 保存新图像
#     bg_img.save(r'captcha2.png')
#
#     print(characterRecognition())

# 文字识别
def characterRecognition():
    # 感觉好像没有必要进行灰度和二值化处理了，白底黑字的准确性挺高的，代码留这，你们自己看着整
    # 读取新图像
    # img = cv2.imread(r'screen\screen2.png')
    # # 将图片转换为灰度图像
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # 对图像进行二值化处理
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # config = "--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789"
    # text = pytesseract.image_to_string(thresh, config=config)

    # 读取新图像
    img = cv2.imread(r'captcha2.png')
    # 进行文字识别
    # --psm 7 单行识别 , --oem 3 使用 LSTM OCR 引擎 , -c tessedit_char_whitelist=0123456789 只识别数字字符
    config = "--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789"
    text = pytesseract.image_to_string(img, config=config)
    # 防止识别不到报错
    try:
        # 去除其他符号，对数字进行重新整合
        text = int(''.join(filter(str.isdigit, text)))
    except Exception:
        text = 1
        # 作者：听雨竞技 https://www.bilibili.com/read/cv22299763 出处：bilibili
    return text

if __name__ == '__main__':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("http://haixing8.cn/commreg/channel.php?d=login.start&clienttype=WAP2")  # 替换为你要测试的Web应用的URL

    login()
    # checkoutUser(checkoutCity)
    a("尊")
    a("尊")
    a("蒲牢")
    # a("霸下")
    while True:

        a("建筑")
        a("内政厅")
        # a("")
        page_text = driver.page_source
        # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
        # pattern = r'(高产县粮)'
        pattern = r'(中产县粮木)'

        match = re.search(pattern, page_text)
        if match:
            an("放弃",4)
            a("确定")

        a("返回首页")
        a("地图")
        a("中产县粮木")
        a("出兵")
        # 找到第一个输入框元素并修改其值为9000
        input_element = driver.find_element_by_name("s_4")
        input_element.clear()
        input_element.send_keys("15000")
        value = "出兵"
        xpath_expression = f'//input[@type="submit" and @value="{value}"]'
        submit_button = driver.find_element_by_xpath(xpath_expression)
        submit_button.click()
        # 根据按钮的value值找到提交按钮元素
        value = "普通出兵"
        xpath_expression = f'//input[@type="submit" and @value="{value}"]'
        submit_button = driver.find_element_by_xpath(xpath_expression)
        submit_button.click()

        import pytesseract


        while True:
            # 使用Selenium获取验证码图像的元素
            captcha_element = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/form[1]/div/img")
            # 保存验证码图像到本地
            captcha_image_path = "captcha.png"
            captcha_element.screenshot(captcha_image_path)
            # import pytesseract

            # # 替换为你实际的 tesseract 可执行文件路径
            # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            # # 使用OCR识别验证码图像中的文字
            # captcha_text = pytesseract.image_to_string(Image.open(captcha_image_path))

            # # 打印识别结果
            # print("验证码识别结果:", captcha_text)

            import paddleocr
            from paddleocr import PaddleOCR
            from selenium import webdriver
            from selenium.webdriver.common.by import By

            ocr = PaddleOCR()
            result = ocr.ocr('captcha.png')
            print(result)
            try:
                ocr_result = result[0][0][1]
                captcha_text = ocr_result[0]
                confidence = ocr_result[1]

                print("识别内容:", captcha_text)
                print("置信度:", confidence)
                input_element = driver.find_element_by_name("code")
                input_element.clear()
                input_element.send_keys(captcha_text)

                value = "出兵"
                xpath_expression = f'//input[@type="submit" and @value="{value}"]'
                submit_button = driver.find_element_by_xpath(xpath_expression)
                submit_button.click()
                page_text = driver.page_source
                # 使用正则表达式匹配农田、林场、石矿、铁矿 6→7级 和 (0:13:36)
                pattern = r'(错误)'
                match = re.search(pattern, page_text)
                if not match: break
            except:
                value = "换一个"
                xpath_expression = f'//input[@type="submit" and @value="{value}"]'
                submit_button = driver.find_element_by_xpath(xpath_expression)
                submit_button.click()

        os.remove(captcha_image_path)
        time.sleep(120)