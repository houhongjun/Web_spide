# -*- coding:utf-8 -*-

#引入机器学习模块
import pytesseract
#引入图形处理模块
from PIL import Image

#引入一张图片
img = Image.open("bb.png")
tessdata_dir_config = '--tessdata-dir "D:\\pytesseract\\Tesseract-OCR\\tessdata"'
#识别图片
text = pytesseract.image_to_string(img,config=tessdata_dir_config)

print(text)