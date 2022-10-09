myList=[]
for i in range(7, 9):
    myList.append(i)
print(myList)
myList.insert(5, 6)
print(myList)
print(myList[:4])
print(len(myList))
myList.extend([4, 5, 6])
print(myList)
