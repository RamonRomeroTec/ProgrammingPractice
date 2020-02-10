# 2020 Ramon Romero @RamonRomeroQro

import json
from collections import deque
import sys
from collections import OrderedDict


def flatten(dictionary):
    """
    Flat Dict from JSON-API.

    :type retrived_json: Dict loaded from API-JSON
    :rtype: Dict[string]:List[string]
    """

    flatten = OrderedDict()  # ordered dict to visualize BFS
    queue = deque(dictionary.keys())
    while queue:
        access = queue.popleft()
        eval_key = '[' + \
            "][".join(["\""+str(x)+"\"" for x in access.split('__')])+']'
        try:
            values = eval('dictionary'+eval_key).keys()
            node_vals = [access+'__'+x for x in values]
            queue += node_vals
            flatten[access] = node_vals
        except AttributeError:  # for leaf nodes
            flatten[access] = []
    return flatten


def main(argv):
    if len(argv) != 2:
        print("Missing argument")
    else:
        #'./inputs/sample-1.json'
        fp = open(argv[1])
        dictionary = json.load(fp)  # Load JSON
        fp.close()
        print('key', '\t->\t', 'value')
        for k, v in flatten(dictionary).items():
            print(k, '\t->\t', v)


if __name__ == "__main__":
    main(sys.argv)
