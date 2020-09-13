
# You have 2 integers n and m representing an n by m grid;
# determine the number of ways you can get from the top-left to the bottom-right
# of the matrix y going only right or down.

# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.


def seek_solution(matrix, i, j, word, position):
    if position == len(word):
        return True

    print("Checking [" + str(i) + "," + str(j) + "]=" + matrix[i][j])
    if i > 0 and matrix[i - 1][j] == word[position]:
        return seek_solution(matrix, i - 1, j, word, position + 1)
    if i < len(matrix) - 1 and matrix[i + 1][j] == word[position]:
        return seek_solution(matrix, i + 1, j, word, position + 1)
    if j > 0 and matrix[i][j - 1] == word[position]:
        return seek_solution(matrix, i, j - 1, word, position + 1)
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] == word[position]:
        return seek_solution(matrix, i, j + 1, word, position + 1)
    return False


def word_search(matrix, word):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == word[0]:
                found = seek_solution(matrix, i, j, word, 1)
                if found:
                    return True
    return False


input_matrix = [
    ['4', '3', '2', '1'],
    ['B', 'S', 'M', 'E'],
    ['s', 'T', 'E', 'G'],
    ['M', 'O', 'R', 'A']]
needle = 'STORAGE1234'
print(needle + " found: " + str(word_search(input_matrix, needle)))
