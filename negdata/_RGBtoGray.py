# -*- coding:utf8 -*-
import cv2
import numpy as np 
import os
import re
import shutil
from pathlib2 import Path
 
 
# 批量灰度化图片
def GrayPic(srcImgDir):
    for item in srcImgDir.rglob("*.jpg"):
        # 获取图片名
        imgName = item.name
        img=cv2.imread(imgName)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("gray"+imgName,gray)
        
        
if __name__ == '__main__':

    # 文件路径--跟代码同目录
    srcImgPath = Path("./")
    GrayPic(srcImgPath)
    
    os.system("pause")