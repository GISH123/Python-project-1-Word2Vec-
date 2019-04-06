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

print("Because I can only use 8 colors in matplotlib, please limit your topics to 8 topics")
input_list = input("Enter topics(use \"space\" to split different topic):")
keyword_number = input("Enter how many keywords you want to search for each topic:")
key_list = list(map(str, input_list.split(" ")))



model = word2vec.load('hw1Word2Vec.bin')
# print(model.vectors)
rawWordVec=model.vectors

X_reduced = PCA(n_components=2).fit_transform(rawWordVec) # reduce the dimension of word vector

# show some word(center word) and it‘s similar words
index_and_metrics = {}
for i in range(len(key_list)):
    index_and_metrics["index{0}".format(i)],index_and_metrics["metrics{0}".format(i)] =  model.cosine(u'%s' %key_list[i],int(keyword_number)-1)
  #  index1,metrics1 = model.cosine(u'%s' %key_list[i])
  #  index2,metrics2 = model.cosine(u'信用卡')
  #  index3,metrics3 = model.cosine(u'匯率')
  #  index4,metrics4 = model.cosine(u'台積電')
  #  index5,metrics5 = model.cosine(u'台灣')
  #  index6,metrics6 = model.cosine(u'日本')

# add the index of center word
indexes = {}
for i in range(len(key_list)):
    indexes["index0{0}".format(i)] = np.where(model.vocab==u'%s' % key_list[i])
#index01=np.where(model.vocab==u'銀行')
#index02=np.where(model.vocab==u'信用卡')
#index03=np.where(model.vocab==u'匯率')
#index04=np.where(model.vocab==u'台積電')
#index05=np.where(model.vocab==u'台灣')
#index06=np.where(model.vocab==u'日本')

#numpy append
final_indexes = {}
for i in range(len(key_list)):
    final_indexes["index{0}".format(i)] = np.append(index_and_metrics["index{0}".format(i)],indexes["index0{0}".format(i)])
#index2=np.append(index2,index03)
#index3=np.append(index3,index03)
#index4=np.append(index4,index04)
#index5=np.append(index5,index05)
#index6=np.append(index6,index06)


# plot the result
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)
fig = plt.figure()
ax = fig.add_subplot(111)

colors = ['b','g','r','c','m','y','k','w'] #color by order: blue,green,red, ...etc
color_count = 0
topic_count = 0
for key,val in final_indexes.items():
    for i in final_indexes["index{0}".format(color_count)]:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color= colors[color_count])
        print("第{0}個主題的關鍵字 為 {1}".format(topic_count,model.vocab[i]))
    topic_count += 1
    color_count += 1




if(False): #comment out
    for i in index2:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color='b')

    for i in index3:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color='g')

    for i in index4:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color='k')

    for i in index5:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color='c')

    for i in index6:
        ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i],fontproperties=font,color='y')

ax.axis([-0.5,0.5,-0.5,0.5])
plt.show()


if(False): # for testing
    print(text_title.head(3))
    print(text_content.head(3))
if(False): # for testing
    with open('hw1_text.xlsx') as hw1_fie:
        for line in hw1_file:

    # word segmentation
          fileTrainSeg=[]
          for i in range(len(fileTrainRead)):
             fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11],cut_all=False)))])
if(False): # showing the results of model
    for i in range(0,10):
        print(model.vectors[i])
        print(model.vocab[i])
if(False):
    indexes = model.cosine(u'外資') # trying a keyword in hw1Word2Vec.bin
    print(indexes)
    for index in indexes[0]:
        print(model.vocab[index])
