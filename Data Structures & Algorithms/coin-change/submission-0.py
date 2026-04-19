class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        result = 0
        q = deque([0])
        seen = [False] * (amount + 1)

        while q:
            result += 1
            for _ in range(len(q)):
                curr = q.popleft()
                for coin in coins:
                    next = curr + coin

                    if next == amount:
                        return result
                    if next > amount or seen[next]:
                        continue

                    seen[next] = True
                    q.append(next)

        return -1