


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Step 1: Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        pos_of = {v: i + 1 for i, v in enumerate(vals)}
        rk = [pos_of[v] for v in nums]

        # Step 2: Fenwick Trees
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        top = 1
        while top * 2 <= m:
            top *= 2

        need = (x + 1) // 2
        w = n - x + 1
        cost = [0] * w

        total = 0

        # Step 3: Calculate the cost of every window
        for i in range(n):
            v = nums[i]
            total += v

            p = rk[i]
            while p <= m:
                cnt[p] += 1
                sm[p] += v
                p += p & -p

            # Remove the element outside the sliding window
            if i >= x:
                u = nums[i - x]
                total -= u

                p = rk[i - x]
                while p <= m:
                    cnt[p] -= 1
                    sm[p] -= u
                    p += p & -p

            # Calculate median and cost
            if i >= x - 1:
                pos = 0
                rem = need
                s0 = 0
                pw = top

                while pw:
                    nxt = pos + pw

                    if nxt <= m and cnt[nxt] < rem:
                        pos = nxt
                        rem -= cnt[nxt]
                        s0 += sm[nxt]

                    pw >>= 1

                med = vals[pos]
                c0 = need - rem

                cost[i - x + 1] = (
                    med * c0 - s0
                    + (total - s0) - med * (x - c0)
                )

        INF = 1 << 60

        prev = [0] * (n + 1)

        for _ in range(k):
            cur = [INF] * (n + 1)

            for i in range(x, n + 1):
                # Choice 1: Skip the current position
                a = cur[i - 1]

                # Choice 2: Select a window of length x
                b = prev[i - x] + cost[i - x]

                cur[i] = min(a, b)

            prev = cur

        return prev[n]

