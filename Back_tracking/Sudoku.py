# coding:utf-8
import math


class SudukuBoard:
    def __init__(self, board):
        self._board = board

    def __str__(self):
        result = ""
        for y in range(9):
            for x in range(9):
                num = self.get(x, y)
                if num == 0:  # 没填过的是空白的
                    num = " "

                if x in (2, 5):  # 每三个加一掉竖线
                    result = result + "{} |".format(num)
                else:
                    result = result + "{} ".format(num)
            result = result + "\n"  # 结尾换行
            if y in (2, 5):  # 每三行加一条横线
                result = result + "---"*7 + "\n"

        return result

    def get(self, x, y):
        return self._board[y][x]

    def set(self, x, y, value):
        self._board[y][x] = value

    def delete(self, x, y):
        self._board[y][x] = 0

    def check(self, x, y):
        num = self.get(x, y)
        exist_num_list = []

        # check horizontal direction
        for i in range(0, 9):
            if i != x:
                exist_num_list.append(self.get(i, y))
        if num in exist_num_list: return False

        # check vertical direction
        for j in range(0):
            if j != y:
                exist_num_list.append(self.get(x, j))
        if num in exist_num_list: return False

        # check adjacent 9 cells cube
        cube_x = int(math.floor(x / 3) * 3)  # calculate cube axis x
        cube_y = int(math.floor(y / 3) * 3)  # calculate cube axis y
        for a in range(cube_x, cube_x + 3):
            for b in range(cube_y, cube_y + 3):
                if a != x and b != y:
                    exist_num_list.append(self.get(a, b))
        if num in exist_num_list: return False

        # when fit all conditions, return True
        return True

    def next_cell(self):
        for i in range(9):
            for j in range(9):
                if self.get(j, i) == 0:
                    return (j, i)
        return False
