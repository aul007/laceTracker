from bs4 import BeautifulSoup

def url_list(soup):
  count = 0
  i = 0
 
#gets the number of brands 
  for a in soup.findAll('a'):
    if 'brand' in a['href']:
      count = count + 1 
  
  return count

