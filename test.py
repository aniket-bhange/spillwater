import numpy as np

# stack = np.array([[6, 6, 6, 6, 5, 6],
#                   [6, 0, 2, 6, 1, 6],
#                   [6, 1, 2, 6, 1, 6],
#                   [6, 6, 6, 1, 6, 6],
#                   [0, 0, 0, 0, 0, 0]])


# m,n = stack.shape
# z = np.max(stack)

# water = np.ones((z+1,m,n))


# for level in range(0,z):
#     water[level] = np.where(stack-level <= 0, 1, 0)

# water[0] *= 2

# for level in range(0,z+1):

#     zero = np.argwhere(water[level] == 1)

#     for yy,xx in zero:
#         if xx == 0 or yy == 0 or yy == m-1 or xx == n-1:
#             water[level,yy,xx] = 2

#     count = np.count_nonzero(water[level] == 2)
#     oldcount = 0

#     spill = np.argwhere(water[level] == 2)

#     while oldcount != count:

#         oldcount = count

#         for yy,xx in spill:
            
#             if xx-1 >= 0 and water[level,yy,xx-1] == 1:
#                 water[level,yy,xx-1] = 2
#             if xx+1 < n and water[level,yy,xx+1] == 1:
#                 water[level,yy,xx+1] = 2
#             if yy+1 < m:
#                 if water[level,yy+1,xx] == 1:
#                     water[level,yy+1,xx] = 2
#             if yy-1 >= 0:
#                 if water[level,yy-1,xx] == 1:
#                     water[level,yy-1,xx] = 2
#             if level+1 <= z and water[level+1,yy,xx] == 1:
#                 water[level+1,yy,xx] = 2

#         spill = np.argwhere(water[level] == 2)
#         count = np.count_nonzero(water[level] == 2)

#     water[level] = np.where(water[level] == 1, 1, 0)
#     # print(f"level {level}\n{water[level]}")


# totalcubes = np.sum(water)

# print('\nTotal water blocks = ',totalcubes)

x = np.array([
        [6, 6, 6, 6, 5, 6],
        [6, 0, 2, 6, 1, 6],
        [6, 1, 2, 6, 1, 6],
        [6, 6, 6, 1, 6, 6],
        [0, 0, 0, 0, 0, 0]
    ])
np.save('./numpy/file01', x)