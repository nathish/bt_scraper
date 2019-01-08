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
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-n','--name', help='Specify surname')
group.add_argument('-b','--business', help='Specify business type: e.g "Spanish Restaurants"')
group.add_argument('-f','--file', help='Specify file path')
args = vars(parser.parse_args())

## global variables ##
location = args['location']
surname = args['name']
business = args['business']
base = "https://www.thephonebook.bt.com"
columns = 'Name , Address , Post Code , Area , Phone Number , District , Distance from centre , Data Source, Date'

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
        parse_1 = re.sub(r'(.+), ', r'\1 ', parse_0)
        parse_2 = re.sub(r'(.+), (.+)', r'\1 \2 ', parse_1)
        parse_3 = re.sub(r'(.+), (.+), (.+)', r'\1 \2 \3 ', parse_2)
        parse_4 = parse_3.split(',')
    
        for i in range(hob):
            parse_5 = (parse_4[i])
            x = [line for line in parse_5.split('\n') if line.strip()]
            parse_6 = x[2].split(" ")
            y = parse_6[-2]+" "+parse_6[-1]
            z = x[2].replace(parse_6[-2],'').replace(parse_6[-1],'')
        
            print(x[0],',',x[1],',',y,',',z,',',x[4],',',parse_6[-2],',',x[7],', BT Phone Book,',date)

def bt_scrape_b():
    ## retrieving search request ##
    dt = datetime.datetime.today()
    date = dt.strftime("%d/%m/%y %H:%M:%S")
    URI = base+"/Business/BusinessSearch/?BusinessSearchType=bus&BusinessSearchTerm="+business+"&Location="+location+"&PageNumber="
    r = requests.get(URI)

    soupy = str(BeautifulSoup(r.content, 'html.parser'))
    pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)

    ## calculating number of pages to scrape ##
    srslts = str(re.findall(r'BusinessByTypeSearchResultsHomePage\((.*)\)\;', soupy))
    srslts = srslts.replace("'","")
    nrslts = int(srslts.split(',')[-2])
    tpnum = nrslts / 25
    tpnum = math.ceil(tpnum)

    ## parsing results ##
    for pnum in range(tpnum):
        r_1 = requests.get(URI+str(pnum+1))
        soup = BeautifulSoup(r_1.content, "html.parser")
        soupy = str(soup)
        pan = str(re.findall(r'BusinessByTypeSearchResultsHomePage\((.*)\)\;', soupy))
        pan = pan.replace("'","")
        hob = int(pan.split(',')[-2])
        spoon = str(soup.find_all("div", class_="mb-3 border border-dark d-none d-lg-block"))
        bowl = BeautifulSoup(spoon, 'html.parser')
        bowl = bowl.get_text()

        parse_0 = bowl.replace('[','').replace(']','')
        parse_1 = re.sub(r'(.+), ', r'\1 ', parse_0)
        parse_2 = re.sub(r'(.+), (.+)', r'\1 \2 ', parse_1)
        parse_3 = re.sub(r'(.+), (.+), (.+)', r'\1 \2 \3 ', parse_2)
        parse_3_5 = re.sub(r'(.+\S), (.+)', r'\1 \2 ', parse_3)
        parse_4 = parse_3_5.split(',')

        for i in range(25):
            parse_5 = (parse_4[i])
            x = [line for line in parse_5.split('\n') if line.strip()]
            parse_6 = x[2].split(" ")
            y = parse_6[-3]+" "+parse_6[-2]
            z = x[2].replace(parse_6[-4],'').replace(parse_6[-3],'').replace(parse_6[-2],'')
            print(x[0],',',z,',',y,',',parse_6[-4],',',x[-1],',',parse_6[-3],',',x[4],', BT Phone Book,',date)

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

elif args['business']:
     URI = base+"/Business/BusinessSearch/?BusinessSearchType=bus&BusinessSearchTerm="+business+"&Location="+location+"&PageNumber="
     r = requests.get(URI)
     soupy = str(BeautifulSoup(r.content, 'html.parser'))
     pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)
     if not pan:
         pan = re.findall(r'too many results', soupy)
         if pan:
             print('Too many results found: '+business)
         else:
             print('No match found in search results: '+business)
     else:
         print(columns)
         bt_scrape_b()

else:
    URI = base+"/Person/PersonSearch/?Surname="+surname+"&Location="+location+"&Street=&PageNumber="
    r = requests.get(URI)
    soupy = str(BeautifulSoup(r.content, 'html.parser'))
    pan = re.findall(r'TypeObject.numberResults(.*)\;', soupy)
    if not pan:
        pan = re.findall(r'too many results', soupy)
        if pan:
            print('Too many results found: '+surname)
        else:
            print('No match found in search results: '+surname)
    else:
        print(columns)
        bt_scrape()
