print("Please, enter current day, month, year:")

n_day = int(input())
n_month = int(input())
n_year = int(input())

print("Please, enter your birth day:")

b_day = int(input())
b_month = int(input())
b_year = int(input())

c_age = n_year - b_year

if (b_month > n_month) or (b_month == n_month and b_day > n_day):
    c_age -= 1

if c_age >= 0:
    print("Your age is", c_age)
else:
    print("LMFAO")
