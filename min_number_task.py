print("Enter three number's:")

num_first = int(input())
num_second = int(input())
num_third = int(input())
num_min = num_first

if num_min >= num_second:
    num_min = num_second
if num_min >= num_third:
    num_min = num_third

print("Minimum is", num_min)

# a можно и так
print("Minimum is", min(num_first, num_second, num_third))

