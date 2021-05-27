#Solution of Question 3
#function getMaxLength return number of maximum consecutive  one’s
def getMaxLength(arr, n):
    count = 0 
    res = 0
    for i in range(0, n):
        if (arr[i] == 0):
            count = 0
        else:
            count+= 1 
            res = max(res,count) 
          
    return res
#Initialize list 
arr = [1, 1, 0, 0, 1, 0, 1, 
             0, 1, 1, 1, 1]
n = len(arr) 
print(getMaxLength(arr, n))
