'''
用KNN对手写数字识别分类
数据集：sklearn自带的手写数字数据集（1797幅数字图像，每幅图像8*8像素）
'''
# 1.数据获取
#准备阶段
# 2. 数据探索（样本数量，图像样子，识别结果）， 
# 3. 数据清洗（数据规范化，让数据在同一个数量级的维度），
# 4. 特征选择 （此次数据为图像，所以不需要进行特征选择，将全部图像数据作为特征值矩阵）

# 模型训练 （通过训练得到分类器）
# 模型评估 （利用测试集进行准确率的计算）

# 加载数据
import numpy as np
import pandas as pd

# 引入sklearn中的KNN分类器
# 分类
from sklearn.neighbors import KNeighborsClassifier
# 回归
from sklearn.neighbors import KNeighborsRegressor

# 创建分类器
