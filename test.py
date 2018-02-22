board1 = ("      @   @\n"
                "     /   /\n"
                "@ - A - B\n"
                "     \\ / \\\n" 
                "  @ - C   @\n"
                "       \\\n        @")

board_1_lst = [["A", "B"], ["C"]]
board_2_lst = [["A", "B"], ["C", "D", "E"], ["F", "G"]]

board2 = ("        @   @\n"
"       /   /\n"
"  @ - A - B   @\n"
"     / \ / \ /\n"
"@ - C - D - E\n"
"     \ / \ / \ \n"
"  @ - F - G   @\n"
"       \   \ \n"
"        @   @\n")


board3= ("          @   @\n"
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

def test(x):
    var = ""
    for i in x:
        if i.isalpha():
            var += (i + "\n")
    return var

#print(test(board3))


def test2(x, y, z):
    z = str(z)
    x2 = x.replace(y, z)
    return x2

#print(test2(board3, 'B', 1))



