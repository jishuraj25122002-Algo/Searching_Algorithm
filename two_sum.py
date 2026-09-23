#function calling 
def two_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return left, right
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1

    return -1, -1


# Driver code
arr = []
n=int(input("Enter the number of elements : "))
for i in range(n):
  ele=int(input("Enter the element for index :"))
  arr.append(ele)
target_sum =int(input('Enter the target sum value : '))

result = two_sum(arr, target_sum)
print(result)