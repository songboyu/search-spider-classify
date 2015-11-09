#coding=utf8
import datetime
import jieba

class Segmenter:
    def __init__(self):
        self.mainDict = self.LoadMainDict('dict/dict.txt')

    def Split(self, line):
        _words = []
        _len = len(line)
        while _len > 0:
            if _len > 4:
                cur_len = 4
            else:
                cur_len = _len
            cur = line[0:cur_len]
            while cur_len > 1:
                if cur in self.mainDict:
                    break
                else:
                    cur_len = cur_len - 1
                    cur = cur[0:cur_len]
            _words.append(cur)
            line = line[cur_len:]
            _len = _len - cur_len
        return _words

    def LoadMainDict(self, path):
        f = open(path, 'r')
        dicts = {}
        for line in f:
            line = line.split()[0].strip().decode('utf8')
            dicts[line] = 1
        f.close()
        print 'dict load OK'
        return dicts


if __name__ == '__main__':
    segmenter = Segmenter()
    f = open('data/test.txt')

    segStr = '巴勒斯坦自治领导机构主席阿拉法特３０日上午视察了拉马拉，受到成千上万巴勒斯坦市民的热烈欢迎。阿拉法特检阅了仪仗队，并在震耳欲聋的欢呼声中向群众发表了讲话。'
    _words = jieba.cut(segStr.decode('utf-8'))
    for wordstr in _words:
        print wordstr


    startTime = datetime.datetime.now()
    _words = []
    for line in f:
        # _words += segmenter.Split(line.decode('utf-8'))
        _words += jieba.cut(line.decode('utf-8'), cut_all=False)
    endTime = datetime.datetime.now()
    print (endTime - startTime).seconds