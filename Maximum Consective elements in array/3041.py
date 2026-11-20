
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}
        answer = 0

        for number in nums:

            # Increase number by 1
            dp[number + 1] = max(
                dp.get(number + 1, 0),
                dp.get(number, 0) + 1
            )

            # Keep number unchanged
            dp[number] = max(
                dp.get(number, 0),
                dp.get(number - 1, 0) + 1
            )

            answer = max(answer, dp[number], dp[number + 1])

        return answer
