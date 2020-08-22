#def a func that takes a list of numbers and a sum.
#If the list contains a pair of numbers that match the value of the sum, return the two numbers.

def func(list, sum_value):
    large_num = sum_value - 1
    small_num = 1
    while small_num <= large_num:
        new_list = list[:]  
        if large_num in list and small_num in [n for n in list if n !]:
            print("{} and {}".format(small_num, large_num))
            large_num -= 1
            small_num += 1
        else:
            large_num -= 1
            small_num += 1


list1 = [1, 2, 4, 5, 6, 7, 8, 8] 
sum1 = 10

list2 = [1, 2, 4, 4]
sum2 = 8

func(list1, sum1)
func(list2, sum2)
