def factorial(user_num):
    if user_num == 0:
        return 1
    else:
        return user_num * factorial(user_num-1)
user_num=int(input("Input a number to compute the factiorial : "))
print(factorial(user_num))

