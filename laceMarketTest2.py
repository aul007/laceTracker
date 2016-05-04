from bs4 import BeautifulSoup
from probChars import clean
from brandUrls import url_list
import urllib2
import MySQLdb
import re

db = MySQLdb.connect("localhost","root","+r1t0n$k1k1b0uDiN", "laceDB")

cursor = db.cursor()
#cursor.execute("DROP TABLE IF EXISTS listing")
sql = """CREATE TABLE listing (
         id              int unsigned NOT NULL auto_increment,
         name            varchar(255) NOT NULL,
         currentPrice    decimal(10,2) NOT NULL,
         buyItNow        decimal(10,2) NOT NULL,

         PRIMARY KEY     (id)) """
#cursor.execute(sql)

def soup_open(url):
  req = urllib2.Request(url, headers = {'User-Agent' : "Magic Browser"}) 
  response = urllib2.urlopen(req)
  soup = BeautifulSoup(response.read(),"html.parser")
  return soup 

def get_data(url,soup):
  array = []
  entry = soup.find_all("li",{"class" : "greybg"})

  for i in range(len(entry)):
    name = entry[i].find_all("div",{"class": "data-box"}) 
    buyType = entry[i].find_all("p",{"class" : "currentp"})
    price = entry[i].find_all("p",{"class" : "currentpb"})

    for j in range(len(name)):
      n = name[j].a.contents
      n[j] = clean(n[j])

    for k in range(len(price)):
      kind = buyType[k].contents 
      kindp = price[k].contents
      temp = str(kindp) 
      intPrice = clean(temp)
      intPrice = intPrice.replace("u","")
      if k is 0:
        if str(kind) == "[u'current price']": 
          cp = kind 
          p = intPrice
          BIN = '\0'
          p2 = 0

        if str(kind) == "[u'Buy it Now']":
          BIN = kind
          p2 = intPrice 
          cp = '\0'
          p = 0 

      else:
        if str(kind) == "[u'current price']": 
          cp = kind 
          p = intPrice 
        if str(kind) == "[u'But it Now']":
          BIN = kind
          p2 = intPrice 
    
    try:
      cursor.execute("""INSERT INTO listing (name, currentPrice, buyItNow)VALUES(%r,%    s,%s)""",(n,p,p2))
      db.commit()
    except:
      db.rollback()
      print "error, couldnt add entry"
      print n 



def brand_urls(url2, brand_num, page_num):
  soup = soup_open(url2)
  page = brand_num
  brand_count = brand_num 
  length = url_list(soup)
  i = 0
  brand = [""]*length

  for a in soup.findAll('a'):
    if 'brand' in a['href']:
      brand[i] = a.get('href') #get url of first page of brand
      i = i+1

  for i in range(page, length):
      url = brand[i]
      page = 1 
      soup = soup_open(url)
      message = soup.find_all("div", {"align": "center"})
      '''  
      else:
        brand = url3
        page = page_num
        message = soup.find_all("div", {"align": "center"}) 
      '''
      message = soup.find_all("div", {"align": "center"}) 
      #while the page exists 
      while len(message) is 0:
        if brand_count is brand_num:
          if page < page_num:
            page = page_num
        url = brand[i] + "page/%d/" % page
        print url

        try: 
          soup = soup_open(url)
        except urllib2.HTTPError, e: 
          break

        soup = soup_open(url)
        get_data(url,soup)
        message = soup.find_all("div", {"align": "center"}) 
        if(len(message) is not 0): 
          print "page doesnt exist"
        page = page +1

      brand_count = brand_count + 1 
      print brand_count 
  return url
  
  return ""
def main():
  url2 = "http://www.lacemarket.us/"
  brand_num = 39
  page_num = 124
  brand_urls(url2,brand_num, page_num)

main()  
