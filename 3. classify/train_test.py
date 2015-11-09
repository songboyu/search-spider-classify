# coding: utf-8
import sys

import numpy as np
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.feature_extraction.text import HashingVectorizer

from sklearn import ensemble
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.svm import SVC 
from sklearn import linear_model

'''加载数据'''
def input_data(train_file, test_file):
    train_words = []
    train_tags = []

    for line in open(train_file, 'r'):
        tks = line.split('\t')
        train_words.append(tks[0])
        train_tags.append(tks[1])

    test_words = []
    test_tags = []
    for line in open(test_file, 'r'):
        tks = line.split('\t')
        test_words.append(tks[0])
        test_tags.append(tks[1])

    return train_words, train_tags, test_words, test_tags

'''文本向量化'''
def vectorize(train_words, test_words):
    # 停用词表
    with open('dict/stopwords.txt', 'r') as f:
        stopwords = set([w.strip() for w in f])

    v = HashingVectorizer(non_negative=True, stop_words=stopwords, n_features=30000)
    train_data = v.fit_transform(train_words)
    test_data = v.fit_transform(test_words)
    return train_data, test_data

'''计算准确率、召回率、F1'''
def evaluate(actual, pred):
    m_precision = metrics.precision_score(actual, pred, average='weighted')
    m_recall = metrics.recall_score(actual, pred, average='weighted')
    m_f1_score = metrics.f1_score(actual,pred, average='weighted')

    print u' 准确率:     {0:0.3f}'.format(m_precision)
    print u' 召回率:     {0:0.3f}'.format(m_recall)
    print u' F1-score:   {0:0.3f}'.format(m_f1_score);  

'''多种分类算法'''
# Multinomial Naive Bayes Classifier（多项朴素贝叶斯）
def train_clf_MNB(train_data, train_tags):
    clf = MultinomialNB(alpha=0.01)
    clf = clf.fit(train_data, np.asarray(train_tags))
    return clf
# k-nearest neighbors（K邻近）
def train_clf_KNN(train_data, train_tags):
    clf = KNeighborsClassifier() # default with k=5  
    clf = clf.fit(train_data, np.asarray(train_tags))
    return clf
# Support Vector Machine（支持向量机）
def train_clf_SVM(train_data, train_tags):
    clf = SVC(kernel = 'linear') # default with 'rbf' 
    clf = clf.fit(train_data, np.asarray(train_tags))
    return clf
# Random Forest（随机森林）
def train_clf_RF(train_data, train_tags):
    clf = ensemble.RandomForestClassifier(n_estimators=500, max_depth=10, n_jobs=-1)
    clf = clf.fit(train_data, np.asarray(train_tags))
    return clf
# Logistic Regression（线性回归）
def train_clf_LR(train_data, train_tags):
    clf = linear_model.LogisticRegression()
    clf = clf.fit(train_data, np.asarray(train_tags))
    return clf


def main():
    train_file = 'data/train.txt'
    test_file = 'data/test.txt'
    # 加载数据
    print  '\nload ======================================='
    train_words, train_tags, test_words, test_tags = input_data(train_file, test_file)
    print 'Step 1: input_data OK'
    train_data, test_data = vectorize(train_words, test_words)
    print 'Step 2: vectorize OK'

    # Multinomial Naive Bayes Classifier
    print '\nMNB ======================================='
    # 训练
    clf = train_clf_MNB(train_data, train_tags)
    print 'Step 3: train_clf OK'
    # 保存模型
    joblib.dump(clf, 'model/'+str(type(clf))[8:-2]+'.model')
    print 'Step 4: model save OK'
    # 预测
    pred = clf.predict(test_data)
    print 'Step 5: predict OK'
    # 计算准确率、召回率、F1
    evaluate(np.asarray(test_tags), pred)
    print 'Step 6: evaluate OK'

if __name__ == '__main__':
    main()