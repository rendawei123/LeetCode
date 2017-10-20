"""
Write a function to find the longest common prefix string amongst an array of strings.

题意：
求所有字符串的最长公共前缀，即数组的所有字符串都包含这个前缀。
普通循环遍历做法
"""



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = []
        judge = True

        if len(strs) == 0:
            return ''

        else:
            shorted = len(strs[0])

            for each in strs:
                if len(each) < shorted:
                    shorted = len(each)

            for i in range(shorted):
                if judge:
                    common.append(strs[0][i])
                    for each in strs:
                        if each[i] != common[-1]:
                            common.pop()
                            judge = False
                            break
                else:
                    break
            return ''.join(common)
            #return common

if __name__ == '__main__':
    strs = ['baca', 'bcba']
    #strs = []
    a = Solution()
    print(a.longestCommonPrefix(strs))
