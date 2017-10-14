"""
最大价格差
跟解法1y一样，只是这个是简单解法
"""





class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        most_profit = 0

        for i in range(len(prices) - 1):
            most_profit += max(prices[i + 1] - prices[i], 0)

        return most_profit

if __name__ == '__main__':
    p = [2, 7, 4, 2, 5]
    p1 = []
    s = Solution()
    print(s.maxProfit(p1))
