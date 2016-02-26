first_num = input("This will make up your fizz. What number would you like to replace?")
first_num = int(first_num)

second_num = input("This will make up your buzz. What number would you like to replace?")
second_num = int(second_num)

for i in range(1,101):
    if i % first_num == 0 and i % second_num == 0:
        print("fizzbuzz")
    elif i % first_num == 0:
        print("fizz")
    elif i % second_num == 0:
        print("buzz")
    else:
        print(i)
