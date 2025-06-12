

class Solution(object):
    @staticmethod
    def runningSum(nums):
        result = []
        current_sum = 0
        for num in nums:
            current_sum += num
            result.append(current_sum)

        return result


s = Solution()
print(s.runningSum([1, 3, 5, 7]))