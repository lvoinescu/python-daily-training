# You have a landscape, in which puddles can form.
# You are given an array of non-negative integers representing the elevation at each location.
# Return the amount of water that would accumulate if it rains.

# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.

#        X
#    X███XX█X
# _X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
# 6

def my_naive_solution(arr):
    result = 0
    left_peak = 0
    left_peak_index = 0
    while left_peak_index < len(arr):
        if left_peak <= arr[left_peak_index]:
            left_peak = arr[left_peak_index]
            left_peak_index += 1
        else:
            left_peak_index -= 1
            right_peak = arr[left_peak_index + 1]
            right_peak_index = 0
            for j in range(left_peak_index + 1, len(arr)):
                if right_peak <= arr[j]:
                    right_peak = arr[j]
                    right_peak_index = j
                if right_peak >= left_peak:
                    break
            to_subtract = sum(arr[left_peak_index + 1:right_peak_index])
            if right_peak_index > 0:
                result += min(right_peak, left_peak) * (right_peak_index - left_peak_index - 1) - to_subtract
                left_peak_index = right_peak_index
                left_peak = right_peak
            else:
                left_peak_index += 1
    return result


print(my_naive_solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
