'''
345. 反转字符串中的元音字母

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
'''

class Solution:
    '''
    双指针
    使用双指针，一个指针从头向尾遍历，一个指针从尾到头遍历，当两个指针都遍历到元音字符时，交换这两个元音字符。
    java可以使用hashset检查元音字母：https://www.jianshu.com/p/f6f514e3def8
    '''

    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        result = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1
        return ''.join(result)


s1 = 'leetcode'
s = Solution()
print(s.reverseVowels(s1))
