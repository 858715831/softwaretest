import string
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear_input_field(element):
    element.clear()

def get_next_day(month, day, year):
    options = Options()
    # options.add_argument("--headless")  # 无界面运行浏览器
    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:3000/")  # 替换为你要测试的Web应用的URL

    month_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "month")))  # 替换为月份输入框的ID
    day_input = driver.find_element(By.ID, "day")  # 替换为日期输入框的ID
    year_input = driver.find_element(By.ID, "year")  # 替换为年份输入框的ID
    submit_button = driver.find_element(By.ID, "submit")  # 替换为提交按钮的ID

    clear_input_field(month_input)
    month_input.send_keys(str(month))

    clear_input_field(day_input)
    day_input.send_keys(str(day))

    clear_input_field(year_input)
    year_input.send_keys(str(year))
    # time.sleep(5)

    submit_button.click()

    next_day_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result")))  # 替换为显示下一天日期的元素ID

    next_day = next_day_element.text

    # time.sleep(2)
    driver.quit()
    # print(next_day)
    return next_day


# 等价类测试示例
test_cases = [
    (1, 1, 1900),
    (1, 1, 1899),
    (1, 1, 2051),
    (-1, 7, 2050),
    (13, 29, 2000),
    (1, -1, 2001),
    (1, 32, 2000),
    (4, 30, 2001),
    (4, -1, 2000),
    (4, 31, 2001),
    (2, 28, 2001),
    (2, -1, 2001),
    (2, 29, 2001),
    (2, 29, 2000),
    (2, -1, 2000),
    (2, 30, 2000),
    (1, 1, 0.1),
    (0.2, 1, 1900),
    (1, 0.3, 1900),
    (4, 0.4, 1900),
    (2, 0.5, 2001),
    (2, 0.6, 2000)
]



def auto():
    # 执行测试用例
    for test_case in test_cases:
        month, day, year = test_case
        # print(month, day, year)
        next_day = get_next_day(month, day, year)
        print(next_day)
def autoInt():
    while True:
        year=random.randint(1800,2090)
        month=random.randint(-1, 13)
        day=random.randint(-1, 32)
        next_day = get_next_day(month, day, year)
        print(next_day)

def autoFloat():
    while True:
        year=round(random.uniform(1800,2090),2)
        month=round(random.uniform(-1, 13),2)
        day=round(random.uniform(-1, 32),2)
        next_day = get_next_day(month, day, year)
        print(next_day)

def autoString():
    while True:
        length = 4  # 字符串长度
        characters = string.ascii_letters + string.digits + string.punctuation
        month = ''.join(random.choice(characters) for i in range(length))
        day = ''.join(random.choice(characters) for i in range(length))
        year = ''.join(random.choice(characters) for i in range(length))
        next_day = get_next_day(month, day, year)
        print(next_day)

if __name__ == '__main__':
    auto()
    # autoInt()
    # autoFloat()
    # autoString()