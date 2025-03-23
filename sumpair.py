def pairsum(a,n,x):
    for i in range(n): 
        for j in range(n):
            if (i==j):
                continue
            
            if(a[i] + a[j] ==x):
                return a[i], a[j]
            
            if(a[i] + a[j] > x):
                break
    return 0

arr= [2,3,5,6,9,11,14]
val= 17

print("Pairs with sum equal to {} - {}".format(val, pairsum(arr,len(arr),val)))  