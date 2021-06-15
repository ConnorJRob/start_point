# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for number in numbers:
    if number % 2 == 0:
        print(number)

# 2. Print the difference between the largest and smallest value:
print((max(numbers)) - (min(numbers)))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
duplicate_num_to_check = 2
check_num = 0
for number in numbers:
    if check_num == 0:
        previous_number = number
    elif check_num > 0:
        if number and previous_number == duplicate_num_to_check:
            print(True)
            break
        else:
            previous_number = number
    check_num += 1

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

start_ban_num = 6
end_ban_num = 7

total = 0
lock_tracker = False

for number in numbers:
        if lock_tracker == True and number != end_ban_num:
            pass
        else:
            if number == end_ban_num:
                lock_tracker = False
                pass
            else:
                if number != start_ban_num :
                    total += number
                elif number == start_ban_num :
                    lock_tracker = True
                elif number == end_ban_num:
                    lock_tracker = False


print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

q5_total = 0
q5_check_num = 0
last_number = ""
unlucky_num = 13

# numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

for number in numbers:
    if number == unlucky_num:
        last_number = number
        pass
    elif last_number == 13:
        last_number = number
        pass
    else:
        q5_total += number
        last_number = number

print(q5_total)
print(last_number)





