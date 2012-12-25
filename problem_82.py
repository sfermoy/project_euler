from numpy import *
mat = genfromtxt("prob_82_input.txt", delimiter=",")
#mat= genfromtxt("prob_82_test.txt")


def smallest_unvisited(values, visited):
    min_index = unravel_index(values.argmin(), values.shape)
    if visited[min_index[0], min_index[1]] > 0:
        values[min_index[0], min_index[1]] = 20 ** 12  # infinity
        return smallest_unvisited(values, visited)
    else:
        return [values, min_index]


def dikjstra(matrix):
    nrows = len(matrix)
    mcols = len(matrix[0])
    tentitive = array(
        [[10 ** 12 for x in xrange(mcols)] for x in xrange(nrows)])  # infinity
    result = array([[0 for x in xrange(mcols)] for x in xrange(nrows)])
    #add source with edge weight 0 to all first column nodes
    tentitive[:, 0] = matrix[:, 0]

    for z in xrange((nrows * mcols)):
        tentitive, index = smallest_unvisited(tentitive, result)

        i = index[0]
        j = index[1]
        # rules for which nodes are connected
        if i == 0:
            #down
            option = matrix[i + 1, j] + tentitive[i, j]
            if option < tentitive[i + 1, j]:
                tentitive[i + 1, j] = option

        elif i == (nrows - 1):
            #up
            option = matrix[i - 1, j] + tentitive[i, j]
            if option < tentitive[i - 1, j]:
                tentitive[i - 1, j] = option

        else:
            #up
            option = matrix[i - 1, j] + tentitive[i, j]
            if option < tentitive[i - 1, j]:
                tentitive[i - 1, j] = option
            #down
            option = matrix[i + 1, j] + tentitive[i, j]
            if option < tentitive[i + 1, j]:
                tentitive[i + 1, j] = option

        if j < (mcols - 1):
            #right
            option = matrix[i, j + 1] + tentitive[i, j]
            if option < tentitive[i, j + 1]:
                tentitive[i, j + 1] = option

        matrix[i, j] = tentitive[i, j]
        result[i, j] = tentitive[i, j]
    return result

######main#############
result = dikjstra(mat)
last_column = result[:, len(mat) - 1]
print min(last_column)
