# Write a function to transpose a 2D list.



def transpose_2d_list(lst):
    return [list(i) for i in zip(*lst)]

print(transpose_2d_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
