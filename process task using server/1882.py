import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = []
        busy = []
        ans = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        current_time = 0

        for i, duration in enumerate(tasks):

            current_time = max(current_time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= current_time:
                end, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:

                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    end, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Choose the server with minimum weight and index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Update server's finishing time
            heapq.heappush(
                busy,
                (current_time + duration, weight, index)
            )

        return ans
