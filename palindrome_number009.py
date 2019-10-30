'''
题目描述

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
class Solution:
    '''
    解法1：小于0返回False，大于等于0求倒转整数
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        cur = 0
        num = x
        while num != 0:
            cur = cur * 10 + num % 10
            num = int(num / 10)
        return cur == x

    '''
    解法2：将整数转换为字符串
    '''
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i = int(len(str(x))/2)
        for j in range(0,i):
            if x[j] == x[len(str(x))-j-1]:
                continue
            else:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))