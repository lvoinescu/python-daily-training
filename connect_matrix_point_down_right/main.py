# You have 2 integers n and m representing an n by m grid;
# determine the number of ways you can get from the top-left to the bottom-right
# of the matrix y going only right or down.

# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.

def from_top_left_to_bottom_right(matrix, i, j, partial_solution):
    if i >= len(matrix) or j >= len(matrix[0]):
        return

    if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        partial_solution.append(matrix[i][j])
        print("Complete path: " + str(partial_solution))
        partial_solution.pop()

    if i < len(matrix):
        partial_solution.append(matrix[i][j])
        from_top_left_to_bottom_right(matrix, i + 1, j, partial_solution)
        partial_solution.pop()

    if j < len(matrix[i]):
        partial_solution.append(matrix[i][j])
        from_top_left_to_bottom_right(matrix, i, j + 1, partial_solution)
        partial_solution.pop()


input_matrix = [
    ['0', '4', '8', 'C'],
    ['1', '5', '9', 'D'],
    ['2', '6', 'A', 'E'],
    ['3', '7', 'B', 'F']
]

from_top_left_to_bottom_right(input_matrix, 0, 0, [])
