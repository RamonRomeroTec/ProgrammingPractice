class Solution(object):
    def crawl(self, startUrl, htmlParser):
        c=0
        i=0
        while i < len(startUrl):
            if startUrl[i]=='/':
                c+=1
            if c==3:
                break
            i+=1
        home=startUrl[:i]
        visited=set()
        s=[startUrl]
        while s:
            n=s.pop()
            if n not in visited:
                visited.add(n)
                for n in htmlParser.getUrls(n):
                    if n not in visited and home in n:
                        s.append(n)
        return(visited)
        
        