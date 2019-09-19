'''
Given below is a represenatation of a simple Browser which has three searching options i.e Bing,Ask.com and Flipkart.com.
It allows user to choose between 3 search engines and input the data that user want to search.
It displays the search results of the entered user input
'''


from bs4 import BeautifulSoup
import requests
import sys

class MyBrowser:

    def __init__(self,a):
        self.a = a

    def Bing_search(self):

        print('\nBing Search Engine ')
        search = input('\nBing Search : ')
        url = "https://www.bing.com/search?q="+ search +"&qs=n&form=QBLH&sp=-1&pq=&sc=0-0&sk=&cvid=14B0A43B798149C9AD28C4A5563B6599"

        response = None

        try:
            response = requests.get(url)
        except Exception as e:
            print(repr(e))
            sys.exit(1)

        if response.status_code != 200:
            print("Non success status code returned "+str(response.status_code))
            sys.exit(1)

        soup = BeautifulSoup(response.text,'html.parser')


        items = soup.find_all("li",{"class":"b_algo"})

        itemlist = []
        for item in items:
            text = item.text.encode('utf-8')
            itemlist.append(text)

        for itemtext in itemlist:
            print(itemtext)


    def Ask_search(self):

        print('\nAsk.com Search Engine ')
        inp = input('\nAsk.com Search : ')
        url = "https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q="+ inp

        response = None

        try:
            response = requests.get(url)
        except Exception as e:
            print(repr(e))
            sys.exit(1)

        if response.status_code != 200:
            print("Non success status code returned "+str(response.status_code))
            sys.exit(1)

        soup = BeautifulSoup(response.text,'html.parser')

        ress = soup.find_all("p",{"class":"PartialSearchResults-item-abstract"})

        reslist = []
        for res in ress:
            text = res.text.encode('utf-8')
            reslist.append(text)

        for restext in reslist:
            print(restext)

        
    def Flipkart_search(self):
        print('\nFlipkart Shopping Portal')
        search = input('\nProduct Search : ')
        url = "https://www.flipkart.com/search?q="+search+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        response = None

        try:
            response = requests.get(url)
        except Exception as e:
            print(repr(e))
            sys.exit(1)

        if response.status_code != 200:
            print("Non success status code returned "+str(response.status_code))
            sys.exit(1)

        soup = BeautifulSoup(response.text,'html.parser')

        prods = soup.find_all("div",{"class":"_3wU53n"})

        prodlist = []
        for prod in prods:    
            text = prod.text.encode('utf-8')
            prodlist.append(text)

        for prodtext in prodlist:
            print(prodtext)


print('\nWelcome to My Browser \nChoose any below options for Surfing \n1.Bing.com\n2.Ask.com\n3.Flipkart.com\n4.Exit Browser ')
a = int(input('\nEnter your Choice : '))
obj = MyBrowser(a)
if a == 1:
    obj.Bing_search()
elif a == 2:
    obj.Ask_search()
elif a == 3:
    obj.Flipkart_search()
else:
    print('\nInvalid Choice')



