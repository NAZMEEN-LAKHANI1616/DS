arr = [1, 6, 7, 19, 22, 100]; 

def linsearch(arr, n, x): 
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 
    return -1;
x = 19;
n = len(arr); 
result = linsearch(arr, n, x)
if(result == -1): 
    print("linear search:","Element is not present in array") 
else: 
    print("linear search:","Element is present at index", result);
def binarySearch(arr, l, r, x): 
    while l <= r: 
        mid = l + (r - l)//2; 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
X= 19; 
  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if(result != -1): 
    print("binary search:","Element is present at index % d" % result)
else: 
    print("binary search:","Element is not present in array")
