#!/bin/bash
 
d=`date +%m-%d-%Y//%T`
message=' "$d -> Another Problem" '
            
git pull
git add -A
eval git commit -m "$message"      
git push origin master
