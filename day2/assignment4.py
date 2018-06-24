##Question no:1 Take an input year from user and decide whether it is
#a leap year or not.
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

#question no:2 Take length and breadth input from user and check whether
 #the dimensions are of square or rectangle.
length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
if length==breadth:
            print("Given dimensions are of square")
else:
            print("Given dimensions are of rectangle")


 #question no:3 Take the input age of 3 people and
 #determine oldest and youngest among them
first=int(input("Enter  age of 1st person:"))
second=int(input("Enter age of 2nd person"))
third=int(input("Enter age of 3rd person"))
if first<second and first<third:
    print("First person is younger")
elif second<first and second<third:
    
    print("2nd person is younger")
elif third<first and third<second:
    
    print("Third person is younger")
elif first==second or second==third or first==third:
    print("All are of same age")
else:
    print("cant tell")


#question no4:
for i in range(1,200):
    i=int(input("Enter your point:"))
    if i>=1 and i<=51:
        print("Sorry!No prize this time")
        break
    elif i>=52 and i<=150:
        print("Congratulations1 You have won a wooden dog")
        break
    elif i>=152 and i<=180:
        print("Congratulations1 You have won a  Book")
        break
    else:
        print("Invalid point entered")
        break


#Question no :5
a=float(input("Please Enter quantity to get bill:="))

if a<1000:
    print("No discount available!your bill is:",a*100,"Rs")
elif a>=1000:
    b=a*100
    c=10/100*b
    d=b-c
    print("congratulations you got 10% discount,you current bill is:",d,"Rs")
    
