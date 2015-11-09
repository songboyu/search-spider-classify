#coding=utf-8

import sys
import random

if __name__ == '__main__':

    inputFile = 'data/data.txt'
    rate = 0.8
    trainOut = 'data/train.txt'
    testOut = 'data/test.txt'

    fin = open(inputFile, 'r')
    fTrain = open(trainOut, 'w')
    fTest = open(testOut, 'w')
    for line in fin:
        curRandom = random.random()
        if (curRandom <= rate):
            fTrain.write(line)
        else:
            fTest.write(line)
    print 'split OK'
    fin.close()
    fTrain.close()
    fTest.close()
