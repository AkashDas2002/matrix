from display import *
from draw import *
from matrix import *

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



add_edge(matrix,0,0,0,250,250,0)

draw_lines( matrix, screen, color )
display(screen)
