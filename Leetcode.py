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
from typing import Counter


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
6. 三数之和

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
'''
7. 接雨水
困难
相关标签
相关企业
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

'''   
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3:
            return 0

        left_max = [0] * length
        right_max = [0] * length
        trap = 0

        for i in range(length):     
            left_max[i] = max(left_max[i - 1], height[i])    # 左侧最大值

        right_max[-1]=height[-1]    # 右侧最大值
        for i in range(length-2, -1, -1):    
            right_max[i] = max(right_max[i + 1], height[i])  

        for i in range(length):
            current_area = min(left_max[i], right_max[i])
            if height[i] < current_area:
                trap += current_area - height[i]

        return trap
        
'''
8. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。


示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
     
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # 字符集合，set()为创建一个不能重复元素的集合    
        left = 0
        max_length = 0

        for right in range(len(s)):
            # 如果字符在集合中，左指针右移，直到移除重复字符
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # 添加当前字符到集合中
            char_set.add(s[right])
            # 更新最长长度
            max_length = max(max_length, right - left + 1)

        return max_length 
    
#注释：本题的解法是滑动窗口法，即用两个指针left和right，分别指向窗口的左右边界，
# 大神总结滑动窗口·算法的步骤：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/3982/hua-dong-chuang-kou-by-powcai


'''
9. 找到字符串中所有字母异位词

给定两个字符串 s 和 p.找到 s 中所有p的异位词的子串,返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        


# 示例用法
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))  # 输出: [0, 6]



import sys
input = sys.stdin.read

def main():
    data = input().split()  # 读取输入数据，以空格为分隔符
    index = 0                    # 索引
    n = int(data[index])         # 读取数组长度
    index += 1                  # 索引+1
    vec = []                    # 数组
    for i in range(n):                     # 读取数组元素
        vec.append(int(data[index + i]))          
    index += n                 # 索引+数组长度

    p = [0] * n             # 前缀和数组
    presum = 0             # 前缀和
    for i in range(n):        # 计算前缀和
        presum += vec[i]           
        p[i] = presum              
    results = []                    # 结果数组
    while index < len(data):         # 读取查询区间
        a = int(data[index])            # 读取查询区间左端点
        b = int(data[index + 1])             # 读取查询区间右端点
        index += 2                     # 索引+2

        if a == 0:            # 左端点为0，则查询区间为整个数组
            sum_value = p[b]         # 计算前缀和
        else:
            sum_value = p[b] - p[a - 1]         # 计算前缀和

        results.append(sum_value)          # 结果数组添加前缀和值

    for result in results:      # 输出结果数组
        print(result)                # 输出结果


a=[0,4,26,40,45,50,51,52,53]
b=[0,5,15,40,60,70,73,74,75]
c=[0,5,15,40,80,90,95,98,100]
num=0
maxtotal=0
max_i, max_j, max_k = -1, -1, -1
for i in range(0,9):
    for j in range(0,9):
        for k in range(0,9):
            total=a[i]+b[k]+c[j]
            if(i+k+j==8):
                num+=1
                print((total),i,j,k)
                if total > maxtotal:  # 更新最大的总和及对应的 i, j, k
                    maxtotal = total
                    max_i, max_j, max_k = i, j, k
print(maxtotal,max_i,max_j,max_k)





'''
10:编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

#思路
这道题目看上去貌似一道数学问题，其实并不是！

题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！

正如：关于哈希表，你该了解这些！ (opens new window)中所说，当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。

所以这道题目使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止。

判断sum是否重复出现就可以使用unordered_set。

还有一个难点就是求和的过程，如果对取数值各个位上的单数操作不熟悉的话，做这道题也会比较艰难。

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True

            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num



    def div(self, n: int):    # 除法版本
        new_num = 0
        while n:
            r=n%10
            n=n//10
            new_num += r ** 2

        return new_num

ans = Solution().isHappy(19)
print(ans)