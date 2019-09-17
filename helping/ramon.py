def invertir_arreglo(arr):
    nuevo = []
    for i, v in enumerate(arr):
        if i % 2 != 0:
            nuevo.append(v*-1)
        else:
            nuevo.append(v)
    return nuevo

def encontrar_cota(arr):
    if arr[-1] < 0:
        arr = [(x*-1) for x in arr]
    cota = arr[0]
    evaluator=division_sintetica(arr, cota)
    case = -1
    for i in evaluator:
        if i < 0:
            case = 1
            break

    if case == 1:# nega
        while True:
            arreglo_respuesta=division_sintetica(arr, cota)
            i = 0
            while i< len(arreglo_respuesta):
                if arreglo_respuesta[i]<0:
                    break
                i+=1
            if i==len(arreglo_respuesta):
                return cota
            cota+=1


    else:

        while True:
            arreglo_respuesta=division_sintetica(arr, cota)
            for i in arreglo_respuesta:
                if i < 0:
                    return cota+1
            cota=cota-1
    
        


def division_sintetica(arr, cota):

    aux=arr[::-1]
    ans = [ aux[0] ]
    for i in range(1, len(arr)):        
        suma = aux[i]+ (cota * ans[-1])
        ans.append (suma)

    return ans

###

def func( x , arr): 
    evalu=0
    for i in range(len(arr)):
        print('xxx',x,arr[i] )
        evalu= evalu + (x * arr[i]) **i
    print(evalu)
    return evalu
   
# Prints root of func(x) 
# with error of EPSILON 
def bisection(a,b, arr): 
    au1=func(a, arr)
    au2=func(b, arr)
    if ((au1 *  au2) >= 0): 
        print("You have not assumed right a and b\n") 
        return -1
   
    c = a 
    while ((b-a) >= 0.01): 
  
        # Find middle point 
        c = (a+b)/2
   
        # Check if middle point is root 
        if (func(c, arr) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(c, arr)*func(a, arr) < 0): 
            b = c 
        else: 
            a = c 
              
    print("The value of root is : ","%.4f"%c) 
      
# Driver code 
# Initial values assumed 


###

def main():
    #arr = [5, 4, 3, 2]
    arr = [0, 3, 7, 1]
    #print(invertir_arreglo(arr))
    maxinum = encontrar_cota(arr),
    minimun = -1*encontrar_cota(invertir_arreglo(arr))
    print(maxinum, minimun)
    print(bisection(minimun, maxinum, arr))
    # print()


if __name__ == "__main__":
    main()
