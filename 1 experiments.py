def find_all_indexes(numbers, key):
   arr = sorted(numbers)  # dont use numbers.sort() as it returns none it js sorts it and stores 
   low , high = 0 , len(arr)-1 
   result = []
   while low <= high :
      mid = (low + high)//2
      if arr[mid] == key :
         left = mid 
         while left >= 0 and arr[left] == key : # dont use arr[left] >= 0 as it chacks the value not the index
            result.append(left)
            left -= 1
            
         right = mid+1  #define right after left scan finished not in its loop as it keeps getting rested 
         while right < len(arr) and arr[right] == key:
               result.append(right)
               right += 1 

         return sorted(result)
            
      elif arr[mid] < key :
         low = mid + 1
      else : 
         high = mid - 1          
   


print((find_all_indexes([10,4,5,3,3,8,11,3,4,1,2],3)))


if __name__ == "__main__":
    data = [1, 3, 5, 8, 9, 12, 15]
    x = int(input("Enter number to search: "))
    result = find_all_indexes(data, x)

    if result != -1:
        print(f"Found at index  {result}")
    else:
        print("Not found")









