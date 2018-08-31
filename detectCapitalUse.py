'''

ord es una funcion que nos recupera el codigo ascii de la letra
Operador de suma lógica no existe, es necesario ejecutar and

'''
class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        '''
        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital if it has more than one letter, like "Google".
        Otherwise, we define that this word doesn't use capitals in a right way.
        '''
        
        initMayus=True
        restminus=True
        restmayus=True

        # write your code here
        
        if ord(word[0]) >= 65 and  ord(word[0]) <= 90:
            initMayus=True
        else:
            initMayus=False 
            
            
        for  i in range(1, len(word)):
            if ord(word[i]) >= 65 and  ord(word[i]) <= 90:
                restmayus=restmayus and True

                restminus=restminus and False
            else:
                restmayus=restmayus and False
                restminus=restminus and True    

        #print (restminus);
                
    
        if (initMayus==True and restminus==True):
            return True
        elif (initMayus==True and restmayus==True):
            return True
        elif (initMayus==False and restminus==True):
            return True
        else:
            return False
