print("Enter three number's:")

num_first = int(input())
num_second = int(input())
num_third = int(input())
num_min = num_first

# Есть ли смысл делать минимальным num_second, если num_min равно num_second? Аналогично и с num_third
if num_min >= num_second:
    num_min = num_second
if num_min >= num_third:
    num_min = num_third

print("Minimum is", num_min)

# a можно и так
# Можно, так красивее намного
print("Minimum is", min(num_first, num_second, num_third))

