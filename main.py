from display import *
from draw import *
from matrix import *

import math

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

m1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
m2 = []
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6). m2 = ")
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)

print("\nTesting identity. m1 = ")
ident(m1)
print_matrix(m1)

print("\nTesting Matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)

print("\nTesting Matrix multiplication. m1 = ")
m1.clear()
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print_matrix(m1)


print("\nTesting Matrix multiplication m1 * m2 = ")
matrix_mult(m1,m2)
print_matrix(m2)


matrix.clear()
amat = []
add_point(matrix,250,0,0)
add_point(amat, 250, 0, 0)
for i in range(120):
    spiralSim(amat, math.pi/60,1,250,250)
    add_point(matrix,amat[0][0],amat[0][1],amat[0][2])
draw_lines(matrix,screen,color)

r = 50.0/60.0
a = 250 + (1 - r) * 250 / (r * r + 1)
b = 250 + (r - r*r) * 250 / (r * r + 1)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)

spiralSim(matrix, math.pi / 2, r, a, b)
draw_lines(matrix,screen,color)
# draw_lines( matrix, screen, color )
# matrix_mult(rotate,matrix)
#
# draw_lines( matrix, screen, color )
#
# matrix_mult(rotate,matrix)
#
# draw_lines( matrix, screen, color )
#
# matrix_mult(rotate,matrix)
#
# draw_lines( matrix, screen, color )
#
# matrix_mult(rotate,matrix)
#
# draw_lines( matrix, screen, color )
#
# matrix_mult(rotate,matrix)
#
# draw_lines( matrix, screen, color )
#
# matrix_mult(rotate,matrix)





display(screen)
