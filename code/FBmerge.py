class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if (not any(nums1)):
            nums1[:]=nums2[:]
        p= len(nums1) - 1
        m=m-1
        n=n-1
        while p>=0 and m>=0 and n>=0:
            if nums1[m]> nums2[n]:
                nums1[p]=nums1[m]
                nums1[m]=0
                m=m-1
                p=p-1
            else:
                nums1[p] = nums2[n]
                n=n-1
                p=p-1
        if m<0 and n>=0:
            nums1[:n+1] = nums2[:n+1]
            
        
        
        