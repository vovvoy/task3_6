p = int(input())
for x in range (p):
    s1 = input()
    s2 = input()
    k = 0
    s1 = "".join(set(s1))
    s2 = "".join(set(s2))
    for i in range (len(s1)):
        for x in range (len(s2)):
            if s1[i] == s2[x]:
                k += 1
                break
                
    if k == 0:
        print ('NO')
    else:
        print('YES')
        
