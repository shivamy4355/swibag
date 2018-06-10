printData = {}
def func(name,age,phone,reg):
    a = (name,age,phone)
    printData[reg] =a
def commit():
    for i in printData:
       print("Reg: ",i,"\n",printData[i])
    name=input("Please Enter Your Name: ")
    age=input("Please Enter your Age: ")
    phone=input("Please Enter Your Contact No: ")
    reg=input("Please Enter your 8 digit Reg No: ")
    a={name:0,age:1,phone:2,reg:3}
    print(a)

commit()
