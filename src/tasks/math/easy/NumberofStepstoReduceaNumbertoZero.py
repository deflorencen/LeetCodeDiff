

class Solution:
    @staticmethod
    def numberOfSteps(num):
        step_count = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            step_count += 1
        return step_count