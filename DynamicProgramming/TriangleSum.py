# coding: utf-8


# from bottom to top, every point has two base point
# 1. select the larger one and plus it as the max sum for current point.
def dp_max_sum(triangle):
    result = triangle
    for x in range(len(triangle)-2, -1, -1):
        for y in range(0, len(triangle[x])):
            # get two children point and select the larger one
            bases_list = get_base(x, y)
            left_base = triangle[bases_list[0][0]][bases_list[0][1]]
            right_base = triangle[bases_list[1][0]][bases_list[1][1]]
            result[x][y] = result[x][y] + max(left_base, right_base)

    print(result)


def get_base(x, y):
    left = [x + 1, y]
    right = [x + 1, y + 1]
    bases_list = [left, right]
    return bases_list


if __name__ == "__main__":
    triangle = [[2],
                [5, 4],
                [1, 4, 7],
                [8, 6, 9, 6]
                ]

    dp_max_sum(triangle)

