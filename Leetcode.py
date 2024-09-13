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
