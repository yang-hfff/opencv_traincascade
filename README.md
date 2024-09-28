# OPENCV级联分类器训练

## 1.收集样本

### 正样本
  - 转化成灰度（可用_RGBtoGray.py脚本）
  - 转化成jpg格式（可用_BMP2JPG.py脚本）
  - 分辨率20X20
  - 从0开始按序号命名（可用_ReName.py脚本）
### 负样本
  - 转化成灰度（可用_RGBtoGray.py脚本）
  - 转化成jpg格式（可用_BMP2JPG.py脚本）
  - 分辨率随意
  - 需要明显多于正样本
  - 从0开始按序号命名（可用_ReName.py脚本）

## 2.生成txt数据集路径表

  - 生成文件（可用_GenTXT.py脚本）
  - 拷贝到项目顶层目录（可用_copy.py脚本）

## 3.生成正样本数据集（负样本数据在下一步用于训练）
  - 编辑step1.py，根据自己的样本情况修改参数
  - 执行step1.py脚本

## 4.训练
  - 编辑step2.py，根据自己的样本情况修改参数
  - 执行step2.py脚本

## 3.得到模型
  - 进入xml文件夹，里面就有训练各个层数的模型

## 5.示范

 ```python
import cv2

# 读取待检测的图像
image = cv2.imread('12.jpg')

# 获取 XML 文件，加载人脸检测器
faceCascade = cv2.CascadeClassifier('cascade.xml')

# 色彩转换，转换为灰度图像
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 调用函数 detectMultiScale
faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5))

#print(faces)
# 打印输出的测试结果
print("发现{0}个人脸!".format(len(faces)))

# 逐个标注人脸
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2) #矩形标注
    #cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)
    
# 显示结果
cv2.imshow("dect",image)
# 保存检测结果
cv2.imwrite("re.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 ```
