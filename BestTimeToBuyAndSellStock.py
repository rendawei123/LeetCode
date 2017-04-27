class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

if __name__ == '__main__':
    b = []
    c = [5, 3, 1]
    a = [3, 5, 2, 1, 4]
    s = Solution()
    print(s.maxProfit(c))
