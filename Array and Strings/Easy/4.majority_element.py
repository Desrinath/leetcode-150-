'''169. Majority Element

Easy
Topics
premium lock icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?'''

#solution 1
a=[1,1,2,2,2]
count=0
can=0
for new in a :
    if count==0:
        can=new
        count=1
    elif can==new:
        count=count+1
    else:
        count=count-1
print(can)

#solution2
nums=[1,1,2,2,2]
s=0
e=len(nums)-1
nums.sort()

while s<=e:
    mid=(s+e)//2
    break
print(nums[mid])