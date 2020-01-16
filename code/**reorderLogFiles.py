# Use tuple in lambda as second key, to order

class Solution(object):
    def reorderLogFiles(self, logs):
        llogs=[]
        dlogs=[]
        for l in logs:
            ev=l.split(" ")
            k, v = ev[0], " ".join(ev[1:])
            if not v[0].isdigit():
                llogs.append((k,v))
            else:
                dlogs.append(l)
        return([str(pair[0]+" "+ pair[1]) for pair in sorted(llogs, key=lambda x:(x[1], x[0]))])+dlogs
            
                
        