class Solution:
    def reorderSpaces(self, text: str) -> str:
        s=text.count(" ")
        text=text.split()
        if len(text)!=1:
            sp=" "*(s//(len(text)-1))
            tail=" "*(s-(len(sp)*(len(text)-1)))
            return (sp).join(text)+tail
        else:
            tail=" "*(s)
            return text[0]+tail
        