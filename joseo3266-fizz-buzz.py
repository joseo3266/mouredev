
for number in range(1,101):
    tres = False
    cinco = False
    if number % 3 == 0:
        tres = True
    if number % 5 == 0:
        cinco = True
    if tres and cinco:
        print("fizzbuzz")
    elif tres == True:
        print("fizz")
    elif cinco:
        print("buzz")
    else:
        print(number)