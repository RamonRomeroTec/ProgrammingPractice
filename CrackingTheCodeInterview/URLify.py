
def urlify(s):
    s=s.strip()
    
    return s.replace(" ", "%20")
    
    
    
s = str(input())
print(urlify(s))

