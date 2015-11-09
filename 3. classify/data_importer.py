#encoding=utf8

import os
import re
import random
import dircache

import jieba

if __name__ == '__main__':
    pick_num = 500
    
    dirNameDict = { 
         'C0': 0, # 汽车
         'C1': 1, # 财经
         'C2': 2, # 科技
         'C3': 3, # 健康
         'C4': 4, # 体育
         'C5': 5, # 旅游
         'C6': 6, # 教育
         'C7': 7, # 招聘
         'C8': 8, # 文化
         'C9': 9, # 军事
    }
     
    outputPath = 'data/data.txt'
    inputDir = 'data/ClassFile/'
    ofs = open(outputPath, 'w')
    dirnum = 0
    for dirName in dirNameDict.keys():
        newDir = inputDir + dirName + '/'
        if not os.path.exists(newDir):
            continue
        fileList = dircache.listdir(newDir)
        filenum = -1
        picked = 0

        # 从0-7999中随机抽取500个数
        s = random.sample(range(8000), pick_num)

        for fileName in fileList:
            filenum += 1

            # 只取随机的500个文件，控制数据总量
            if filenum not in s:
                continue

            picked += 1
            filePath = newDir + fileName
            if not os.path.exists(filePath):
                continue

            ifs = open(filePath, 'r')
            text = ifs.read()
            text = text.replace('\xa1\xa1',' ')
            text = text.decode('gbk', 'ignore')
            text = text.replace('\n', ' ')
            text = text.replace('\t', ' ')

            text = ' '.join(jieba.cut(text, cut_all=False))
            text = re.sub(u'[$^()-=~！@#￥%……&*（）——+·{}|：“”《》？【】、；‘’，。、]+', u'', text)

            ofs.write(text.encode('utf-8') + '\t' + str(dirNameDict[dirName]) + '\n')
            ifs.close()
        print dirnum, picked
        dirnum += 1

    ofs.close()