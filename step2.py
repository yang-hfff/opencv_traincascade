import os

#numPos和numNeg是训练时每一层的样本数，numPos可以小于vec中的数目（推荐），numNeg可以大于实际数目
#maxFalseAlarmRate是训练时的FA，只有小于它才会进入下一层
#网上推荐numPos：numNeg=1：3
#正样本用vec描述，负样本用txt指明路径即可
#xml目录需要自己提前创建
#训练时出现的列表中：N训练层数，HR命中率，FA警告（FA<maxFalseAlarmRate进入下一层）
#负样本不用指定图中:目标个数，Xmin,Ymin,Xmax,Ymax。训练时会自动resize
os.system("opencv_traincascade.exe -data xml -vec pos.vec -bg neg.txt -numPos 90 -numNeg 198 -numStages 20 -w 20 -h 20 -maxFalseAlarmRate 0.5 -mode ALL")

os.system("pause");
