'''
用KNN对手写数字识别分类
数据集：sklearn自带的手写数字数据集（1797幅数字图像，每幅图像8*8像素）
'''
# 1.数据获取
# 2. 数据探索（样本数量，图像样子，识别结果）， 
# 3. 数据清洗（数据规范化，让数据在同一个数量级的维度），
# 4. 特征选择 （此次数据为图像，所以不需要进行特征选择，将全部图像数据作为特征值矩阵）
# 5. 模型训练 （通过训练得到分类器）
# 6. 模型评估 （利用测试集进行准确率的计算）

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import  preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# 1、 加载数据
from sklearn import datasets
# 加载数据集合 手写数字图片数据集 load_digits
digits = datasets.load_digits()

# 2、 数据探索
# 特征矩阵
feature  = digits.data
# 目标向量
target = digits.target
# 图片
images = digits.images
print(feature.shape) #(1797,64)
print(feature[0])
print(target[0])

plt.gray()
plt.imshow(images[0])
plt.show()

# 3、 划分测试集，训练集
train_x,test_x,train_y,test_y = train_test_split(feature,target,test_size=0.25,random_state=33)
#
# 4、  数据规范化处理 z-score规范化
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)


# # 引入sklearn中的KNN分类器
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform',algorithm='auto',leaf_size=30)
# 训练分类器
knn.fit(train_ss_x,train_y)
# 使用分类器进行预测
predict_y = knn.predict(test_ss_x)
# 输出分类器的准确率
print('KNN准确率：%.4lf' % accuracy_score(test_y,predict_y))
