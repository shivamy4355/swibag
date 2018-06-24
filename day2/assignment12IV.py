
#function which returns a/b
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
#if i will give the value of a,b then it will calculate the formula assigned to c
        #and will print vaule of calculated c
            
