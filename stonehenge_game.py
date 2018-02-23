"""
An implimentation of Stonehenge
"""
from game import Game
from stonehenge_state import StonehengeState

dic1 = {"h": [["@", "A", "B"], ["@", "C"]], "d1": [["@", "A"], ["@", "B", "C"]],
        "d2": [["@", "C", "A"], ["@", "B"]]}

board1 = ("      {}   {}\n"
          "     /   /\n"
          "{} - {} - {}\n"
          "     \\ / \\\n"
          "  {} - {}   {}\n"
          "       \\\n        {}".format(dic1["d1"][0][0],
                                         dic1["d1"][1][0],
                                         dic1["h"][0][0],
                                         dic1["h"][0][1],
                                         dic1["h"][0][2],
                                         dic1["h"][1][0],
                                         dic1["h"][1][1],
                                         dic1["d2"][1][0],
                                         dic1["d2"][0][0]))

dic2 = {"h": [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G"]],
        "d1": [["@", "A", "C"], ["@", "B", "D", "F"], ["@", "E", "G"]],
        "d2": [["@", "F", "C"], ["@", "G", "D", "A"], ["@", "E", "B"]]}

board2 = ('        {}   {}\n'
          '       /   /\n'
          '  {} - {} - {}   {}\n'
          '     / \ / \ /\n'
          '{} - {} - {} - {}\n'
          '     \ / \ / \ \n'
          '  {} - {} - {}   {}\n'
          '       \   \ \n'
          '        {}   {}'.format(dic2["d1"][0][0],
                                   dic2["d1"][1][0],
                                   dic2["h"][0][0],
                                   dic2["h"][0][1],
                                   dic2["h"][0][2],
                                   dic2["d1"][2][0],
                                   dic2["h"][1][0],
                                   dic2["h"][1][1],
                                   dic2["h"][1][2],
                                   dic2["h"][1][3],
                                   dic2["h"][2][0],
                                   dic2["h"][2][1],
                                   dic2["h"][2][2],
                                   dic2['d2'][2][0],
                                   dic2["d2"][0][0],
                                   dic2["d2"][1][0]))

dic3 = {"h": [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G", "H", "I"],
              ["@", "J", "K", "L"]],
        "d1": [["@", "A", "C", "F"], ["@", "B", "D", "G", "J"],
               ["@", "E", "H", "K"], ["@", "I", "L"]],
        "d2": [["@", "J", "F"], ["@", "K", "G", "C"], ["@", "L", "H", "D", "A"],
               ["@", "I", "E", "B"]]}

board3 = ('          @   @\n'
          '         /   /\n'
          '    @ - A - B   @\n'
          '     \ / \ / \ / \n'
          '  @ - C - D - E   @\n'
          '     / \ / \ / \ /\n'
          '@ - F - G - H - I\n'
          '     \ / \ / \ / \ \n'
          '  @ - J - K - L   @ \n'
          '        \   \   \ \n'
          '         @   @   @\n'.format())


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
          "       \   \   \   \ \n"
          "        @   @   @   @\n")

dic4 = {"h": [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G", "H", "I"],
              ["@", "J", "K", "L", "M", "N"],
              ["@", "O", "P", "Q", "R"]],
        "d1": [["@", "A", "C", "F", "J"], ["@", "B", "D", "G", "K", "O"],
               ["@", "E", "H", "L", "P"], ["@", "I", "M", "Q"],
               ["@", "N", "R"]],
        "d2": [["@", "O", "J"], ["@", "P", "K", "F"], ["@", "Q", "L", "G", "C"],
               ["@", "R", "M", "H", "D", "A"], ["@", "N", "I", "E", "B"]]}

dic = {1: [board1, dic1], 2: [board2, dic2], 3: [board3, dic3],
       4: [board4, dic4]}


class Stonehenge(Game):
    """
        Abstract class for a game to be played with two players.
        """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        len_game = ''
        self.length = int(input("Enter the length of stonehenge: "))
        for x in dic:
            if x == self.length:
                len_game = dic[x]
        self.current_dic = len_game[1]
        self.current_state = StonehengeState(p1_starts, len_game[0],
                                             len_game[1])

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns claiming cells When a  " + \
                       "player captures at least half of the cells in a " + \
                       "ley-line, then the player captures that ley-line." + \
                       " The first player to capture at least half of the " + \
                       "ley-lines is the winner. "
        return instructions

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        # return not any(i.isalpha() for i in state)

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        lst = []
        for value in self.current_dic.values():
            for i in value:
                lst.append(i[0])
        p1 = lst.count(1)
        p2 = lst.count(2)
        if p1 > p2 and player == 'p1':
            return True
        elif p2 > p1 and player == 'p2':
            return True
        return False

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return:
        :rtype:
        """
        # TODO: Impliment this
        if not string.strip().isalpha():
            return -1

        # TODO: use upper to test for

        return str(string.strip())


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
