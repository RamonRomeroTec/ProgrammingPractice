'''
Copyright 2019 © Ramon Romero   @RamonRomeroQro

This program is free software under the GNU General Public License.

'''

import sys
import re


def getvalue(cell_name, functions, matrix, visited):
    '''Get keys to evaluate'''

    for i in range(len(cell_name)):
        if cell_name[i].isdigit():
            break

    #key = (int(cell_name[i:])-1, dict_letters[cell_name[:i]])
    key = (int(cell_name[i:])-1, ord(cell_name[:i])-ord('A'))

    if key in visited:
        return "#ERROR"

    if key in functions:
        visited.add(key)
        return evaluation(key, functions, matrix, visited)  # mutual recursion

    else:
        if matrix[key[0]][key[1]] == "":
            return '#NAN'
        else:
            return "matrix["+str(key[0])+"]["+str(key[1])+"]"


def evaluation(key, functions, matrix, visited):
    ''' Splitting  functions and keys'''
    cells = re.findall(r'[A-Z]+[0-9]+', functions[key][1:])  # find cells
    if key not in functions:
        return str(matrix[key[0]][key[1]])

    for cell in cells:
        # mutual recursion
        s1 = str(getvalue(cell, functions, matrix, visited))
        functions[key] = functions[key].replace(cell, s1)

    if "#NAN" in functions[key][1:]:
        return "#NAN"
    elif "#ERROR" in functions[key][1:]:
        return "#ERROR"
    else:
        try:
            return eval(functions[key][1:])  # pythonic evaluation
        except:
            return "#ERROR"


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
                splitted[col] = int(splitted[col])

        matrix.append(splitted)
        row = row+1

    fp.close()

    for key in functions.keys():
        matrix[key[0]][key[1]] = evaluation(key, functions, matrix, set())

    # Print output
    print("\n".join(["\t".join([str(e) for e in line]) for line in matrix]))


if __name__ == "__main__":
    '''Console Spreadsheet'''
    main(sys.argv)
