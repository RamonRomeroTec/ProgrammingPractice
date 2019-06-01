class Solution(object):
    def subdomainVisits(self, cpdomains):
        table={}
        for e in cpdomains:
            e=e.split(' ')
            counter , domains = int(e[0]), e[1].split('.')
            for i in range(len(domains)):
                key=".".join(domains[i:])
                if key in table:
                    table[key]+=counter
                else:
                    table[key]=counter
        return [str(v)+" "+str(k) for k,v in table.items()]
    
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        