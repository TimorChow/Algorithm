# coding:utf-8
import random
import math


INFINITE = 1000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)


def get_distance(point1, point2):
    return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)


# 根据x坐标排序
# sort by x axis
def sort_by_x(points_list):
    return sorted(points_list, key=lambda point: point.x)


# 根据y坐标排序
# sort by y axis
def sort_by_y(points_list):
    return sorted(points_list, key=lambda point: point.y)


def get_closest_pair(points_list):
    shortest_distance = INFINITE  # initial the shortest as INFINITE
    point1 = None
    point2 = None
    length = len(points_list)
    points_list = sort_by_x(points_list)
    if length == 1:
        return {"distance": shortest_distance,
                "point1": point1,
                "point2": point2}

    elif length == 2:
        point1, point2 = points_list[0], points_list[1]
        shortest_distance = get_distance(point1, point2)
        return {"distance": shortest_distance,
                "point1": point1,
                "point2": point2}

    elif length >= 3:
        # find the mid point which divide the point set to two parts
        mid_line = (points_list[0].x+points_list[-1].x)/2

        # 分左右区域
        # divide the area to two parts
        left_points_list = [point for point in points_list if point.x < mid_line]
        right_points_list = [point for point in points_list if point.x >= mid_line]

        # 递归求左右两边的最小点对
        # recurrence and get the shortest distance and the pair
        distance_of_left_result = get_closest_pair(left_points_list)
        distance_of_right_result = get_closest_pair(right_points_list)

        # 求得最小点对, 并保存两个点的位置
        # get the shortest distance and save the pair
        if distance_of_left_result['distance'] >= distance_of_right_result['distance']:
            shortest_distance = distance_of_right_result['distance']
            point1 = distance_of_right_result['point1']
            point2 = distance_of_right_result['point2']

        elif distance_of_left_result['distance'] < distance_of_right_result['distance']:
            shortest_distance = distance_of_left_result['distance']
            point1 = distance_of_left_result['point1']
            point2 = distance_of_left_result['point2']

        # 中间区域求最小点对
        left_mid_area_points_list = [point for point in points_list if 0 < mid_line-point.x <= shortest_distance]  # 左边区域点 get point on the left side
        right_mid_area_points_list = [point for point in points_list if 0 < point.x-mid_line <= shortest_distance]  # 右边区域的点 get point on the right side

        # right_mid_area_points_list = sort_by_y(right_mid_area_points_list) # 右边区域按y轴排序 sort the point located on the right side

        distance_of_mid = INFINITE

        # compare each point on the left side with every point on the right side(in two squares)
        # get the shortest distance and closest pair
        point_of_leftmid_pair = None
        point_of_rightmid_pair = None
        for point_of_leftmid in left_mid_area_points_list:
            # filter, get all points located in two squares(according to y axis)
            right_mid_area_points_list = [point for point in right_mid_area_points_list if abs(point_of_leftmid.y-point.y) <= shortest_distance]
            for point_of_rightmid in right_mid_area_points_list:
                distance_of_pair = get_distance(point_of_leftmid, point_of_rightmid)
                # if distance is shorter, then replace it and save new pair
                if distance_of_pair < distance_of_mid:
                    distance_of_mid = distance_of_pair
                    point_of_leftmid_pair, point_of_rightmid_pair = point_of_leftmid, point_of_rightmid

        # compare shortest distance of left, mid, and right sides.
        print(shortest_distance, distance_of_mid)
        if distance_of_mid < shortest_distance:
            shortest_distance = distance_of_mid
            point1 = point_of_leftmid_pair
            point2 = point_of_rightmid_pair

        return {"distance": shortest_distance,
                "point1": point1,
                "point2": point2}


def draw(points_list, point1, point2):
    import matplotlib.pyplot as plt
    x = [point.x for point in points_list]
    y = [point.y for point in points_list]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Scatter Plot')
    # 设置X轴标签
    plt.xlabel('X')
    # 设置Y轴标签
    plt.ylabel('Y')
    # 画散点图
    plt.plot([point1.x, point2.x], [point1.y, point2.y], color='r')
    ax1.scatter(x, y, c='r', marker='o')
    # 设置图标
    plt.legend('x1')
    # 显示所画的图
    plt.show()


def main():
    points_list = []
    for n in range(30):  # 生成随机点阵 get random point set
        p = Point(random.random(), random.random())
        points_list.append(p)

    result = get_closest_pair(points_list)
    print(result['distance'], result['point1'], result["point2"])
    print(get_distance(result['point1'], result['point2']))

    draw(points_list, result['point1'], result["point2"])

if __name__ == "__main__":
    main()
