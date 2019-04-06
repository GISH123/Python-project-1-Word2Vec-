import pandas as pd
import jieba
import word2vec
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties # for matplot chinese
import re
from sklearn.decomposition import PCA
path = u'hw1_text.xlsx'
def get_title():
    title =  pd.read_excel(path,"all",encoding='utf-8')['標題']
    return title
def get_content():
    content = pd.read_excel(path,"all")['內容']
    return content
def clean_string(temp):
    string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",temp)
    return string

text_title = get_title()
for i in range(len(text_title)): # to trim out special characters
    text_title[i] = clean_string(text_title[i])

text_content = get_content()
for i in range(len(text_content)): # to trim out special characters
    text_content[i] = clean_string(text_content[i])

fileTrainSeg=[]
for i in range(len(text_title)): # word segmentation
    fileTrainSeg.append([' '.join(list(jieba.cut(text_title[i],cut_all=False)))])

#with open("hw1Output1.txt", "w", encoding='utf-8') as text_file: # output a txt file with segmented words
#      print(fileTrainSeg, file=text_file)

with open("hw1Output1.txt", "w", encoding='utf-8') as text_file:
   for i in range(len(fileTrainSeg)):
       for j in range(len(fileTrainSeg[i])):
        text_file.write(fileTrainSeg[i][j])
        text_file.write('\n')

word2vec.word2vec('hw1Output1.txt', 'hw1Word2Vec.bin', size=300,verbose=True)

