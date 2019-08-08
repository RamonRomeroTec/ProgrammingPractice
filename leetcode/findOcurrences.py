class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        a=[]
        text=text.split(" ")
        for i in range(len(text)-2):
            if text[i]==first:
                if text[i+1]==second:
                    a.append(text[i+2])
                else:
                    i+=1
        return a