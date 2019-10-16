# -*- coding: utf-8 -*-

import re

img = r'!\[.+\]\(.+\)'
fileDir = './md/'
filename = 'article.md'
# ImgNum = 60
githubImgUrl = 'https://raw.githubusercontent.com/Bounce00/pic/master/fpga/timing_toturial'

def replaceUrls(filename):
    with open(filename,'r',encoding='utf-8') as f:
        text = f.read()
        MdImgUrls = re.findall(img, text)
        for idx, itm in enumerate(MdImgUrls):   
            pos = itm.find('(')
            youdaoUrl = itm[pos+1:-1]
            githubUrl = githubImgUrl + str(idx) + '.png'
            text = text.replace(youdaoUrl, githubUrl)
    return text

def writeNewFile(fileDir, text):
    with open(fileDir + 'new.md', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    text = replaceUrls(fileDir + filename)
    writeNewFile(fileDir, text)


