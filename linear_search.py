#function definition
def linear_search(arr,x):
  for i in range(len(arr)):
    if arr[i]==x:
      return i
  return -1  

#driver code
arr=[]
n=int(input('enter the number of elements : '))
for i in range(n):
  ele=int(input('Enter the element : '))
  arr.append(ele)

x=int(input('enter the number to search : '))

#function calling 
result=linear_search(arr,x)

if result !=-1:
  print("Searching element is present at index :" , result )
else:
  print("Element not found ")  