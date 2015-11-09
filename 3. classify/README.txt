步骤一  
运行data_importer.py，生成 "文本\t类别" 这样格式的数据。
处理数据时采用了jieba分词
修改代码中pick_num的值，可以控制数据总量（默认500*10=5000）

步骤二  
运行data_spliter.py，划分训练集和测试集
修改代码中rate的值，可以控制训练集、测试集比例（默认0.8 即4:1）

步骤三
运行train_test.py，对数据进行训练和预测
	
基于统计的分类算法是主流，主要包括以下几种分类模型：

相似度模型（Rocchio、K-近邻）
概率模型（贝叶斯）
线性模型（LR、SVM）
非线性模型（决策树、神经网络）

示例代码中提供了5种算法供参考及测试

1. Multinomial Naive Bayes Classifier（多项朴素贝叶斯）
2. k-nearest neighbors（K邻近）
3. Support Vector Machine（支持向量机）
4. Random Forest（随机森林）
5. Logistic Regression（线性回归）

尝试其他分类方法请参考scikit-learn doc（http://scikit-learn.org/stable/tutorial/index.html）

步骤四
运行classify.py，即可对指定文本进行分类，输出类别