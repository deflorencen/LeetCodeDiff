

class Solution:
    @staticmethod
    def maximumWealth(accounts):
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth