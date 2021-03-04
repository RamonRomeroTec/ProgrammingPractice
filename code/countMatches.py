class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        def evaluation_rule(ruleKey):
            if ruleKey == "type":
                return 0
            elif ruleKey == "color":
                return 1
            else:
                return 2
        c=0    
        for t in items:
            if t[evaluation_rule(ruleKey)]==ruleValue:
                c+=1
            
        return c
        