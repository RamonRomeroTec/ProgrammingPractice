# 2020 Ramon Romero @RamonRomeroQro

import json
import sys


def doc_counter(retrived_json):
    """
    Linear evaluation and storage using hashtable (dictionaty) as counter

    :type retrived_json: Dict loaded from API-JSON
    :rtype: Dict[string]:int
    """

    list_items = retrived_json['payload']['items']
    counter = {}
    for item in list_items:
        if item['status'] in counter:
            counter[item['status']] += 1
        else:
            counter[item['status']] = 1
    return counter


def retrive_by_status(status, retrived_json):
    """
    Retrive elements by status

    using doc_counter as was suggested will increase complexity from N->2N

    :type retrived_json: Dict loaded from API-JSON
    :type status: string

    :rtype: List[Dict]
    """

    list_items = retrived_json['payload']['items']
    elements_of_interest = [
        item for item in list_items if item['status'] == status]
    return elements_of_interest


def retrive_by_name(file_name, retrived_json):
    """

    Retrive document based on atribute, file_name

    :type retrived_json: Dict loaded from API-JSON
    :type file_name: string

    :rtype: Dict
    """

    list_items = retrived_json['payload']['items']
    for item in list_items:
        if item['file_name'] == file_name:
            return item
    return None


def main(args):
    """
    Retrive path from command line interface and evaluate all.
    """
    fp = open(args[1])
    retrived = json.load(fp) # Load JSON
    fp.close()

    print('01:', doc_counter(retrived)) # First function
    for status in doc_counter(retrived).keys():
        list_status = retrive_by_status(status, retrived) # Second function
        print('02:', status, '->', list_status)

    for x in list_status:
        print('03:', x['file_name'], '->',
              retrive_by_name(x['file_name'], retrived)) # Third function


if __name__ == "__main__":
    main(sys.argv)
