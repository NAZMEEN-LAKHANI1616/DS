random_list_of_nums = [9, 1, 15, 28, 6]
def bubble_sort(nums):
  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
               
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
                swapped = True
bubble_sort(random_list_of_nums)
print("bubble sort:",random_list_of_nums)

def insertion_sort(nums):
    
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        
        j = i - 1
       
        
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = item_to_insert
insertion_sort(random_list_of_nums)
print("insertion sort:",random_list_of_nums)

def selection_sort(nums):
    
    for i in range(len(nums)):
        
        lowest_value_index = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        
        
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
selection_sort(random_list_of_nums)
print("selection sort:",random_list_of_nums)
