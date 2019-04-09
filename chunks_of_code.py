re.sub(r'(76|67)(\d+ )', r'\1(2)', '765 ')

def decurler(i):
    if type(i)==str: 
        i=re.sub('\(|\)','', i) 
    return i 

