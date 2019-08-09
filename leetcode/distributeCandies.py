# sum (1,n) = (n*(n+1))//2
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        arr = [0]*num_people
        current = 1
        suma = 0 
        
        while suma < candies:
            for i in range(num_people):
                arr[i]=arr[i]+current
                suma = suma + current
                if suma + current+1 >= candies:
                    try:
                        arr[i+1]=arr[i+1]+candies-suma
                    except:
                        arr[0]=arr[0]+candies-suma
                    suma = candies
                    break
                current = current+1
                
                
           
        return arr

