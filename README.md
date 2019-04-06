此作品在Anaconda環境下，使用PyCharm IDE進行coding

使用Jieba套件對中文資料進行斷詞斷句(目前繁體中文的斷詞斷句效果較簡體差)  
藉由word2vec實行Vector space based方式，將文字資料弄成向量空間，計算彼此之間的餘弦值來比較關聯程度  
最後使用matplotlib套件，將結果以圖呈現(成果例子可以看看此頁的PNG檔)  
  
#資料集：
使用聯合影音網，類別為"全部財經新聞"，2016/1/1至2016/8/31"的資料 ( by 爬蟲)


首先執行fileSeg.py

使用者執行後輸入 以空格來分割的一串主題 (EX.以老師要求的主題來說 六個主題  輸入  "銀行 信用卡 匯率 台積電 台灣 日本" 包含空格 不包含引號)
只要有出現在hw1Output1.txt的字串(即jieba切好字詞的檔案)，出現次數大過5 的主題都可以找關鍵字
並使用matploblib繪成平面

fileSeg.py 使用jieba切割文字 並把完成後的文字檔處理成bin檔案(讓Word2Vec能使用)

keywordPlot.py 使用者可以輸入最多8個topic 讓word2vec尋找關鍵字(目前找10個) 並繪圖
