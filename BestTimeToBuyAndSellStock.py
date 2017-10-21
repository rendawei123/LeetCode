"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


题意理解

题目的意思是整个过程中只能买一只股票然后卖出，也可以不买股票。也就是我们要找到一对最低价和最高价，最低价在最高价前面，以最低价买入股票，以最低价卖出股票。


解法：
循环遍历价格列表，先取得最小的价格
然后用当前价格减去最小价格，保存价格差
然后获取最大的价格差
"""



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


    #  简单解法
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        most_profit = 0

        for i in range(len(prices) - 1):
            most_profit += max(prices[i + 1] - prices[i], 0)

        return most_profit

if __name__ == '__main__':
    b = []
    c = [5, 3, 1]
    a = [3, 5, 2, 1, 4]
    s = Solution()
    print(s.maxProfit(c))
