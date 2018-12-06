import re




def variableName(name):
    f= re.fullmatch(r'([A-Z]+|_+|[a-z]+)+([a-z]*[A-Z]*_*[0-9]*)*$', name)
    if f:
        return True


    else:
        return False
