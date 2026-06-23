from array import*
arr=array("i",[10,20,30,40,50])
key=int(input("enter element to search:"))

if key in arr:
    print("elementfound")
else:
    print("element is not found")
