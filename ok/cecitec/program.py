import sys
import string
import re
import pprint

def getvalue(ln, dl, functions, matrix, visited):
    # for i in range(len(ln)):
    #     if ln[i].isdigit():
    #         break
    # return int(ln[i:])-1, dl[ln[:i]]
    for i in range(len(ln)):
        if ln[i].isdigit():
            break
    k = (int(ln[i:])-1, dl[ln[:i]])
    if k in visited:
        return "circular"
    if k in functions:
        visited=visited.add(k)
        return evaluation(k, functions, matrix, dl, visited)
    else:
        if matrix[int(ln[i:])-1][dl[ln[:i]]] =="":
            return '#NAN'
        else:
            return "matrix["+str(int(ln[i:])-1)+"]["+str(dl[ln[:i]])+"]"


def evaluation(k, functions, matrix, dl, visited):
    v = re.findall(r'[A-Z]+[0-9]+', functions[k][1:])
    if k not in functions:
        return str(matrix[k[0]][k[1]])

    for var in v:
        s1=str(getvalue(var, dl, functions, matrix, visited))
        functions[k]=functions[k].replace(var, s1)

    if "#NAN" in functions[k][1:]:
        return "#NAN" 
    else:
        to_x=functions[k][1:]
        return eval(to_x)
    # x = re.split(r'\w+', functions[k][1:])
    # j=0
    # print(v)
    # print(x)
    # for i in range(len(x)):
    #     if x[i]=="":
    #         new_row, new_col = getvalue(v[j], dl)
    #         j=j+1
    #         if (new_row, new_col) in functions:
    #             x[i]=evaluation((new_row, new_col), functions, matrix, dl)
    #         else:
    #             x[i]="matrix["+str(new_row)+"]["+str(new_col)+"]"
    # p=("".join(x))
    # print("-->",p)
    # return eval(p)




def main(args):
    dl = dict(zip(string.ascii_uppercase, range(0,26)))
    functions= {}
    fp =  open(args[1], 'r')
    matrix=[]
    row=0
    for line in fp:
        splitted = line.strip('\n').split("\t")
        for col in range(len(splitted)):
            if splitted[col].startswith("="):
                functions[(row, col)] = splitted[col]
            elif splitted[col]!="":
                splitted[col]=int(splitted[col])
        matrix.append(splitted)
        row=row+1
    #print(matrix)
    #print(functions)
   
    for k in functions.keys():
        matrix[k[0]][k[1]]=evaluation(k, functions, matrix, dl, set())


        
               

    print(matrix)

          



if __name__ == "__main__":
    main(sys.argv)