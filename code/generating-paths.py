  
from queue import PriorityQueue
import bisect
import sys
    

class Solution:
    def coinChange(self, coins, amount):

        q = PriorityQueue()

        q.put((0, (0,0)))
        if amount in coins:
            return 1
        while not q.empty():
            sys.stdout.write(f"L-> {q.qsize()}...      ")
            sys.stdout.flush()
            
            priority, element = q.get()
            sum1, steps = element
            if sum1 == amount:
                return steps
            for x in range(len(coins) ):
                if (amount-sum1)>=coins[x]:
                    ns=steps+1
                    q.put((ns, ( sum1+(coins[x]), ns)))
        return -1
# print(Solution().coinChange([1,2,5],11))
print(Solution().coinChange([186,419,83,408],6249))
print(Solution().coinChange([1,2,5,10],18))