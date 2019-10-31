'''
28.实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    '''
    暴力破解
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j<len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i-j+1
                j=0
        if j ==len(needle):
            return i-j
        else:
            return -1

        '''
        解法2：kmp算法
        https://blog.csdn.net/x__1998/article/details/79951598
        '''





haystack = "hello"
needle = "ll"

strStr = Solution()
print(strStr.strStr(haystack, needle))