import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from  sklearn.cluster import DBSCAN

# 加载数据
iris = datasets.load_iris()
# 使用4个特征
X = iris.data[:, :4]
print(X.shape)


# 应用密度聚类
dbscan = DBSCAN(eps=0.4, min_samples=9)
dbscan.fit(X)
label_pred = dbscan.labels_

# 绘制结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()