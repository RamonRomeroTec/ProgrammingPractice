'''
Copyright 2019 © Ramon Romero   @RamonRomeroQro

This program is free software.
Under the GNU General Public License.

'''

import sys
import re


def str_to_index(str1):
    ''' Given a string index return integer equivalent '''
    result = 0
    for i in str1:
        result = result * 26
        result = result + (ord(i) - ord('A') + 1)
    return result-1


def getvalue(cell_name, functions, matrix, visited):
    '''Get values to evaluate'''

    for i in range(len(cell_name)):
        if cell_name[i].isdigit():
            break

    # key = (int(cell_name[i:])-1, ord(cell_name[:i])-ord('A')) chars between A-Z
    key = (int(cell_name[i:])-1, str_to_index(cell_name[:i]))

    if key in visited:
        return "#ERROR"  # circular reference

    if key in functions:
        visited.add(key)
        # mutual recursion
        return evaluation(key, functions, matrix, visited)

    else:
        try:
            if matrix[key[0]][key[1]] == "":
                return '#NAN'  # Empty reference
            else:
                return "matrix["+str(key[0])+"]["+str(key[1])+"]"
        except IndexError:
            return "#ERROR"  # Unexisting index


def evaluation(key, functions, matrix, visited):
    ''' Splitting  functions and keys'''

    #(1,3)= "=A3+B3" 4, 3

    # =4
    # =(4+3)*3
    # =7

    # +
    # 4 3




    cells = re.findall(r'[A-Z]+[0-9]+', functions[key][1:])  # find cells
    if key not in functions:
        return str(matrix[key[0]][key[1]])

    for cell in cells:
        # mutual recursion
        # break if middle error evaluation
        s1 = str(getvalue(cell, functions, matrix, visited))
        if s1 == "#NAN":
            return "#NAN"
        elif s1== "#ERROR" :
            return "#ERROR" 
        functions[key] = functions[key].replace(cell, s1)
    try:
        
        return eval(functions[key][1:].replace('/','//' ))  # pythonic evaluation
    except:
        return "#ERROR"  # syntactical error


def main(args):
    ''' Main and parsing from tsv'''
    functions = {}
    fp = open(args[1], 'r')
    matrix = []
    row = 0
    for line in fp:
        splitted = line.strip('\n').split("\t")
        for col in range(len(splitted)):
            if splitted[col].startswith("="):
                functions[(row, col)] = splitted[col]
            elif splitted[col].isdigit():
                # splitted[col] = float(splitted[col]) handle floating point operations
                splitted[col] = int(splitted[col])

        matrix.append(splitted)
        row = row+1

    fp.close()

    for key in functions.keys():
        matrix[key[0]][key[1]] = evaluation(key, functions, matrix, set())

    # print(functions)

    # Print output
    print("\n".join(["\t".join([str(e) for e in line]) for line in matrix]))


if __name__ == "__main__":
    '''Console Spreadsheet'''
    main(sys.argv)
