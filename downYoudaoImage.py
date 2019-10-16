# -*- coding: utf-8 -*-

import re 

img = r'!\[.+\]\(.+\)'

fileDir = './md/'
filename = 'text.md'
ImgUrls = []
imgDir = './img/'
img_name = 'timing_toturial'


def getUrls(filename):
    with open(filename,'r',encoding='utf-8') as f:
        text = f.read()
        MdImgUrls = re.findall(img, text)
        for itm in MdImgUrls:
            pos = itm.find('(')
            ImgUrls.append(itm[pos+1:-1])
            # print(itm)


def urllib_download(urlLst, imgDir):
    from urllib.request import urlretrieve
    for idx,url in enumerate(urlLst):
        urlretrieve(url, imgDir + img_name + str(idx) + '.png')



if __name__ == "__main__":
    getUrls(fileDir + filename)
    urllib_download(ImgUrls, imgDir)

