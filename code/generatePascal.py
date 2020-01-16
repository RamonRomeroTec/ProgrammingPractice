class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        if numRows==1:
            return [ [1] ]
        if numRows==2:
            return [ [1], [1,1]  ]
        tp= [ [1], [1,1]  ]
        for x in range(numRows-2):
            tp.append([1])
        for j in range(2,numRows):
            while True:
                tp[j].append(tp[j-1][len(tp[j])-1]+tp[j-1][len(tp[j])])
                if len(tp[j])==j:
                    tp[j].append(1)
                    break
        return tp

import sys

def main():
    n=5
    if len(sys.argv)==2:
        try:
            n=int(sys.argv[1])
        except Exception as e:
            print(e)
            return -1

    else:
        return -1
    for row in Solution().generate(n):
        print(row)
    return 0

if __name__ == '__main__':
    main()
  