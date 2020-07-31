# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j] + Z[i][j]
#To print the result
for r in result:
    print(r)

#Finally let's have the full code
# Program to add three matrices using nested loop
# defining matrices using list
X = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

Y = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

Z = [[5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]]

result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j] + Z[i][j]

# printing result
for r in result:
    print(r)
