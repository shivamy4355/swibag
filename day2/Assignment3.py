#all touple question
tuplex = ("tuple", False, 3.2, 1)#q:1
touple with different datatype
print(tuplex)
print("length of tuple is:",len(tuplex))# q 1(II):finding touple length

#Q(A-2)smallest and largest element in tuple
a=(12,14,14,11,87,43,78)
print("smallest element is",min(a))
print("largest element is",max(a))
finding product of all element in tuple
result=1
for x in a:
    result=result*x
print("product of all element in tuple is: ",result)


#B-set questions
#1)	Create  two set using user defined values.
set1=set([1,2,3,4,5])
set2=set([3,4,5,6])
#calculate difference between two sets
print(set1.difference(set2))
#comparing two sets
print(set(set1)^set(set2))
#intersection in both set
print(set1&set2)

#question C -Dictionary
import operator
d={"shivam":80,"ashish":75,"sahil":90,"prince":50,"vinay":40}
#sorting dictionary according to marks
sorted_d = sorted(d.items(), key=lambda x: x[1])
print(sorted_d)
#3)	Count the number of occurrence of each letter in word "MISSISSIPPI".
#Store count of every letter with the letter in a dictionary
a="MISSISSIPPI"
b={'M':a.count('M'),'I':a.count('I'),'S':a.count('S'),'p':a.count('P')}
print(b)
