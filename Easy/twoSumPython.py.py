# two sum
nums = [4, 7, 2, 15]
target = 9
t = []
temp = 0
"""
add nums[0] + nums[1]
add nums[1] + nums[2]

"""
"""
i = 0
while temp != target and i < len(nums) - 1:
    if nums[i] and nums[i + 1] < target:
        temp = nums[i] + nums[i + 1]

        if temp == target:
            t.append(i)
            t.append(i + 1)
        else:
            t = []
            temp = 0
    i += 1
"""


for index, num1 in enumerate(nums):
    for index2, num2 in enumerate(nums):
        temp = num1 + num2
        if temp != target:
            temp = 0
        elif temp == target and index != index2:
            t.append(index2)
            t.append(index)
            # return t
# O(n^2) worst time

for te in t:
    print(te)
