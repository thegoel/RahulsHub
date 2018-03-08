#Rahul Goel
#February 3, 2018, Northwestern University IL
#IEMS 399: Scraping NEOG Q&A sections of given SeekingAlpha Links using BeautifulSoup

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import time

urllist=["https://seekingalpha.com/article/4144778-tyson-foods-tsn-q1-2018-results-earnings-call-transcript?part=single",
         ]

hdr = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'}

output1=[]
output2=[]
output3=[]

for site in urllist:
    req = Request(site, headers=hdr)
    sauce=urllib.request.urlopen(req).read()
    soup=bs.BeautifulSoup(sauce, 'lxml')
    start=soup.find("strong", text="Question-and-Answer Session").parent
    for p in start.find_next_siblings("p"):
        output1.append(p.text)


    
 #   for item in start.findAll("strong", text="Thomas P. Hayes - Tyson Foods, Inc."):
#        print(item.find_next('p'))
   

   
    for item in soup.findAll("strong", text="Thomas P. Hayes - Tyson Foods, Inc."):
        output2.append(item.find_next('p').text)
        
output3=list(set(output1) & set(output2))
print(output3)
  
