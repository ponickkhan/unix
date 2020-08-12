thislist = [1,2,3,4,5,6,7,8,9,10]

def rm_odd():
    for num in thislist:
     if (num%2)!=0:
        thislist.remove(num)
    print(thislist)



rm_odd()