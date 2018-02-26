board1 = ("      @   @\n"
          "     /   /\n"
          "@ - A - B\n"
          "     \\ / \\\n"
          "  @ - C   @\n"
          "       \\\n        @")

board2 = ("        @   @\n"
          "       /   /\n"
          "  @ - A - B   @\n"
          "     / \ / \ /\n"
          "@ - C - D - E\n"
          "     \ / \ / \ \n"
          "  @ - F - G   @\n"
          "       \   \ \n"
          "        @   @\n")

board3 = ("          @   @\n"
          "         /   /\n"
          "    @ - A - B   @\n"
          "     \ / \ / \ / \n"
          "  @ - C - D - E   @\n"
          "     / \ / \ / \ /\n"
          "@ - F - G - H - I\n"
          "     \ / \ / \ / \ \n"
          "  @ - J - K - L   @ \n"
          "        \   \   \ \n"
          "         @   @   @\n")

board4 = ("            @   @\n"
          "           /   /\n"
          "      @ - A - B   @\n"
          "       \ / \ / \ / \n"
          "    @ - C - D - E   @\n"
          "       / \ / \ / \ /\n"
          "  @ - F - G - H - I   @\n"
          "     / \ / \ / \ / \ / \n"
          "@ - J - K - L - M - N\n"
          "     \ / \ / \ / \ / \ \n"
          "  @ - O - P - Q - R   @\n"
          "        \    \   \   \ \n"
          "         @   @   @    @\n")

print(board1 + "\n")
print(board2 + "\n")
print(board3 + "\n")
print(board4)


dic1 = {"h": [["@", "A", "B"], ["@", "C"]], "d1": [["@", "A"], ["@", "B", "C"]],
        "d2": [["@", "C", "A"], ["@", "B"]]}


def test(x):
    """
    testing trying to replace all the "A" with "5"
    """
    new_lst = []
    for value in x.values():
        for lst in value:
            new_lst.append(lst[0])

    print(new_lst)


print(test(dic1))
