# Given an array containing only positive integers,
# return if you can pick two integers from the array which cuts the array
# into three pieces such that the sum of elements in all pieces is equal.

# Example 1:
#
# Input: array = [2, 4, 5, 3, 3, 9, 2, 2, 2]
#
# Output: true
#
# Explanation: choosing the number 5 and 9 results in three pieces [2, 4], [3, 3] and [2, 2, 2]. Sum = 6.
#
# Example 2:
#
# Input: array =[1, 1, 1, 1],
#
# Output: false


class Solution(object):
    def can_pick(self, arr):
        leftIndex = 1
        rightIndex = len(arr) - 1
        while leftIndex < rightIndex + 2:
            leftSum = sum(arr[0: leftIndex])
            rightSum = sum(arr[rightIndex:len(arr)])
            centerSum = sum(arr[leftIndex + 1: rightIndex - 1])
            if leftSum > rightSum:
                rightIndex -= 1
            else:
                if rightSum > leftSum:
                    leftIndex += 1
                else:
                    if centerSum == leftSum:
                        print(
                            "If we extract indexes " + str(leftIndex) + " and " + str(
                                rightIndex) + " we get 3 'equal' intervals")
                        return True
                    else:
                        leftIndex += 1
        return False


print(Solution().can_pick([2, 4, 5, 3, 3, 9, 2, 2, 2]))
# True

print(Solution().can_pick([1, 2, 3, 4, 5]))
# False
