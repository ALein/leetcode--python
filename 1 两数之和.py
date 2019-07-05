# D:\anaconda\envs\tensorflow\python
# _*_ coding:utf-8 _*_
"""
# Time: 2019/7/5  11:31
# Author: AL_Lein
1.两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例：
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
# 我直接用的暴力搜索法，第一个数开始遍历，查找位置在这个数后面 并且相加能得到target的数，
#  找到后就直接返回这两数的index
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return '没有相应答案'