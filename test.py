# import pytesseract
# from PIL import Image
#
# try:
#     # 替换为你实际的 tesseract 可执行文件路径
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
#     # 加载图像
#     image = Image.open('fuck.png')
#
#     # 使用 OCR 识别图像中的文本
#     text = pytesseract.image_to_string(image)
#
#     # 输出识别结果
#     print("识别结果:", text)
#
# except Exception as e:
#     print("OCR 错误:", str(e))


from paddleocr import PaddleOCR
from selenium import webdriver
from selenium.webdriver.common.by import By
ocr = PaddleOCR()
result = ocr.ocr('captcha.png')
ocr_result = result[0][0][1]
captcha_text = ocr_result[0]
confidence = ocr_result[1]

print("识别内容:", captcha_text)
print("置信度:", confidence)