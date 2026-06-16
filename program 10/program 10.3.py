try:
    num=int(input("enter a number:"))
    result = 10 / num
except ValueError:
    print("Error:invalid input!please enter a valid number:")
except ZeroDivisionError:
    print("error:Divisio by Zero!")
else:
    print("result:",result)
        
