"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

题意：
给一个整数行，迭代出帕斯卡三角形的第一个整数行

pascal's triangle的特点是第i+1行第j个元素为第i行第j个元素和第j-1个元素的和，当然头尾两个元素要特殊处理

解法：

nB法：
挨个进行判断处理，使用迭代的方法

递归法
先求出第n行，然后再递归从1到n
"""


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

    def getRow_1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        return self.row(self.getRow(rowIndex-1))

    def row(self, ahead):
        result = []

        for i in range(len(ahead) + 1):

            if i == 0 or i == len(ahead):
                result.append(1)
            else:
                result.append(ahead[i] + ahead[i-1])

        return result

if __name__ == '__main__':
    n = 5
    a = Solution()
    print(a.generate(n))
