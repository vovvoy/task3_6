your_str = input()
upper_sum = 0
lower_sum = 0
for char in your_str:
    if char.isupper() == 1:
        upper_sum += 1
    if char.islower() == 1:
        lower_sum += 1
print(round(100 / (upper_sum + lower_sum) * upper_sum, 2))
print(round(100 / (upper_sum + lower_sum) * lower_sum, 2))
