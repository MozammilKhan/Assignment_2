"""
An implementation of a state for SubtractSquare.

NOTE: You do not have to run python-ta on this file.
"""
from typing import Any
from game_state import GameState
import copy


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, current_state: str, current_dic) \
            -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.current_dic = current_dic
        self.current_state = current_state
        print(self.current_dic)

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return self.current_state

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        moves = ""
        for i in self.current_state:
            if i.isalpha():
                moves += i
        return moves

    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        # TODO fix this
        if self.p1_turn:
            new_move = "1"
        elif not self.p1_turn:
            new_move = "2"
        new_dic = copy.deepcopy(self.current_dic)
        # changing the items in the dictionary
        for value in new_dic.values():
            for lst in value:
                if move in lst:
                    lst[lst.index(move)] = new_move
                if (len(lst) - 1) / 2 <= lst.count(new_move) and "@" in lst:
                    lst[lst.index("@")] = new_move
        board1 = ("      {}   {}\n"
                  "     /   /\n"
                  "{} - {} - {}\n"
                  "     \\ / \\\n"
                  "  {} - {}   {}\n"
                  "       \\\n        {}".format(new_dic["d1"][0][0],
                                                 new_dic["d1"][1][0],
                                                 new_dic["h"][0][0],
                                                 new_dic["h"][0][1],
                                                 new_dic["h"][0][2],
                                                 new_dic["h"][1][0],
                                                 new_dic["h"][1][1],
                                                 new_dic["d2"][1][0],
                                                 new_dic["d2"][0][0]))
        board2 = ('        {}   {}\n'
                  '       /   /\n'
                  '  {} - {} - {}   {}\n'
                  '     / \ / \ /\n'
                  '{} - {} - {} - {}\n'
                  '     \ / \ / \ \n'
                  '  {} - {} - {}   {}\n'
                  '       \   \ \n'
                  '        {}   {}'.format(new_dic["d1"][0][0],
                                           new_dic["d1"][1][0],
                                           new_dic["h"][0][0],
                                           new_dic["h"][0][1],
                                           new_dic["h"][0][2],
                                           new_dic["d1"][2][0],
                                           new_dic["h"][1][0],
                                           new_dic["h"][1][1],
                                           new_dic["h"][1][2],
                                           new_dic["h"][1][3],
                                           new_dic["h"][2][0],
                                           new_dic["h"][2][1],
                                           new_dic["h"][2][2],
                                           new_dic['d2'][2][0],
                                           new_dic["d2"][0][0],
                                           new_dic["d2"][1][0]))
        new = board2

        new_state = StonehengeState(not self.p1_turn,
                                    new, new_dic)
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - State: {}".format(self.p1_turn,
                                                  self.current_state)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        # TODO idk what this is
        pass


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
