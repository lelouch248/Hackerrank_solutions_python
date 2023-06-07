# Normal non optimized code

def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    sum_array = [0] * n
    for i in range(n):
        for y in range(n):
            if i == y:
                continue
            else:
                sum_array[i] += arr[y]

    print(min(sum_array),max(sum_array))
    
    
    
  #optimized code 
  def miniMaxSum(arr):
    # Initialize variables for minimum and maximum sums
    min_sum = float('inf')
    max_sum = float('-inf')
    total_sum = 0

    # Calculate the total sum of the array
    for num in arr:
        total_sum += num

    # Calculate the minimum and maximum sums
    for num in arr:
        current_sum = total_sum - num
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)

    print(min_sum, max_sum)
