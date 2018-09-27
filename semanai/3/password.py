def prefixfunction(txt,m,lps):
	l = 0
	lps[0] = 0
	i = 1
	while i<m:
		if txt[i]==txt[l]:
			l+=1
			lps[i] = l
			i += 1
		else:
			if l!=0:
				l = lps[l-1]
			else:
				lps[i] = 0
				i += 1

                
if __name__ == '__main__':

    s = input().strip()
    longitud = len(s)
    if longitud==1 or longitud==2:
    	print("Just a legend")
    	exit(0)
    lps = [0]*longitud
    prefixfunction(s,longitud,lps)
    val = lps[-1]
    if val==0:
    	print("Just a legend")
    elif val in lps[:-1]:
    	print(s[:val])
    elif lps[val-1]==0:
    	print("Just a legend")
    elif lps[val-1]:
    	print(s[:lps[val-1]])
    else:
    	print("Just a legend")
