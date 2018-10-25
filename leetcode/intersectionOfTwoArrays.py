from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        s=set(nums1)

        z=set(nums2)

        inter=s&z

        a=Counter(nums1)

        b=Counter(nums2)
        r=[]
        for i in inter:
            while a[i]!=0 and b[i]!=0:
                r.append(i)
                a[i]=a[i]-1
                b[i]=b[i]-1


        return sorted(r)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
