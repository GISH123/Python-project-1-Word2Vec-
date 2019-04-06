此作品在Anaconda環境下，使用PyCharm IDE進行coding

使用Jieba套件對中文資料進行斷詞斷句(目前繁體中文的斷詞斷句效果較簡體差)  
藉由word2vec實行Vector space based方式，將文字資料弄成向量空間，計算彼此之間的餘弦值來比較關聯程度  
最後使用matplotlib套件，將結果以圖呈現(成果例子可以看看此頁的PNG檔)  

# 如果只想純粹使用看看，直接下載整份文件下來，執行keywordPlot.py即可"  
使用者執行keywordPlot.py後輸入 以空格來分割的一串主題 (這邊我使用的範例為六個主題  輸入  "銀行 信用卡 匯率 台積電 台灣 日本" 包含空格)  
只要有出現在hw1Output1.txt的字串(即jieba切好字詞的檔案)，出現次數大過5的主題都可以找關鍵字  
並使用matploblib繪成平面

# 資料集：
使用聯合影音網，類別為"全部財經新聞"，2016/1/1至2016/8/31"的資料 ( by 爬蟲)  
執行fileSeg.py之後(可使用其他資料，相關檔名自行更改)將這些資料(因為超過25mb無法上傳github)使用Word2Vec轉換成向量形式，儲存為一個名為hw1Word2Vec.bin的檔案，以供keywordPlot.py使用

#備註
此份檔案可在更改小部分，使用word2vec對其他資料集進行分析，由於我已經把keywordPlot.py多數Input變數化，照理來說應該方便許多
