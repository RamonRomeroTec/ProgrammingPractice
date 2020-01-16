#!/bin/bash
 
# d=`date +%m-%d-%Y//%T`
# message=' "$d -> Another Problem" '
            
# git pull
# git add -A
# eval git commit -m "$message"      
# git push origin master

#git log --format=%aD <FILE> | tail -1

#!/bin/bash


# import os
# dirx='./code'
# for filename in os.listdir(dirx):
#     if filename.startswith("_"): 
#         i=0
#         while i<len(filename):
#             if filename[i]!='_':
#                 break
#             i+=1
#         news=filename[i:]
#         os.rename(os.path.join(dirx, filename), os.path.join(dirx, news))
#         continue
    

# #os.rename('a.txt', 'b.kml')
for filename in ./code/*.py; do

    echo `git log --diff-filter=A --follow --format=%aD -1 -- $filename` $filename
done