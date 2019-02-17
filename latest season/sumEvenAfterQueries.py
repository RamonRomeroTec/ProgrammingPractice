'''
Note: Naive -> Cuello de botella
Checar uso de variables calculadas en el momento vs almacenadas
considerando repeticion de ellas

'''


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even = set()
        sumatoy = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.add(i)
                sumatoy = sumatoy+A[i]
        ans = []

        for i in queries:
            order = i[0]
            to = i[1]
            bef = A[to]
            #print(sumatoy, even, bef, "<", order)
            A[to] = A[to]+order
            if to not in even and (bef+order) % 2 == 0:
                even.add(to)
                sumatoy = sumatoy+(bef+order)
            elif to in even and (bef+order) % 2 != 0:
                sumatoy = sumatoy-(bef)
                even.remove(to)
            elif to in even and (bef+order) % 2 == 0:
                sumatoy = sumatoy+order

            ans.append(sumatoy)
        return ans
