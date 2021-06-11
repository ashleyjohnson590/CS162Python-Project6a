#Author: Ashley Johnson
#Date: 5/1/2021
#Description: program takes a parameter a list of numbers and returns the max.

def list_max(num_list):
    "takes a prarameter a list of numbers and returns the max."

    #returns number if length of list is 1. Otherwise, compares first number with next number
    #sets highest number to max.
    if len(num_list) == 1:
        max = num_list[0]
        return max
    else:
        if num_list[0] > list_max(num_list[1:]):
            max=num_list[0]
            return max
        else:
            max = list_max(num_list[1:])
            return max


def main():
    num_list = [2,4,9, 1]
    list_max(num_list)

if __name__ == "__main__":


    main()
