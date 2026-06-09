
mylist = input("Enter a list of numbers separated by space: ")
mylist = list(map(int, mylist.split()))

total = 0
for num in mylist:
    total += num

print("The sum of the numbers is:", total)
