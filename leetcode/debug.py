class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        arr = [0]*num_people
        c = 0
        suma = 0 
        while suma < candies:
            for i in range(num_people):
                arr[i]= arr[i] + c+1
                if (c+1*(c+2))//2 > candies:
                    arr[i+1]=candies-((c*(c+1))//2 )
                    suma = candies
                    break
                
                c+=1
                suma=((c*(c+1))//2 )
                
           
        return arr

print(Solution().distributeCandies(10,3))