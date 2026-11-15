class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 1
        odd = 0
        prefixSum = 0
        MOD = 10**9 + 7

        for a in arr:
            prefixSum += a

            if prefixSum % 2:
                odd += 1
            else:
                even += 1

        return (even * odd) % MOD