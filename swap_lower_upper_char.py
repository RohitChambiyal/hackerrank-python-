def checklower(x):
    x = str(x.upper())
    return x

def checkupper(x):
    x = str(x.lower())
    return x

def swap_case(k):
    s = str(k)
    
    x=''
    l = len(s)
    for i in range(l):
        
        if(s[i].islower()):
            x = x + checklower(s[i])
        elif(s[i].isupper()):
            x= x + checkupper(s[i])
        else:
            x= x + s[i]
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
