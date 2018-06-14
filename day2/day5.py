#extract integer from string and add them
#r = input("Enter any string with digit:")
#s = ''.join(x for x in r if x.isdigit())
#a = [int(x) for x in s]
#b=sum(a)
#j=[int(i) for i in str(b)]
#print(type(j))
#k=sum(j)
#print(k)
#*****************************************************
#finding min and max element from a list
#l=[2,3,6,4,7,8,1]
#min(l)
#max(l)
#abs(-455)changes negative  value to positive
#print all no divisible by 7 but not divisible by 5 
#l=[]
#for i in range (2000,3201):
    #if(i%7==0) and (i%5!=0):
        #l.append(str(i))
#print(l)
#def fact(x):
    #if(x==0):
        #return 1
    #else:
        #return x*fact(x-1)
#x=int(input())
##print(x)
#fact(int(input))
#conntecting github
#import requests
#import pprint as pprint
#r=requests.get("http://localhost:44314")
#pprint(r.text)
#r
#web scrapping  in python
#import bs4 as bs
#from pprint import pprint
#import urllib.request
#sauce=urllib.request.urlopen("https://www.instagram.com/mrinalraj").read()
#soup=bs.BeautifulSoup(sauce,'lxml')
#print(soup.title.text)
#for url in soup.find_all('meta'):
    #if url.get('property') == 'og:image':
        #print(url.get('content'))
