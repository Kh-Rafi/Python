s = input()


sorted_s = sorted(s, key=lambda c: (
    not c.islower(),          
    not c.isupper(),          
    not (c.isdigit() and int(c) % 2 != 0),  
    not (c.isdigit() and int(c) % 2 == 0),  
    c                         
))


print("".join(sorted_s))
