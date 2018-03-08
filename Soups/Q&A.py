#Rahul Goel
#February 3, 2018, Northwestern University IL
#IEMS 399: Scraping Q&A sections of given SeekingAlpha Links using BeautifulSoup

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import time

urllist=["https://seekingalpha.com/article/4124369-tyson-foods-tsn-q4-2017-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/4065635-united-therapeutics-uthr-q1-2017-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/4065635-united-therapeutics-uthr-q1-2017-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/4048383-united-therapeutics-uthr-q4-2016-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/4015845-united-therapeutics-uthr-ceo-martine-rothblatt-q3-2016-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3992756-united-therapeutics-uthr-ceo-martine-rothblatt-q2-2016-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3969086-united-therapeutics-uthr-ceo-martine-rothblatt-q1-2016-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3930476-united-therapeutics-uthr-martine-rothblatt-q4-2015-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3608636-united-therapeutics-uthr-martine-rothblatt-q3-2015-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3364525-united-therapeutics-uthr-ceo-roger-jeffs-on-q2-2015-results-earnings-call-transcript?part=single",
        "https://seekingalpha.com/article/3111056-united-therapeutics-uthr-ceo-martine-rothblatt-on-q1-2015-results-earnings-call-transcript?part=single"         
         ]


hdr = {'User-Agent': 'Mozilla/5.0'}

output=[]

for site in urllist:
    time.sleep(10) #delay
    req = Request(site, headers=hdr)
    sauce=urllib.request.urlopen(req).read()
    soup=bs.BeautifulSoup(sauce, 'lxml')
    start=soup.find("strong", text="Question-and-Answer Session").parent #Find the Q&A Secion
    

     
    output.append('----------- BEGIN TRANSCRIPT -------------')
    output.append('\n')
    output.append(soup.title.text)
    output.append('\n')
    output.append('\n') #Adding a return
    print(soup.title.string)
    for p in start.find_next_siblings("p"):
        output.append(p.text)
        output.append('\n')
                
                
    
    
       
#Write files to txt file, you can name this anything you want

with open('/users/rahulgoel/Desktop/Q&A.txt', 'w') as f:
    for line in output:
        f.write(line)
        
