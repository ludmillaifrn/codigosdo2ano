at = [[28, 14, 11], [6, 15, 9], [95, 24, 1]]
min = mat[1][1]
max = mat[1][1]

for i in range(3):
    for j in range(3):
        comp_1 = mat[i][j]
        comp_2 = mat[i-1][j-1]
        if comp_1 > comp_2:
            if max < comp_1:
                max = comp_1
            ver1 = comp_2
            if ver1 < min:
                min = ver1
        elif comp_1 < comp_2:
            if min > comp_1:
                min = comp_1
            ver2 = comp_2
            if ver2 > max:
                max = ver2

print(max,min)
