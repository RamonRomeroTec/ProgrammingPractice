
def my_newf(b1,b2):
    answer=[0]*8
    s=7
    carry=0
    while s>=0:
        answer[s]=((b1[s]^ b2[s]) ^ carry)
        carry=((b1[s] & b2[s]))
        s-=1
    return answer
        
        
                
#sum_Value,carryOver=bitOperator(1,0,0)
print("The sum is",my_newf([0,0,0,0,0,1,1,1],[0,0,0,0,0,0,1,1]))# here you are working with two tens