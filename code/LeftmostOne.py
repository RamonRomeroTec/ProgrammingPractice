class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        l=[]
        for i in arr:
            k=i.index(1)
            print(k)
            l.append(k)

        l=sorted(l)

        return l[0]

            # TODO: write code...
        # Write your code here
