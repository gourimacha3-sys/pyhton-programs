try:
    X=int(input("enter a number upto 100:"))
    if X>100:
        raise ValueError(X)
except ValueError:
    print(X,"is out of allowed range")
else:
    print(X,"is within the allowed range")
