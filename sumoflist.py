def sum(arr):
	sum=0
	for i in range((len(arr))):
		sum+=arr[i]
	return sum
arr=[1,2,3,4,5]
res=sum(arr)
print("Sum of list is {}".format(res))
