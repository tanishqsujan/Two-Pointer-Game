#find if there is a pair in a[0..n-1] with given sum
#using two pointer technique
def ispair(a,n,x):
    i=0
    j= n-1
    while(i<j):
        if (a[i] + a[j] == x):
            return a[i], a[j]
        
        elif(a[i] + a[j] < x):
            i += 1
            
        else:
            j -= 1
    return 0

arr= [2,3,5,8,9,10,11]
val= 17

print("Pairs with sum equal to {} - {}".format(val, ispair(arr,len(arr),val))) 