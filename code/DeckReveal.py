# IMPLEMENT BOTH SIDES; SOLUTION AND ALGORIHM


from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        #deck.sort()
        size=len(deck)
        ans = [None] * size
        index = deque(range(size))

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans