## python 3.6 > ##
from bs4 import BeautifulSoup
import requests
import datetime
import re
import sys
import math
import argparse

## validating arguments ##
parser = argparse.ArgumentParser(description='BT Phone Book to CSV web scraper')
parser.add_argument('-l','--location', help='Specify location', required=True)
parser.add_argument('-n','--name', help='Specify surname', required=False)
parser.add_argument('-f','--file', help='Specify file path', required=False)
args = vars(parser.parse_args())

## global variables ##
location = args['location']
surname = args['name']
base = "https://www.thephonebook.bt.com"
columns = 'Name , Address , Post Code , Area , Phone Number , District , Distance from centre , Date'

def bt_scrape():
    ## retrieving search request ##
    dt = datetime.datetime.today()
    date = dt.strftime("%d/%m/%y %H:%M:%S")
    URI = base+"/Person/PersonSearch/?Surname="+surname+"&Location="+location+"&Street=&PageNumber="
    r = requests.get(URI)

    soupy = str(BeautifulSoup(r.content, 'html.parser'))
    pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)

    ## calculating number of pages to scrape ##
    srslts = str(re.findall(r'PeopleSearchResultsHomePage\((.*)\)\;', soupy))
    srslts = srslts.replace("'","")
    nrslts = int(srslts.split(',')[-2])
    tpnum = nrslts / 25
    tpnum = math.ceil(tpnum)

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

if args['file']:
    filepath = args['file'] 
    with open(filepath) as fp:  
        print(columns)
        for line in fp:
            surname = line
            URI = base+"/Person/PersonSearch/?Surname="+surname+"&Location="+location+"&Street=&PageNumber="
            r = requests.get(URI)
            soupy = str(BeautifulSoup(r.content, 'html.parser'))
            pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)
            if not pan:
                pan = re.findall(r'too many results', soupy)
                if pan:
                    print('Too many results found: '+surname)
                    continue
                else:
                    print('No match found in search results: '+surname)
                    continue
            bt_scrape()
else:
    print(columns)
    bt_scrape()