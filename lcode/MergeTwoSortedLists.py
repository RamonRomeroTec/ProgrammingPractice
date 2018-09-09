

#https://viaje.primeraplus.com.mx/purchase/-7eUv8HN4VM/passengers?departureSeats=13&returnSeats=16&utm_campaign=home-wl&utm_medium=direct&utm_source=widget
class Solution:
    def mergeTwoLists(self, l1, l2):
        for i in l2:
            l1.append(i)

        #print(sorted(l1))

        return sorted(l1)

if __name__ == '__main__':
    a=[1,2,4]
    b=[1,3,4]
    s=Solution()
    print(s.mergeTwoLists(a,b))
