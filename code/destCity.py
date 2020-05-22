class Solution(object):
    def destCity(self, paths):
        d = set()
        o = set()
        for p in paths:
            ori, dest = p
            d.add(dest)
            o.add(ori)
        return list(d - o)[0]
