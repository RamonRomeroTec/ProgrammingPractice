class Solution:
    def groupThePeople(self, groupSizes):
        arr={}
        for index, len_value in enumerate(groupSizes):
            if len_value not in arr:
                arr[len_value]=[[index]]
            else:
                if len(arr[len_value][-1])<len_value:
                    arr[len_value][-1].append(index)
                else:
                    arr[len_value].append([index])
        a=[]
        for x in arr.values():
            for l in x:
                a.append(l)
        return a