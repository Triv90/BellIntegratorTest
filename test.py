from collections import deque


def print_success(previous, moved_pairs, sorted_array):
    result_list = [(sorted_array, -1)]
    array = sorted_array
    while previous[array] != -1:
        result_list.append((previous[array], moved_pairs[array]))
        array = previous[array]

    result_list.reverse()
    for shuffle in result_list:
        result_string = ", ".join(map(str, shuffle[0]))
        if shuffle[1] != -1:
            result_string += " // (" + str(shuffle[0][shuffle[1][0]]) + ", " + str(shuffle[0][shuffle[1][0]+1])
            result_string += ") <-> (" + str(shuffle[0][shuffle[1][1]]) + ", " + str(shuffle[0][shuffle[1][1]+1]) + ')'
        print result_string


def find(array, sorted_array):
    q = deque()
    length = len(array)
    q.append(array)
    previous = {tuple(array): -1}
    moved_pairs = {tuple(array): -1}
    while len(q) != 0:
        array = q.popleft()

        if array == sorted_array:
            print_success(previous, moved_pairs, tuple(sorted_array))
            return True
        for i in range(0, length - 1):
            for j in range(i + 2, length - 1):
                tmp = list(array)
                tmp[i], tmp[j] = tmp[j], tmp[i]
                tmp[i + 1], tmp[j + 1] = tmp[j + 1], tmp[i + 1]
                if not tuple(tmp) in previous:
                    q.append(tmp)
                    previous[tuple(tmp)] = tuple(array)
                    moved_pairs[tuple(tmp)] = [i, j]
    return False

f = open("input.txt", 'r')
inputLine = f.readline()
array = map(int, inputLine.split(','))
sortedArray = sorted(array)

if not find(array, sortedArray):
    print "Array is not sortable."
