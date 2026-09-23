def findmaxprofit(prices):
  min_price = float('inf')
  max_profit = 0


  for i in range(len(prices)):
    if prices[i] < min_price :
      min_price = prices[i]
    elif prices[i] - min_price > max_profit :
      max_profit = prices[i] - min_price 
  return max_profit        


#driver code 
prices = []
n=int(input("Enter the number of elements : "))
for i in range(n):
  ele=int(input("Enter the elements : "))
  prices.append(ele)
#function calling
max_profit=findmaxprofit(prices)
print("the maximum profit of buy and sell the stock is :" , max_profit)  