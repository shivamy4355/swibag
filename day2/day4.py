#l=[1,2,3,4]
#l.append(4)
#a=[7,8,9]
#l.append(a)#adds nested list in a
#l.extend([3,5,7])#to add more element row
#l+[10,11,12]
#l.insert(0,0)#add 0 from 0th index
#l.pop()#delets laste element of list
#l.pop(1)#delete 1st index from the list if there are duplicate element i will only remove 1 element
#l.clear#to empty the list
#l.sort()#sort the list
#l.sort(reverse=True)#sort in reverse order
#l[-1::-1]#do the same in revese order
#a=[1,2,3]
#b=a#copy element
#b==a#check if true or not
#c=b.copy#copy the element of b  in case of change in b c will not be changed
#b[1]=3#change  the element in b
#print a# it will also be changes when you changed b
#d=c.copy()
#d==c#will print true
#d is c # will print false because it is not actually copy
#1st method to print square of up to 10 element in list
#a=[0,1,2,3,4,5,6,7,8,9,10]
#for i in range(len(a)):
    #a[i]=i*i
    #print(a[i])
#2nd method to print square of up to 10 element in list
#print([i**2 for i in range(10)])
#check if else
#a=10
#if a>10:
    #print("ïf block")
#elif a==10:
    #print("elif block")

#else:
          #print("else bloc

#show grade as per marks
#a=input("plese enter your name:")
#b=int(input("enter your marks"))
#if b>=81 and b<=100:
    #print("Your grade is A+")
#elif b>=70 and b<=80:
    #print("grade is a")
#2nd method
#l=[]
#for i in range(int(input("How many student data you wan to enter:\n"))):
    #a=input("Enter Name:\n")
    #b=int(input("Enter marks:\n"))
    #grade=''
    #if b>=81 and b<=100:
          #grade="A+"
    #elif b>=70 and b<=80:
          #grade="A"
    #else:
          #grade="R"
    #l.append([a,grade])
    #print(l)
#print ascii value
#ord("a")
#chr(97)
#to print a-z ascii character value
#a='abcdefghijklmnopqrstuvwxyz'
#l=list(a)
#for i in l:
    #print(ord(i))
#2nd method
#import string
#for i in string.ascii_lowercase:
       #print(ord(i))
#n=1,2,3,4,5
#m=['a','b','c']
#print([[n[0],m[0]],[n[0],m[1]],[n[0],m[2]],[n[1],m[0]],[n[1],m[1]]])random way to do it
#[print([i,j]) for i in [1,2,3,4,5] for  j in ['a','b','c']]
#output
#[1, 'a']
#[1, 'b']
#[1, 'c']
#[2, 'a']
#[2, 'b']
#[2, 'c']
#[3, 'a']
#[3, 'b']
#[3, 'c']
#[4, 'a']
#[4, 'b']
##[4, 'c']
#[5, 'a']
#[5, 'b']
#[5, 'c']
#l=[x for x in range(0,20)if x%2==0]
#output
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#print(l)
#dict_comp={x:chr(65+x)for x in range(1,11)}
#print(dict_comp)
#output:{1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K'}
#set_comp={x**3 for x in range(10) if x%2==0}
#print(set_comp)
#output:{0, 64, 512, 8, 216}
#hasattr(str,'__iter__')#if  sr=tring method have iter method it will return true else false
#list comprihence and generator expression
#from sys import getsizeof
#my_comp=[x*5 for x in range(1000)]
#my_gen=(x*5 for  x in range(100))
#print(getsizeof(my_comp))
#print(getsizeof(my_gen))


