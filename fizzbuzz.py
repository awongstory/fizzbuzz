while 1:
    try:
        first_num = input("This will make up your fizz. What number would you like to replace?")
        first_num = int(first_num)
    except ValueError:
        print("User string is not a number.")
        continue
    print("Your first number is", first_num)
    break
    
while 1:
    try: 
        second_num = input("This will make up your buzz. What number would you like to replace?")
        second_num = int(second_num)
    except ValueError:
        print("User string is not a number.")
        continue
    print("Your second number is", second_num)
    break
    
while 1:
    try:
        user_min_range = input("What is the minimum number in your range?")
        user_min_range = int(user_min_range)
    except ValueError:
        print("User string is not a number.")
        continue
    print("Your minimum number is", user_min_range)
    break
    
while 1: 
    try:
        user_max_range = input("What is the maximum number in your range?")
        user_max_range = int(user_max_range)
    except ValueError:
        print("User string is not a number.")
        continue
    print("Your maximum number is", user_max_range)
    break
    
for i in range(user_min_range, user_max_range):
    if i % first_num == 0 and i % second_num == 0:
        print("fizzbuzz")
    elif i % first_num == 0:
        print("fizz")
    elif i % second_num == 0:
        print("buzz")
    else:
        print(i)
print("Would you like to try again?")


