array = []
arraySize = int(input())
for x in range (arraySize):
    volue = int (input())
    array.append(volue)

array.sort()

min_volue = 0
for x in range (arraySize - 1):
    if x >= 0 and array[x + 1] - array[x] != 1:
        min_volue = x + 2
        break;
if array[len(array) - 1] < 0:
    print (1)
elif min_volue == 0:
    print (array[len(array) - 1] + 1)
else:
    print (min_volue)
