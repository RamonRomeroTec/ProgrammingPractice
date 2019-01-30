def remove_smallest(numbers):
    if len(numbers)==0:
        return []
    else:
        m=min(numbers)
        #del numbers[numbers.index(m)]
        ind=numbers.index(m)
        return numbers[:ind]+numbers[ind+1:]
        
    
