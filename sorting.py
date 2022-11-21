print('Bubble sort')
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = temp


nums = [5,3,8,6,7,2]
sort(nums)
print(nums)

print('Selection sort')
def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        
nums = [5,3,8,6,7,2]
sort(nums)
print(nums)

