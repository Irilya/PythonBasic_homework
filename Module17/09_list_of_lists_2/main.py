
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


nice_list_after = [nice_list[i][n][j] for i in range(len(nice_list))
              for n in range(len(nice_list[i]))
              for j in range(len(nice_list[i][n]))]

print(nice_list_after)


