'''
551. 学生出勤记录 I

给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False
'''


class Solution:
    '''
    遍历
    计数
    '''
    def checkRecord1(self, s: str) -> bool:
        a, l = 2, 3
        for c in s:
            if c == 'A':
                a -= 1
            if c == 'L':
                l -= 1
            else:
                l = 3
            if a == 0 or l == 0:
                return False
        return True

    def checkRecord2(self, s: str) -> bool:
        a, l = 0, 0
        for c in s:
            if c == 'A':
                a += 1
            if c == 'L':
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True

    def checkRecord3(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s


s1 = 'LLALLL'
s = Solution()
print(s.checkRecord1(s1))
print(s.checkRecord2(s1))
