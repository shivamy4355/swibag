
##file=open('abcd.txt','w')
#file.write("hi this is python bla bla")
#print(file.seek(0))
#file.write("hi")
#print(file.read())
#file.close()
#with open("abcd.txt",'w+')as file:
    #file.write("shivam")class Node:
import requests
r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

with open('events.txt','w') as fd:
    fd.write(r.text)
