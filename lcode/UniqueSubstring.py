'''
ok
Input: s = "caaab"
k = 2
Output:["aa","ab","ca"]


'''
class Solution:

    def uniqueSubstring(self, s, k):
        sb=set()
        for i in range(0, len(s)+1-k):
            sb.add(s[i:i+k])
        return (sorted(sb))

if __name__ == '__main__':
    s = "caaaab"
    k = 2
    a= Solution()
    print(a.uniqueSubstring(s,k))
