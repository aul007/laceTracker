# laceTracker

laceTracker.py parses [Lace Market](www.lacemarket.us) for the names and prices of all the listings shown on the site and stores the information in a database. It parses [Lace Market](www.lacemarket.us) by scraping the data from each page starting with the page specified by the user. The parser will move on to the pages of the next brand (in alphabetical order) once it has completed parsing all of the pages of the current brand.  

There are a few command line flags to be aware of (shown in parens) :

python laceTracker.py

The program will prompt you to enter a brand's index (brand_num) and the page number (page_num)
* `brand_num` - The index of the brand that you would like to start parsing at. (0 for 6% DOKIDOKI Acessory, 1 for Alice and the Pirates, etc)
* `page_num` - The page number that you would like to start parsing at. 

An example of use would be:

```
python laceTracker.py
>enter a brand number:
2
>enter a page number:
3
```
This will effectively run the program and start parsing from the first listing of third page of the brand Angelic Pretty. 
