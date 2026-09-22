#function definition
def binary_search(arr,x,i,j):
  while i<=j :
    mid=i+(j-i)//2
    if arr[mid] == x :
      return mid
    elif arr[mid] < x :
      return binary_search(arr ,x ,mid+1,j)
    else :
      return binary_search(arr ,x,i,mid-1)
  return -1


#driver code
arr=[]
n=int(input('Enter the number of elements : '))
for i in range(n):
  ele=int(input("Enter the element :  "))
  arr.append(ele)
m=0
p=len(arr)-1
x=int(input('Enter the element to search : '))
#function calling
result = binary_search(arr,x,m,p)
if result != -1 :
  print("Target element is found at index ",result )
else :
  print("Element not found !!")
