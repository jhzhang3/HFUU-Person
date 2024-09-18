#力扣刷题，主要可以智能填充代码模板，快速刷题。

'''
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()  # 哈希表
        for i, num in enumerate(nums):  # 枚举数组
            if target - num in hashtable:            # 如果哈希表中存在目标值减去当前值，则找到了
                return [hashtable[target - num], i]  # 返回下标
            hashtable[nums[i]] = i  # 哈希表中添加当前值和下标
        return []         # 如果没有找到，返回空列表
                
'''
2. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]
输出: [0]
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left=0
        right=1
        while right<n:
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1    
        return nums


'''
3. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == []:
            return [[]]
        hashtable={}
        for str in strs:  # 枚举字符串
            i=''.join((sorted(str)))  # 排序字符串，得到字母异位词
            if i in hashtable:  # 如果哈希表中存在该字母异位词，则添加到该字母异位词的列表中
                hashtable[i].append(str)   
            else :
                hashtable[i]=[str]  # 否则，创建该字母异位词的列表
        return list(hashtable.values())  # 返回哈希表中所有值（即字母异位词的列表）


'''
4.最长连续序列

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入:nums = [100,4,200,1,3,2]
输出:4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2:
输入:nums = [0,3,7,2,5,8,4,6,0,1]
输出:9
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)  # 转换为集合，去除重复元素
        max_lenth =0
        for num in num_set:  # 枚举集合
            if num - 1 not in num_set:  # 如果当前值-1不存在，则创建新的连续序列
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:  # 枚举连续序列
                    current_num += 1
                    current_length += 1
                max_lenth = max(max_lenth, current_length)  # 更新最大长度
        return max_lenth    



'''
5.盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2:

输入:height = [1,1]
输出:1

'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前容量
            current_area = min(height[left], height[right]) * (right - left)
            # 更新最大容量
            max_area = max(max_area, current_area)
            # 移动指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


'''
15. 三数之和

提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 .

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 先对数组进行排序
        result = []
        length = len(nums)
        if length<3:
            return []
        
        for i in range(length):
            # 避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, length - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1  # 增加较小的值
                elif current_sum > 0:
                    right -= 1  # 减小较大的值
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 避免重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result
    
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        length = len(nums)
        if nums==[]:
            return []
        for i in range(length):
            if i >0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,length-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if current_sum<0:
                    left+=1
                elif current_sum>0:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+= i 
                    right-= i 
        return result                                               