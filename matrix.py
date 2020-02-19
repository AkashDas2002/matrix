"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    # xcors = []
    # ycors = []
    # zcors = []
    # ones = []
    # for list in matrix:
    #     xcors.append(str(list[0]))
    #     ycors.append(str(list[1]))
    #     zcors.append(str(list[2]))
    #     ones.append(str(list[3]))
    # print(" ".join(xcors))
    # print(" ".join(ycors))
    # print(" ".join(zcors))
    # print(" ".join(ones))
    listOflists = []
    for i in range(len(matrix[0])):
        listOflists.append([])
        for j in range(len(matrix)):
            listOflists[-1].append(str(matrix[j][i]))
    listOfStrings = [" ".join(list) for list in listOflists]
    print("\n".join(listOfStrings))

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    numRows = len(m1[0])
    numCols = len(m2)
    newmat = []
    for i in range(numCols):
        newmat.append([])
        for j in range(numRows):
            sum = 0
            for n in range(len(m1)):
                sum += m1[n][j] *  m2[i][n]
            newmat[-1].append(sum)
    m2.clear()
    for x in range(numCols):
        m2.append(newmat[x])



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
