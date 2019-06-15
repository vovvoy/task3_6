your_list = []
list_size = int(input())
for x in range (list_size):
    volue = int(input())
    your_list.append(volue)

step = int(input())

if step < 0:
    your_list.reverse()

for x in range (abs(step)):
    your_list.append(your_list[0])
    your_list.remove(your_list[0])
    
if step < 0:
    your_list.reverse()
    
print (your_list)
 
    
