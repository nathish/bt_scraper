## python 3.6 > ##
from bs4 import BeautifulSoup
import requests
import datetime
import re
import sys
import math

## validating arguments ##
if not len(sys.argv) > 2:
    print("usage: python bt_scrape.py {town or city} {surname}")

location = sys.argv[1]
surname = sys.argv[2]

## retrieving search request ##
dt = datetime.datetime.today()
date = dt.strftime("%d/%m/%y %H:%M:%S")
base = "https://www.thephonebook.bt.com"
URI = base+"/Person/PersonSearch/?Surname="+surname+"&Location="+location+"&Street=&PageNumber="
r = requests.get(URI)

soupy = str(BeautifulSoup(r.content, 'html.parser'))

## validating search results ##
pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)
if not pan:
    pan = re.findall(r'too many results', soupy)
    if pan:
        print('Too many results found')
    else:
        print('No match found in search result')
        exit()
    exit()

## calculating number of pages to scrape ##
srslts = str(re.findall(r'PeopleSearchResultsHomePage\((.*)\)\;', soupy))
srslts = srslts.replace("'","")
nrslts = int(srslts.split(',')[-2])
tpnum = nrslts / 25
tpnum = math.ceil(tpnum)

print("Name",",","Address",",","Post Code",",","Area",",","Phone Number",",","District",",","Distance from centre",",","Date")

## parsing results ##
for pnum in range(tpnum):
    r_1 = requests.get(URI+str(pnum+1))
    soup = BeautifulSoup(r_1.content, "html.parser")
    soupy = str(soup)
    pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)
    hob = int(pan[0].split('=')[1])
    spoon = str(soup.find_all("div", class_="mb-3 border border-dark px-3"))
    bowl = BeautifulSoup(spoon, 'html.parser')
    bowl = bowl.get_text()
    
    parse_0 = bowl.replace('[','').replace(']','')
    parse_1 = re.sub(r'(.+), (.+)', r'\1 \2', parse_0)
    parse_2 = parse_1.split(',')
    
    for i in range(hob):
        parse_3 = (parse_2[i])
        x = [line for line in parse_3.split('\n') if line.strip()]
        parse_4 = x[2].split(" ")
        y = parse_4[-2]+" "+parse_4[-1]
        z = x[2].replace(parse_4[-2],'').replace(parse_4[-1],'')
        
        print(x[0],',',x[1],',',y,',',z,',',x[4],',',parse_4[-2],',',x[7],',',date)
