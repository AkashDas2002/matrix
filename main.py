from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

# m1 = [[1,2,3],[2,0,2],[3,3,3],[0,0,1]]
# m2 = [[2,0,2,0],[3,4,1,0]]
# matrix_mult(m1,m2)
# print_matrix(m2)

add_edge(matrix,0,0,0,50,50,0)

draw_lines( matrix, screen, color )
display(screen)
