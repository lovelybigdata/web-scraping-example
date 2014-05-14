#這邊有一些用到比較老的語法  參考就好

import urllib2
import csv
from bs4 import BeautifulSoup
url = "http://www.malegislature.gov/People/Senate"
page = urllib2.urlopen(url).read( )
soup = BeautifulSoup(page)
a_tags = soup.findAll ('a' , attrs={"title":True}) 

''' title 這個應該是網站自行定義的屬性 
　　直接指定回傳這些資料
　　在開發的過程中，可以直接用互動交談介面 下達 soup 觀察一下網站的結構
或是  soup.prettify() '''
 

for tag in a_tags :
  
    if '/People/Profile/KAO0' in  tag['href'] :
        print 'YES'


''' Python 就連寫註釋的時候也要對齊哦

   print tag['href'] 用這個語法會列出網站中
   超連結的內容 那個網站的超連結內容全部是以相對目錄的方式列出 
     如果要找一個超連結的值剛好是等於　'/People/Profile/KAO0'
    記得要搭配的是 in 的語法   


     # '/People/Profile/KAO0' in  tag['href'] :  #

 '''

links ={} 

'''
建立一個list用來儲存網址
'''
for tag in a_tags :
  
    if 'People' in  tag['href'] :
        links[tag['title']]=tag['href']

'''
這裡要用的語法是 links[tag['title']]=tag['href'] 這樣才會存入多筆資料
這樣的語法輸出的格式就會是  title href
'''

print links


'''這次一樣把整個表格給捉下來試試看

'''

f= csv.writer(open("my_example2.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["Name",	"Photo" ,	"Party"	,"Room"	,"Phone Number" ,	"Email Address" ]) # Write column headers as the first line

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fullLink = link.get ('href')
 
    tds = tr.find_all("td")
 
    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        Photo = str(tds[1].get_text())
        Party = str(tds[2].get_text())
        Room = str(tds[3].get_text())
        PhoneNumber = str(tds[4].get_text())
        EmailAddress = str(tds[5].get_text())
       
 
    except:
        print "bad tr string"
        continue #This tells the computer to move on to the next item after it encounters an error
 
    f.writerow([names,Photo, Party,Room, PhoneNumber, EmailAddress])
