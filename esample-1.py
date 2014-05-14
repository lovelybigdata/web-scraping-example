
from bs4  import BeautifulSoup
'''這個寫法是固定的 只要你是使用 BeautifulSoup4 就是這樣寫
網路上有些比較早期的教學就不是這樣
要記得自己改過來
'''


html = "<p><b>Test</b></p>" 
'''html文件也可以直接用這樣方式表示作為範例
   反正只是範例檔
   而且這個範例的好處是你可以發現 html 真的是一種要求很不嚴格的標準
   最後輸出的結果如下
   但是一開始並沒有特別指令 <html> 與 <body>

<html>
 <body>
  <p>
   <b>
    Test
   </b>
  </p>
 </body>
</html>

'''
soup = BeautifulSoup(html)
'''將解析後的結果放進soup中'''

b_tags = soup.findAll('b')
'''會顯示出  [<b>Test</b>] '''

print soup.prettify ( )

print b_tags 
'''使用 prettyify()進行資料輸出
這個指令的好處是可以將html資料的型式，用縮排的方式顯示出來
方便開發人員觀察資料格式
'''

