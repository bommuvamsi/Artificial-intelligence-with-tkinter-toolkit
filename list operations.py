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

output :-
    
 ======================== RESTART: V:/list operations.py ========================
[7, 8]
[7, 8, 6]
[7, 8, 6]
3
[7, 8, 6, 4, 5, 6]
