def reverse_string(s):
    i = len(s)-1
    r = ''
    while i >= 0:
        r = r + s[i]
        i-=1
    print(r)    

reverse_string("abc")    
