# There are five items a b c d e, whose weight are 2 2 6 5 4, and values are 6 3 5 4 6
# now you have a knapsack whose capacity is 10. How can you carry the most valuable things.
import numpy as np


# recurrently
def recurrence_pick(items, index, capacity):
    if index < 0:
        return 0
    elif capacity == 0:
        return 0

    weight = items[index]['weight']
    value = items[index]['value']

    if weight > capacity:
        return recurrence_pick(items, index-1, capacity)
    else:
        pick_i = recurrence_pick(items, index-1, capacity-weight) + value
        not_pick_i = recurrence_pick(items, index-1, capacity)
        total_value = max(pick_i, not_pick_i)
        return total_value


# dynamic programming
def dp_pick(items, capacity):
    subset = np.zeros((len(items), capacity))
    for i in range(0, len(items)):
        weight = items[i]['weight']
        value = items[i]['value']
        # print("picking {}, w:{}, v:{}".format(i, weight, value))
        for w in range(0, capacity):
            # fill first roll
            if i == 0:
                if weight-1 > w:
                    subset[i][w] = 0
                else:
                    subset[i][w] = value

            # if there is no space for weight
            elif weight - 1 > w:
                subset[i][w] = subset[i-1][w]

            # compare pick and not pick
            else:
                pick = subset[i-1][w-weight] + value
                if weight-1 == w:
                    pick = value
                not_pick = subset[i-1][w]
                subset[i][w] = max(pick, not_pick)
            # print(subset)

    return subset[len(items)-1, capacity-1]


if __name__ == "__main__":
    items0 = [
        {'weight': 2, 'value': 6},
        {'weight': 2, 'value': 3},
        {'weight': 6, 'value': 5},
        {'weight': 5, 'value': 4},
        {'weight': 4, 'value': 6},
    ]

    items0 = [
        {'weight': 4, 'value': 6},
        {'weight': 5, 'value': 4},
        {'weight': 6, 'value': 5},
        {'weight': 2, 'value': 3},
        {'weight': 2, 'value': 6},

    ]
    items1 = [
        {'weight': 1, 'value': 1},
        {'weight': 2, 'value': 6},
        {'weight': 5, 'value': 18},
        {'weight': 6, 'value': 22},
        {'weight': 7, 'value': 28},
    ]
    print(recurrence_pick(items0, 4, 10))
    print(recurrence_pick(items1, 4, 11))
    print(dp_pick(items0, 10))
    print(dp_pick(items1, 11))
