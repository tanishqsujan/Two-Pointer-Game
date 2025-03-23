def small(num, left= None, right= None):
    #initiate left and right
    if left is None and right is None:
        (left, right)= (0, len(num) - 1)
        
    #base condition
    if left > right:
        return left
    
    mid= left + (right - left)//2
    
    #if the mid index matches with its value then the mismatch lies on the right half
    if(num[mid] == mid):
        return small(num, mid + 1, right)
    
    #mismatch lies on the left half
    else:
        return small(num, left, mid - 1)
    
if __name__ == '__main__':
    num= [0,1,2,6,9,11,15]
    print("The smallest missing element is: ", small(num))
