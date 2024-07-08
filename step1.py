import os

#处理前要将pos.txt里面每行按"*.jpg 1 0 0 20 20"的格式修改，neg.txt不需要改格式
#neg.txt和pos.txt里面末尾的空行要删去
#neg.txt里面图片大小和数量可以不用特别指定，也不需要生成vec文件
os.system("opencv_createsamples.exe -vec pos.vec -info pos.txt -num 100 -w 20 -h 20")

os.system("pause");