'''
best time to buy and sell
'''



from typing import List

class BestTime:

    '''
    You are given an array prices where prices[i] is
    the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
    '''
    @staticmethod
    def greedy(prices: List[int]) -> int:
        '''
        greedy algorithm: nested for loop
        complexity: O(N + N*logN)
        '''
        max_profit = (0,0)
        for m in range(0, len(prices)-1):
            buy = prices[m]
            for n in range(buy+1, len(prices)):
                sell = prices[n]
                if (sell-buy) > (max_profit[1]-max_profit[0]):
                    max_profit = (buy, sell)
        return max_profit[1]-max_profit[0]

    @staticmethod
    def min_max(prices: List[int]) -> int:
        '''
        split nums into two arrays for min-arr and max-arr
        maximize the gap 
        complexity: O(N)
        '''
        max_profit = 0
        for i in range(1, len(prices)):
            min_price = min(prices[:i])
            max_price = max(prices[i:])
            price_gap = (max_price - min_price)
            if  price_gap > max_profit:
                max_profit = price_gap
        return max_profit

    '''
    You are given an integer array prices where prices[i]
    is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock.
    You can only hold at most one share of the stock at any time.
    However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.
    '''

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        max_profit = 0 
        for i in range(2, len(prices)):
            # sell and buy may be the same day
            profit = BestTime.min_max(prices[:i]) + \
                    BestTime.min_max(prices[i-1:])
            if profit > max_profit:
                max_profit = profit
        return max_profit