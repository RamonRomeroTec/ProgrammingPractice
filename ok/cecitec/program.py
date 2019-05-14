'''
Copyright 2019 © Ramon Romero   @RamonRomeroQro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    cells = re.findall(r'[A-Z]+[0-9]+', functions[key][1:]) # find cells
    if key not in functions:
        return str(matrix[key[0]][key[1]])

    for cell in cells:
        s1 = str(getvalue(cell, functions, matrix, visited))  # mutual recursion
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
            elif splitted[col] != "":
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
