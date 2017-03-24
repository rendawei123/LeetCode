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


