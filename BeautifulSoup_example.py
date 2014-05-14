'''這個範例是由  http://programminghistorian.org/lessons/intro-to-beautiful-soup 中所取得的
   很簡明的說明了進行網路爬蟲的流程
   簡單的來說：將網頁整個結構給捉下來→把不要的部分給刪掉→只保留下你想要的部份→輸出成csv檔案
   其中'a'與'p'都是html的基本元素 'a'指的是超連結 'p"指的是段落
   而'td' 'th' 'tr'都是屬於表格相關的元素
   
   另外因為網頁結構並沒有明確限制，所以常常有意外的狀況發生
   像是本例中原始表格就有3個是沒有資料可以輸出的
   所以也介紹了在python中要如何處理 
   try:  
   
   except:
   
'''

from bs4 import BeautifulSoup
import csv
 
soup = BeautifulSoup (open("43rd-congress.html"))
 
final_link = soup.p.a
final_link.decompose()
 
f= csv.writer(open("43rd_Congress_all.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["Name", "Years", "Position", "Party", "State", "Congress", "Link"]) # Write column headers as the first line
 
trs = soup.find_all('tr')
 
for tr in trs:
    for link in tr.find_all('a'):
        fullLink = link.get ('href')
 
    tds = tr.find_all("td")
 
    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()
 
    except:
        print "bad tr string"
        continue #This tells the computer to move on to the next item after it encounters an error
 
    f.writerow([names, years, positions, parties, states, congress, fullLink])
