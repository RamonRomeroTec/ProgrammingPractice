class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=['x']*len(s)
        for  index, destiny in enumerate(indices):
            ans[destiny]=s[index]
        return "".join(ans)
        