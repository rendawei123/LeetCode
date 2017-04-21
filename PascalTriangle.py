class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if not numRows:
            return result

        for i in range(numRows):

            if i == 0:
                result.append([1])
            else:
                result.append(self.nums(result[-1]))

        return result

    def nums(self, list1):
        list2 = []
        for i in range(len(list1) + 1):
            if i == 0 or i == len(list1):
                list2.append(1)
            else:
                list2.append(list1[i] + list1[i - 1])
        return list2

if __name__ == '__main__':
    n = 0
    a = Solution()
    print(a.generate(n))
