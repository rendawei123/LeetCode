class Solution(object):
    def getRow(self, rowIndex):
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
    # list1 = [1, 2, 1]

    n = 4
    s = Solution()
    print(s.getRow(n))
    # print(s.row(list1))
