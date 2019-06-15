number_of_loop = int(input())
open_brackets = []
for x in range(number_of_loop):
    brackets = input()
    open_brackets = []
    for bracket in brackets:
        if bracket == '(' or bracket =='{' or bracket == '[':
            open_brackets.append(bracket)
        elif bracket == '}' and open_brackets[-1] == '{' or bracket == ']' and open_brackets[-1] == '[' or bracket == ')' and open_brackets[-1] == '(':
            open_brackets.pop()    
        else:
            break
    
    if len(open_brackets) == 0:
        print ('YES')
    else:
        print ('NO')
            
            
    
                     
