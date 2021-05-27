def findMaximum(dict):
    newDict={}
    x=list(dict.values())
    k=list(dict.keys())
    key=(k[x.index(max(x))])
    newDict[key]=dict[key]
    return newDict
    
    
    return maximum
dict={'a':1,'b':2}
res=findMaximum(dict)
print(res)
    
    
