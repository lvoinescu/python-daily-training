# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible
# for every character of str1 to every character of str2.
# And all occurrences of every character in ‘str1’ map to same character in ‘str2’


def isomorphic(a, b):
    if len(a) != len(b):
        return False

    character_map = {}
    for i in range(0, len(a)):
        if a[i] not in character_map:
            character_map[a[i]] = b[i]
        else:
            if b[i] != character_map[a[i]]:
                return False
    return True


print(isomorphic("aab", "xxy"))
print(isomorphic("aer", "qer"))
print(isomorphic("aab", "xyy"))
