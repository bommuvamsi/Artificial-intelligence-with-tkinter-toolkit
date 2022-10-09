
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
  
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


output :-
    
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======================== RESTART: V:/matrix transpose.py =======================
[12, 4, 3]
[7, 5, 8]
