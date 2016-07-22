##This script helps me download the latest manga releases of Bleach. If there are no new releases it shows me No new releases otherwise it notifies me that there is a new release and begins downloading by making a folder with the chapter name.
import requests,bs4
import re
import os.path
from gi.repository import Notify

Notify.init('bleach')

url='http://mangafox.me/manga/bleach/'

re=requests.get(url)

beautiful=bs4.BeautifulSoup(re.text,"lxml")

links=beautiful.select('h3 .newch')

#Getting the name of the chapter
chapname=beautiful.select('h3 .tips')[0].getText()

a=links[0].getText()

os.chdir('/home/shivesh/Desktop/bleach')

if os.path.isdir(chapname) is True:
 n=Notify.Notification.new("No New Chapter Released")
 n.show()                                       
 quit()															#Terminating the program if folder already exists i.e no new releases
 
if a=="new":
 n=Notify.Notification.new("New Chapter Released")
 n.show()                                       
 
 os.makedirs(chapname)
 
 url = 'http://mangafox.me/manga/bleach/vTBD/c683/1.html'
 
 re=requests.get(url)
 
 b=bs4.BeautifulSoup(re.text,"lxml")
 
 pages=b.select('.l')
 
 page_number=int(pages[0].getText()[len(pages[0].getText())-5:len(pages[0].getText())-3])
 
 for i in range(1,page_number+1):
  url = 'http://mangafox.me/manga/bleach/vTBD/c683/'+str(i)+'.html'
  res=requests.get(url)
  b=bs4.BeautifulSoup(res.text,"lxml")
  manga=b.select('#image')
  res2=requests.get(manga[0].get('src'))
  url2=manga[0].get('src')
  imageFile = open(os.path.join('/home/shivesh/Desktop/bleach/'+chapname, 'page'+str(i)), 'wb')
 
  for chunk in res2.iter_content(100000):
   imageFile.write(chunk)
  
  imageFile.close()
