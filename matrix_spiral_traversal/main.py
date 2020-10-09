# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

# Example:
#
# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]


# The clockwise spiral traversal of this array is:
#
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# My naive strategy
#  S-----------------X  <- corner++
#  E <-switch spiral |
#  |                 |
#  |                 |
#  X-----------------X  <- corner++
#  ^
#  corner++
#
def matrix_spiral_print_naive(M):
    j_step = 1
    i_step = 0
    i, j = 0, 0
    start_i, end_i = 0, len(M) - 1
    start_j, end_j = 0, len(M[0]) - 1
    corner_count = 0

    while start_i <= end_i and start_j <= end_j:
        print("[", i, j, "]", M[i][j])
        if i == start_i + 1 and j == start_j:
            start_i += 1
            end_i -= 1
            start_j += 1
            end_j -= 1
            j_step = 1
            i_step = 0
            corner_count = 0

        if (i == start_i and j == end_j) or \
                (i == end_i and j == end_j) or \
                (i == end_i and j == start_j):
            corner_count += 1
            if corner_count == 1:
                i_step = 1
                j_step = 0
            elif corner_count == 2:
                i_step = 0
                j_step = -1
            elif corner_count == 3:
                i_step = -1
                j_step = 0
        i += i_step
        j += j_step


grid = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print_naive(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
