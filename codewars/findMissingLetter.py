def find_missing_letter(chars):
    s=chars[0]
    for i in chars:
        if i!=s:
            return s
        else:
            s=chr(ord(s)+1)


