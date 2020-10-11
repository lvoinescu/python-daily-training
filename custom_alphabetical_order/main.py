# Given a list of words, and an arbitrary alphabetical order, verify that the words
# are in order of the alphabetical order.
#
# Example:
#
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: False
#
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'
#
# Example 2:
#
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: True
#
# Explanation: The words are in increasing alphabetical order


def is_sorted_given_order(words, order):
    order_index = {}
    i = 0
    order_index[""] = -1
    for character in order:
        order_index[character] = i
        i += 1

    char_index = 0
    done = False
    while not done:
        max_char = ""
        for word in words:
            done = True
            if char_index >= len(word):
                continue
            else:
                done = False
            if max_char is not None and order_index[word[char_index]] < order_index[max_char]:
                return False
            if order_index[word[char_index]] > order_index[max_char]:
                max_char = word[char_index]
        char_index += 1
    return True


def is_regularly_sorted(words):
    char_index = 0
    done = False
    while not done:
        max_char = ""
        for word in words:
            done = True
            if char_index >= len(word):
                continue
            else:
                done = False
            if max_char is not None and word[char_index] < max_char:
                return False
            if word[char_index] > max_char:
                max_char = word[char_index]
        char_index += 1
    return True


print("ab abx abf:", "sorted" if is_regularly_sorted(["ab", "abx", "abf"]) else "not sorted")
print("ab abd abf:", "sorted" if is_regularly_sorted(["ab", "abd", "abf"]) else "not sorted")
print("a ab abd abf:", "sorted" if is_regularly_sorted(["a"",ab", "abd", "abf"]) else "not sorted")
print("ax ab abd abf:", "sorted" if is_regularly_sorted(["ax", "ab", "abd", "abf"]) else "not sorted")
print("ax ab abcd abf:", "sorted" if is_regularly_sorted(["a", "ab", "abxd", "abf"]) else "not sorted")

print()
sample1 = ["abcd", "efgh"]
order1 = "zyxwvutsrqponmlkjihgfedcba"
print(sample1, "Sorted" if is_sorted_given_order(sample1, order1) else "not sorted", "according to order", order1)
# False
sample2 = ["zyx", "zyxw", "zyxwy"]
order2 = "zyxwvutsrqponmlkjihgfedcba"
print(sample2, "Sorted" if is_sorted_given_order(sample2, order2) else "not sorted", "according to order", order2)
# # True
