"""Program that takes a value lower_bound and upper_bound and conducts a
binary search to find the number that the user chose that is between
these 2 values

Authour: Victor Tarnovski
Date 2020-11-18

"""

import math

def main():
    while True:
        lower_bound = (input("Enter the lower boundary of the range: "))
        upper_bound = (input("Enter the upper boundary of the range: "))
        try:
            lower_bound = int(lower_bound)
            upper_bound = int(upper_bound)
        except ValueError:
            print("Please input only integers")
            continue
        else:
            if lower_bound < upper_bound :
                break
            else:
                print("Upper boundary must be greater than the lower one")
                continue
    
    number_of_questions = math.log(upper_bound - lower_bound, 2)
    number_of_questions = math.ceil(number_of_questions)

    mid = round((upper_bound + lower_bound)/2)
    while True :
        answer = input("Is the number greater than " + str(mid) + " (y/n)?: ")
        if answer in ['y', 'Y', 'yes', 'Yes']:
            lower_bound = mid
            mid = round((lower_bound + upper_bound)/2 + 1)
            break
        elif answer in ['n', 'N', 'no', 'No']:
            upper_bound = mid
            mid = round((upper_bound + lower_bound)/2 - 1)
            break
        else:
            print("Please check that your input is either y or n")
            continue

    i=2
    while i < number_of_questions :
        answer = input("Is the number greater than " + str(mid) + " (y/n)?: ")
        if answer in ['y', 'Y', 'yes', 'Yes']:
            lower_bound = mid
            mid = round((lower_bound + upper_bound)/2)
            i += 1
        elif answer in ['n', 'N', 'no', 'No']:
            upper_bound = mid
            mid = round((upper_bound + lower_bound)/2)
            i += 1
        else:
            print("Please check that your input is either y or n")
             
    while True :
        answer = input("Is the number greater than " + str(mid) + " (y/n)?: ")
        if answer in ['y', 'Y', 'yes', 'Yes']:
            print("The number you chose was: ", upper_bound)
            break
        elif answer in ['n', 'N', 'no', 'No']:
            print("The number you chose was: ", mid)
            break
        else:
            print("Please check that your input is either y or n")
            continue
main()
