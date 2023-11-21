# 1,1,2,3,5,8
# a,b,c
print("Fibonacci numbers")
"""
print("1")
old = 1 #a
current = 1 # b
next_number = 0 #c
number = 18
current_number = 0

print(old)
while current_number <= number:
    next_number = old + current
    current_number = next_number
    if current_number >= number:
        break
    else:
        print(current_number)
    old = current + next_number
    current_number = old
    if current_number >= number:
        break
    else:
        print(current_number)
    current = old + next_number
    current_number = current
    if current_number >= number:
        break
    else:
        print(current_number)
"""    
    
def fibonacci(number):
    print("1")
    old = 1 #a
    current = 1 # b
    next_number = 0 #c
    current_number = 0

    print(old)
    while current_number <= number:
        next_number = old + current
        current_number = next_number
        if current_number >= number:
            break
        else:
            print(current_number)
        old = current + next_number
        current_number = old
        if current_number >= number:
            break
        else:
            print(current_number)
        current = old + next_number
        current_number = current
        if current_number >= number:
            break
        else:
            print(current_number)
        
fibonacci(39)