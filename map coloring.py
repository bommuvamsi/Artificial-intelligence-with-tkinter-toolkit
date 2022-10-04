def addColor(R, province, color):
    ans = []
    for rr in R:
        res = checkRestriction(rr, province, color)
        if res == False:
            return False
        elif res == None:
            continue
        else:
            ans.append(res)
    return ans
def checkRestriction(rr, province, color):
   
    index = -1
    other = -1
    if rr[0] == province:
        index = 0
        other = 1
    elif rr[1] == province:
        index = 1
        other = 0
    else:
        return rr

    if isinstance(rr[other], int):
      
        if (color != rr[other]):
            return None
        else:
            return False
    else:
        return [rr[other], color]



def solveCSP(provinces, n, R, ci):
    if (ci == 0):
        
        newR = addColor(R, provinces[0], 1)
        if (newR == False):
            return False
        ans = {provinces[0]:1}
        res = solveCSP(provinces, n, newR, 1)
        if (res == False):
            return False
        ans.update(res)
        return ans
    elif (ci == len(provinces)):
        return {}

   
    for color in range (1,n+1):
        ans = {provinces[ci]:color}
        newR = addColor(R, provinces[ci], color)
        if (newR == False):
            continue
        res = solveCSP(provinces, n, newR, ci+1)
        if (res == False):
            continue
       
        ans.update(res)
        return ans

    
    return False
n=5
colors=[]
for i in range(1,n+1):
    colors.append(i)
 
cmap = {}
cmap["ab"] = ["bc","nt","sk"]
cmap["bc"] = ["yt", "nt", "ab"]
cmap["mb"] = ["sk","nu","on"]
cmap["nb"] = ["qc", "ns", "pe"]
cmap["ns"] = ["nb", "pe"]
cmap["nl"] = ["qc"]
cmap["nt"] = ["bc", "yt", "ab", "sk", "nu"]
cmap["nu"] = ["nt", "mb"]
cmap["on"] = ["mb", "qc"]
cmap["pe"] = ["nb", "ns"]
cmap["qc"] = ["on", "nb", "nl"]
cmap["sk"] = ["ab", "mb", "nt"]
cmap["yt"] = ["bc", "nt"]

R = []

for x in cmap:
    for y in cmap[x]:
        R.append([x,y])

provinces = []
for p in cmap:
    provinces.append(p)

while(1):
    num=int(input("Enter number of the color? "))
    print(solveCSP(provinces, num, R, 0))

output :-
    
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: V:\map coloring.py =========================
Enter number of the color? 3
{'ab': 1, 'bc': 2, 'mb': 1, 'nb': 1, 'ns': 2, 'nl': 1, 'nt': 3, 'nu': 2, 'on': 2, 'pe': 3, 'qc': 3, 'sk': 2, 'yt': 1}
Enter number of the color? 1
False


